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

Lesson overview
-----------------

> <i class="fa fa-lock"></i> **License:** [Creative Commons Attribution share alike 4.0 International  License](https://creativecommons.org/licenses/by-sa/4.0/deed.en)
>
> <i class="fa fa-user"></i> **Target Audience:** Researchers, Technicians, trainers, anyone with interest in using HPC
>
> <svg xmlns="http://www.w3.org/2000/svg" height="14" width="16" viewBox="0 0 576 512"><!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2023 Fonticons, Inc.--><path d="M384 64c0-17.7 14.3-32 32-32H544c17.7 0 32 14.3 32 32s-14.3 32-32 32H448v96c0 17.7-14.3 32-32 32H320v96c0 17.7-14.3 32-32 32H192v96c0 17.7-14.3 32-32 32H32c-17.7 0-32-14.3-32-32s14.3-32 32-32h96V320c0-17.7 14.3-32 32-32h96V192c0-17.7 14.3-32 32-32h96V64z"/></svg> **Level:** Beginner  
>
> <i class="fa fa-arrow-left"></i> **Prerequisites**  
> To be able to follow this course, learners should:
> 
> Have basic command-line skills. 
>
> If you lack command-line experience, you can prepare by following this [e-learning or Linux introduction](https://www.vibtrainingandconferences.be/events?f%5B0%5D=status%3Aupcoming&text=linux).
>
> <i class="fa fa-bookmark"></i> **Description**  
>
> Large-scale data analysis and complex computations often exceed the limits of standard computing resources. This half-day course provides researchers and professionals with essential knowledge to confidently work with High Performance Computing (HPC) environments. 
>
> During the session, you will explore the structure of HPC systems, understand available resources, and learn practical techniques for navigating and using these environments effectively. The course highlights the differences and similarities among the VSC instances in Ghent and Leuven and the VIB Data Core. 
> 
>The **presentation** which goes alongside this material can be found [here](https://docs.google.com/presentation/d/1J6qROZ35JVeKpVx8TAjWNtbsjescx95ZtqbBCV8vYrg/edit?usp=sharing).
>
> <i class="fa fa-arrow-right"></i> **Learning Outcomes:**  
> By the end of the course, learners will be able to:
>
> 1. Identify differences and similarities among different HPC instances
> 2. Access existing HPC infrastructures in Flanders, including VSC and VIB Data Core
> 3. Navigate and use different HPC environments (storage, analysis, and debug)
> 4. Query and manage specific modules on the HPC
> 5. Submit jobs to run software and scripts on the compute cluster
> 6. Monitor and check information about submitted jobs
>
> <i class="fa fa-hourglass"></i> **Time estimation**: 4.5 hours (1/2 day)
>
> <i class="fa fa-asterisk"></i> **Requirements:** The (technical) installation requirements are described in the chapter [Get ready](./docs/chapters/01_GetReady4course.md)
>
> <i class="fa fa-envelope-open-text"></i> **Supporting Materials**:
> 
> 1. [Presentation](./docs/presentations/)
>
> 2. Extra info about HPC in Flanders and data transfer
>
>    * How to connect to the Open On Demand interface of Tier2 UGent: https://tier.hpc.ugent.be 
>
>    * How to install Globus for Data transfer on Windows: https://docs.globus.org/globus-connect-personal/install/windows/
>
>    * Documentation VSC (***Vlaams Supercomputer Centrum***): https://docs.vscentrum.be
> 
> ## Proposed Schedule
>
>> - 13:00 - 13:30 - Introduction
>> - 13:30 - 15:00  -Access through terminal and browser
>> - 15:00 - 15:15 - Coffee Break
>> - 15:15 - 16:00 - Interactive sessions (debug and testing)
>> - 16:00 - 16:30 - Querying and using modules in the HPC
>> - 16:30 - 17:00 - Submitting and managing jobs
>
> <i class="fa fa-life-ring"></i> **Acknowledgement**:
>
> * [VIB Data Core](https://datacore.sites.vib.be/en)
> * [VIB Bioimaging Core Leuven](https://bioimagingcore-leuven.sites.vib.be/en)
>
> <i class="fa fa-money-bill"></i> **Funding:** This project has received funding from VIB.
>
> <i class="fa fa-anchor"></i> **PURL**:  <span style="color:red">not yet available</span>
>
> # Authors and Contributors
>
> Authors
>
>[<img src="https://raw.githubusercontent.com/vib-training-conferences/training_material_template/refs/heads/main/docs/images/ORCID-iD_icon_vector.svg" width="20"/>](https://orcid.org/0000-0001-6691-4233) Bruna Piereck
>
>[<img src="https://raw.githubusercontent.com/vib-training-conferences/training_material_template/refs/heads/main/docs/images/ORCID-iD_icon_vector.svg" width="20"/>](https://orcid.org/0009-0007-1722-2370)  Janick Mathys
>
> Contributors
>
>[<img src="https://raw.githubusercontent.com/vib-training-conferences/training_material_template/refs/heads/main/docs/images/ORCID-iD_icon_vector.svg" width="20"/>](https://orcid.org/0009-0002-2539-116X)  Boris Depoortere
>
>**We welcome contributors for these materials**
>
> ## Citing this lesson
>
> Please cite as:
>
> <span style="color:red">to be updated soon</span>
>
> # Chapters List
> 
> | Chapter | Title |
> | :---    | :---  |
> |1        |[Get ready for the course, instalation and accounts](./docs/chapters/01_GetReady4course.md)|
> |2        |[HPC Infrastructure](./docs/chapters/03_Infrastructure.md)|
> |3        |[Connecting to HPCs](./docs/chapters/03_connecting_2_resources.md)|
> |4        |[VIB Data Core Compute](./docs/chapters/04_vib_compute.md)|
> |5        |[Transferring Data](./docs/chapters/05_data_transfer.md)|
> |6        |[Software on HPCs](./docs/chapters/06_software.md)|
> |7        |[Jupyter Notebooks](./docs/chapters/07_jupyter_notebook.md)|

# Workshop and Material organization

> We are using the interactive Open Educational Resource online/offline course infrastructure called LiaScript.
> It is a distributed way of creating and sharing educational content hosted on github.
> To see this document as an interactive LiaScript rendered version, click on the
> following link/badge: [LiaScript](https://liascript.github.io/course/)

# References

* This material is inspired and uses excerpts from [**"HCP Training Bio-imaging"**](https://github.com/vib-bic-training/HPC_training_bioimaging_1), by Benjamin Pavie and Tatiana Woller. Use was authorized.

* We use information available in the [VSC (***Vlaams Supercomputer Centrum***) Documentation](https://docs.vscentrum.be)

* We also use information availabl only for VIB personel in the [VIB Data Core documentation](https://docs.datacore.vib.be/)

# About us

*About ELIXIR Training Platform*

The ELIXIR Training Platform was established to develop a training community that spans all ELIXIR member states (see the list of Training Coordinators). It aims to strengthen national training programmes, grow bioinformatics training capacity and competence across Europe, and empower researchers to use ELIXIR's services and tools.

One service offered by the Training Platform is TeSS, the training registry for the ELIXIR community. Together with ELIXIR France and ELIXIR Slovenia, VIB as lead node for ELIXIR Belgium is engaged in consolidating quality and impact of the TeSS training resources (2022-23) (https://elixir-europe.org/internal-projects/commissioned-services/2022-trp3).

The Training eSupport System was developed to help trainees, trainers and their institutions to have a one-stop shop where they can share and find information about training and events, including training material. This way we can create a catalogue that can be shared within the community. How it works is what we are going to find out in this course.

*About VIB and VIB Technologies*

VIB is an entrepreneurial non-profit research institute, with a clear focus on groundbreaking strategic basic research in life sciences and operates in close partnership with the five universities in Flanders – Ghent University, KU Leuven, University of Antwerp, Vrije Universiteit Brussel and Hasselt University.

As part of the VIB Technologies, the 12 VIB Core Facilities, provide support in a wide array of research fields and housing specialized scientific equipment for each discipline. Science and technology go hand in hand. New technologies advance science and often accelerate breakthroughs in scientific research. VIB has a visionary approach to science and technology, founded on its ability to identify and foster new innovations in life sciences.

The goal of VIB Technology Training is to up-skill life scientists to excel in the domains of VIB Technologies, Bioinformatics & AI, Software Development, and Research Data Management.

--------------------------------------------

*Editorial team for this course*

Authors: @[orcid(Alexander Botzki)](https://orcid.org/0000-0001-6691-4233), @[orcid(Bruna Piereck)](https://orcid.org/0000-0001-5958-0669)

Technical Editors: Alexander Botzki

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
  "keywords": "HPC, Data Analysis, OPEN, Bioinformatics, Slurm, Torque, VSC",
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
