<!--
author:   Bruna Piereck, Janick Mathys, Boris Depoortere, VIB-BIC training
email:    trainingandconferences@vib.be
version:  2.0.0
language: en
narrator: UK English Female

icon:     https://vib.be/sites/vib.sites.vib.be/files/logo_VIB_noTagline.svg

comment:  This document shall provide an entire compendium and course on the
          development of Open-courSes with [LiaScript](https://LiaScript.github.io).
          As the language and the systems grows, also this document will be updated.
          Feel free to fork or copy it, translations are very welcome...

script:   https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.js
          https://felixhao28.github.io/JSCPP/dist/JSCPP.es5.min.js

link:     https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.css
link:     https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css
link:     https://raw.githubusercontent.com/vibbits/material-liascript/master/img/org.css
link:     https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css
link:     https://fonts.googleapis.com/css2?family=Saira+Condensed:wght@300&display=swap
link:     https://fonts.googleapis.com/css2?family=Open+Sans&display=swap
link:     https://raw.githubusercontent.com/vibbits/material-liascript/master/vib-styles.css

tutor:    VIB
edition:  2nd 

@JSONLD
<script run-once>
  let json = @0 

  const script = document.createElement('script');
  script.type = 'application/ld+json';
  script.text = JSON.stringify(json);

  document.head.appendChild(script);

  // this is only needed to prevent and output,
  // as long as the result of a script is undefined,
  // it is not shown or rendered within LiaScript
  console.debug("added json to head")
</script>
@end

orcid:    [@0](@1)<!--class="orcid-logo-for-author-list"
-->

# Introduction to HPC

> This material is inspired and using extracs from [**"HCP Training Bio-imaging"**](https://github.com/vib-bic-training/HPC_training_bioimaging_1), by Benjamin Pavie and Tatiana Woller. Use was authorized.

>This material in under active development at the moment.

<section>

> We are using the interactive Open Educational Resource online/offline course infrastructure called LiaScript.
> It is a distributed way of creating and sharing educational content hosted on github.
> To see this document as an interactive LiaScript rendered version, click on the
> following link/badge: [LiaScript](https://liascript.github.io/course/)

## General context

Welcome to our **Introduction to HPC** VIB workshop! We are very happy to have you here.

This is the 2nd edition of this workshop

The half day session aims to introduce the different options available withing the Flemish system, while enabling students to quickly adapt to any HPC system they might access around the globe. With some best practices and differences and similarities within each system.

The **presentation** which goes alongside this material can be found [here](https://docs.google.com/presentation/d/1J6qROZ35JVeKpVx8TAjWNtbsjescx95ZtqbBCV8vYrg/edit?usp=sharing).

## Proposed Schedule

Half day Schedule:

- 13:00 - 13:30 - Introduction
- 13:30 - 15:00 - Accessing in the terminal and OnDemand
- 15:00 - 15:15 - Coffee Break
- 15:15 - 16:00 - Interactive sessions (debug and testing)
- 16:00 - 16:30 - Querying and using modules in the HPC
- 16:30 - 17:00 - Submitting and managing jobs

</section>

# Lesson overview

> <i class="fa fa-lock"></i> **License:** [Creative Commons Attribution share alike 4.0 International  License](https://creativecommons.org/licenses/by-sa/4.0/deed.en)
>
> <i class="fa fa-user"></i> **Target Audience:** Researchers, Technitians, trainers, anyone with interest in using HPC
>
> <svg xmlns="http://www.w3.org/2000/svg" height="14" width="16" viewBox="0 0 576 512"><!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2023 Fonticons, Inc.--><path d="M384 64c0-17.7 14.3-32 32-32H544c17.7 0 32 14.3 32 32s-14.3 32-32 32H448v96c0 17.7-14.3 32-32 32H320v96c0 17.7-14.3 32-32 32H192v96c0 17.7-14.3 32-32 32H32c-17.7 0-32-14.3-32-32s14.3-32 32-32h96V320c0-17.7 14.3-32 32-32h96V192c0-17.7 14.3-32 32-32h96V64z"/></svg> **Level:** Beginner  
>
> <i class="fa fa-arrow-left"></i> **Prerequisites**  
> To be able to follow this course, learners should have knowledge in:
> 
> 1. Basic of command line  
>
> <i class="fa fa-bookmark"></i> **Description**  

> In this half-day introduction, you will have the opportunity to know a bit more about the structure of the HPC (tiers), what resources you have available, and most importantly, how to use and navigate the HPC. 
>
> In this course, you will learn the differences and similarities between
>
> - VSC (Vlaams Supercomputer Centrum) instances in Gent and Leuven
>
> - VIB Data Core
>
> - And a glimpse of what you could find beyond.
>
> It is our aim that you can more easily adjust to any HPC system that you encounter in your professional life.
> 
> <i class="fa fa-arrow-right"></i> **Learning Outcomes:**  
> By the end of the course, learners will be able to:
>
> 1. Describe differences and similarities among HPC Tiers and usage
>
> 2. Access existing HPC infrastructures in Flanders, such as VSC and VIB Data Core
>
> 3. Use the different environments in the HPC (storage, analysis, and debug)
>
> 4. Querying and using modules and their versions in the HPC
>
> 5. Submit jobs to use software and scripts on the cluster
>
> 6. Check information about submitted jobs
>
> <i class="fa fa-hourglass"></i> **Time estimation**: 4 hours
>
> <i class="fa fa-asterisk"></i> **Requirements:** The (technical) installation requirements are described in [Chapter 2](./chapters/02_GetReady4course.md)
>
> <i class="fa fa-envelope-open-text"></i> **Supporting Materials**:
> 
> - How to connect to the Open On Demand interface:  https://tier.hpc.ugent.be 
>
> - How to install Globus for windows: : https://docs.globus.org/globus-connect-personal/install/windows/
>
> - Documentation VSC: https://docs.vscentrum.be
> 
> <i class="fa fa-life-ring"></i> **Acknowledgement**:
>
> * [VIB Data Core](https://datacore.sites.vib.be/en)
> * [VIB Bioimaging Core Leuven](https://bioimagingcore-leuven.sites.vib.be/en)
>
> <i class="fa fa-money-bill"></i> **Funding:** 
>
> <i class="fa fa-anchor"></i> **PURL**:  


# Authors and Contributors

Authors

- [Bruna Piereck](@[orcid](https://orcid.org/0000-0001-6691-4233))
- [Janick Mathys](@[orcid](https://orcid.org/0009-0007-1722-2370))

Contributors

- [Boris Depoortere](@[orcid](https://orcid.org/0009-0002-2539-116X))

## Citing this lesson

Please cite as:

  1. ...

# Chapters List

Material for the HPC training.

## [Lesson Overview](chapters/01_LessonOverview.md)

[preview-lia](https://raw.githubusercontent.com/vib-tcp/introduction_2_HPC/refs/heads/main/chapters/01_LessonOverview.md)

## [Course preparation](chapters/02_GetReady4course.md)

## [HPC Infrastructure](chapters/03_Infrastructure.md)

## [Connecting to HPCs](chapters/04_connecting_2_resources.md)

## [Transferring Data](chapters/05_data_transfer.md)

## [Software on HPCs](chapters/06_software.md)

## [Jupyter Notebooks](chapters/07_jupyter_notebook.md)

## [VIB Data Core Compute](chapters/vib_compute.md)



```json   @JSONLD
{
  "@context": "https://schema.org/",
  "@type": "LearningResource",
  "@id": "https://elixir-europe-training.github.io/ELIXIR-TrP-TeSS/",
  "http://purl.org/dc/terms/conformsTo": {
    "@type": "CreativeWork",
    "@id": "https://bioschemas.org/profiles/TrainingMaterial/1.0-RELEASE"
  },
  "description": "In this course you will learn about the structure of the HPC (tiers), what resources you have available, and most importantly, how to use and navigate the HPC. We focus on the VSC (Vlaams Supercomputer Centrum) instances and VIB Data Core cluster computer. Most of them use Slurm what could be used similarly in other HPCs. Our goal is to help you easily adapt to any HPC system you encounter in your professional life",
  "keywords": "HPC, Data Analysis, OPEN, Bioinformatics, Slurm, VSC",
  "name": "Introduction to HPC",
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "educationalLevel": "beginner",
  "competencyRequired": "none",
  "teaches": [
    "How to request and connect to the HPC",
    "How to allocate resources and send Jobs to the queue",
    "How to manage and debug Jobs"
    "Best practices in the HPC"
  ],
  "audience": "Anyone with interest in using HPC for data analysis",
  "inLanguage": "en-US",
  "learningResourceType": [
    "Slides, Activities"
  ],
  "author": [
    {
      "@type": "Person",
      "name": "Bruna Piereck"
    },
    {
      "@type": "Person",
      "name": "Janick Mathys"
    },
  ],
  "contributor": [
    {
      "@type": "Person",
      "name": "Boris Depoortere"
    },
  ]
}
```
