#!/usr/bin/env python3
"""Assemble the single-file LiaScript course from README.md + docs/chapters/*.md.

LiaScript builds its sidebar from the headings of the *one* document the player is
pointed at; its `import:` header only pulls in definitions (script/link/macros), not
content. So a course split across files cannot show up as sidebar chapters unless the
files are concatenated first. This script does that concatenation.

Run locally with:  python3 .github/scripts/build_course.py
"""

from __future__ import annotations

import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
CHAPTER_DIR = ROOT / "docs" / "chapters"
OUTPUT = ROOT / "course.md"

# The README section that starts the trailing "meta" part of the document. Everything
# from this heading onwards is moved *after* the chapters so the sidebar reads
# overview -> chapters -> colophon.
TAIL_MARKER = "# Workshop and Material organization"

# Must be emitted *after* the header comment, never before it: LiaScript only reads
# course metadata from the first HTML comment in the document, so putting this note
# first silently drops author, version, narrator, links/scripts and all macros. It also
# cannot live inside the header comment, where a line that is not `key: value` makes
# LiaScript discard the entire header.
GENERATED_NOTE = (
    "<!-- GENERATED FILE - DO NOT EDIT.\n"
    "     Built by .github/scripts/build_course.py from README.md and docs/chapters/*.md.\n"
    "     Edit those files instead; this one is regenerated on every push to main. -->"
)


def fail(msg: str) -> "None":
    sys.exit(f"build_course: {msg}")


def slug(title: str) -> str:
    """Approximate LiaScript's heading anchors: lowercase, punctuation dropped,
    whitespace collapsed to single hyphens. Non-ASCII (e.g. emoji) is kept."""
    text = unicodedata.normalize("NFC", title).strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return re.sub(r"[\s_]+", "-", text).strip("-")


def chapter_key(filename: str) -> str:
    """Normalise a chapter filename so links survive the numbering drift in this repo
    (several cross-references point at e.g. 02_GetReady4course.md when the file is
    actually 01_GetReady4course.md)."""
    stem = pathlib.Path(filename).stem
    return re.sub(r"[^a-z0-9]", "", re.sub(r"^\d+[_-]*", "", stem).lower())


def split_header(text: str) -> "tuple[str, str]":
    """Return (leading HTML comment block, rest). Empty header if the file has none."""
    stripped = text.lstrip()
    if not stripped.startswith("<!--"):
        return "", text
    end = text.index("-->", text.index("<!--")) + len("-->")
    return text[:end], text[end:]


def iter_lines_outside_code(text: str):
    """Yield (line, in_code) so heading rewrites skip fenced code blocks."""
    fence = None
    for line in text.split("\n"):
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if match:
            marker, info = match.group(1)[0], match.group(2)
            # CommonMark: the info string of a backtick fence may not contain
            # backticks. That rules out lines such as ``` ml show IPython ```, which
            # are inline code written with the wrong delimiter, not block openers.
            valid = marker == "~" or "`" not in info
            if fence is None and valid:
                fence = marker
                yield line, True
                continue
            if fence is not None and marker == fence and not info.strip():
                fence = None
                yield line, True
                continue
        yield line, fence is not None


def shift_headings(body: str, title: str) -> str:
    """Prefix the chapter with `# <title>` and push its own headings down so its
    top-most level lands at 2, keeping one sidebar chapter per file."""
    lines = list(iter_lines_outside_code(body))
    levels = [
        len(m.group(1))
        for line, in_code in lines
        if not in_code and (m := re.match(r"^(#{1,6})\s+\S", line))
    ]
    if not levels:
        fail(f"no headings found in chapter {title!r}")

    shift = 2 - min(levels)
    if max(levels) + shift > 6:
        shift = 6 - max(levels)
    shift = max(shift, 0)

    out = []
    for line, in_code in lines:
        m = re.match(r"^(#{1,6})(\s+\S.*)$", line)
        if not in_code and m:
            line = "#" * min(len(m.group(1)) + shift, 6) + m.group(2)
        out.append(line)
    return f"# {title}\n\n" + "\n".join(out).strip("\n")


def rewrite_links(text: str, anchors: "dict[str, str]") -> str:
    """Point in-repo references at the combined document instead of at loose files."""

    def chapter_link(match: "re.Match[str]") -> str:
        filename, fragment = match.group("file"), match.group("frag") or ""
        if fragment:
            # The sub-heading keeps its text (only its level changed), so its own
            # anchor still resolves inside the combined document.
            return "(" + fragment + ")"
        anchor = anchors.get(chapter_key(filename))
        if anchor is None:
            print(f"  ! unresolved chapter link: {filename}", file=sys.stderr)
            return match.group(0)
        return f"(#{anchor})"

    # Matches ./chapters/x.md, ../chapters/x.md, ./docs/chapters/x.md and the
    # extension-less root-absolute form /chapters/x used in a few places.
    text = re.sub(
        r"\((?:\.{0,2}/)+(?:docs/)?chapters/(?P<file>[^)#]+?)(?:\.md)?(?P<frag>#[^)]*)?\)",
        chapter_link,
        text,
    )
    # course.md lives at the repo root, so image paths have to be root-relative.
    # `../images/...` is valid from docs/chapters/ but resolves to docs/images/, which
    # does not exist; `/images/...` resolves against the LiaScript host. Both are
    # already broken today, in the chapter files as well as in the rendered course.
    text = re.sub(r'(src=")(?:\.{0,2}/)+images/', r"\1images/", text)
    text = re.sub(r"(\]\()(?:\.{0,2}/)+images/", r"\1images/", text)
    return text


def parse_chapters(readme: str) -> "list[tuple[pathlib.Path, str]]":
    """Read the chapter order from README's `# Chapters List` table, so adding a row
    there is all it takes to add a chapter to the course."""
    table = re.search(r"#\s*Chapters List(?P<body>.*?)(?:\n\s*\n|\Z)", readme, re.S)
    if not table:
        fail("could not find the '# Chapters List' table in README.md")

    rows = re.findall(
        r"\[(?P<title>[^\]]+)\]\((?:\./|\.\./)?(?:docs/)?chapters/(?P<file>[^)#]+\.md)\)",
        table.group("body"),
    )
    if not rows:
        fail("the '# Chapters List' table contains no chapter links")

    by_key = {chapter_key(p.name): p for p in sorted(CHAPTER_DIR.glob("*.md"))}
    chapters = []
    for title, filename in rows:
        path = by_key.get(chapter_key(filename))
        if path is None:
            fail(f"chapter file for {filename!r} (listed as {title!r}) does not exist")
        chapters.append((path, title.strip()))

    missing = set(by_key.values()) - {p for p, _ in chapters}
    for path in sorted(missing):
        print(f"  ! not listed in the Chapters List, skipped: {path.name}", file=sys.stderr)
    return chapters


def main() -> None:
    readme = README.read_text(encoding="utf-8")
    header, body = split_header(readme)
    if not header:
        fail("README.md has no leading LiaScript header comment")
    if TAIL_MARKER not in body:
        fail(f"README.md has no {TAIL_MARKER!r} section to split on")

    overview, tail = body.split(TAIL_MARKER, 1)
    tail = TAIL_MARKER + tail

    chapters = parse_chapters(readme)
    anchors = {chapter_key(path.name): slug(title) for path, title in chapters}

    parts = [header.strip(), GENERATED_NOTE, overview.strip()]
    for path, title in chapters:
        _, chapter_body = split_header(path.read_text(encoding="utf-8"))
        parts.append(shift_headings(chapter_body.strip(), title))
        print(f"  + {path.name} -> # {title}")
    parts.append(tail.strip())

    OUTPUT.write_text(rewrite_links("\n\n".join(parts), anchors) + "\n", encoding="utf-8")
    print(f"  = wrote {OUTPUT.relative_to(ROOT)} ({len(chapters)} chapters)")


if __name__ == "__main__":
    main()
