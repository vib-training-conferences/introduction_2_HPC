<!--

author:   Tatiana Woller, Bruna Piereck, Alexander Botzki
email:    trainingandconferences@vib.be
version:  1.0.0
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

@orcid: [@0](@1)<!--class="orcid-logo-for-author-list"-->

# Introduction to HPC usage

> This material in under active development at the moment

**Hello and welcome to our HPC workshop, we are very happy to have you here!** 
================================================================================
**This material is derived from ["HPC training Bio-imaging"](https://liascript.github.io/course/?https://raw.githubusercontent.com/vib-bic-training/HPC_training_bioimaging_1/refs/heads/main/README.md#1)**
========================================================================================

> This material is a distributed way of creating and sharing educational content hosted on github.
> To see this document as an interactive LiaScript rendered version (WIP), click on the
> following link/badge:
>
> [![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?link)

<section>

### Lesson overview

> <i class="fa fa-bookmark"></i> **Description**  
> This is our interactive hands-on course about the use of HPC (High Performance Computing). Here you will learn about different HPC structures, their similarities and specificities. You will learn best practices to submit and have good registry of your 'jobs' and to check the list of available software. The aim is that understanding the building blocks your are not only able to use the VSC and VIB resources, but can easily adapt whenever facing another instance of HPC.
> 
> <i class="fa fa-arrow-left"></i> **Prerequisites**  
> To be able to follow the **General** HPC course, you should:
> 
> 1. Have notions of command line in Unix-based system
>
> <i class="fa fa-asterisk"></i> **General Requirements (Technical):** 
> You can find here a list of technical details you need to get prepared in oder to follow this course. You can find some help on ***HOW?*** in the specific sessions in the material of this course. 
>
> - Create a VSC account 
>
> Check the [Get ready chapter](../chapters/02_GetReady4course.md) to know more about this.
>
> <i class="fa fa-arrow-right"></i> **Learning Outcomes (LO's):**  
> 
> <svg xmlns="http://www.w3.org/2000/svg" height="14" width="16" viewBox="0 0 576 512"><!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2023 Fonticons, Inc.--><path d="M384 64c0-17.7 14.3-32 32-32H544c17.7 0 32 14.3 32 32s-14.3 32-32 32H448v96c0 17.7-14.3 32-32 32H320v96c0 17.7-14.3 32-32 32H192v96c0 17.7-14.3 32-32 32H32c-17.7 0-32-14.3-32-32s14.3-32 32-32h96V320c0-17.7 14.3-32 32-32h96V192c0-17.7 14.3-32 32-32h96V64z"/></svg> **Level:** Beginner   
> 
> **By the end of the course, learners will be able to:**
>
>> - **General LO's**
>> 
>> 1. Describe differences and similarities among HPC Tiers and usage.
>>
>> 2. Access existing HPC infrastructures in Flanders such as VSC and VIB Data Core
>>
>> 3. Use the different environments in the HPC (storage, analysis, debug)
>>
>> 4. Querying and using modules and its versions in the HPC
>>
>> 5. Submit jobs to use softwares and scripts on the cluster 
>>
>> 6. Check information about submitted jobs
>
>**Target Audience:** Scientific staff, trainers, training providers, anyone that wishes to use HPC instances
>
>
> <i class="fa fa-hourglass"></i> **Time estimation General session**: 1/2 day 
>
> <i c
<i class="fa fa-lock"></i> **License:** 

<img src="https://raw.githubusercontent.com/vibbits/rdm-course-2022/main/images/logos/CC-by.png" title="" alt="" width="143">

[**Creative Commons Attribution 4.0 International  License**](https://creativecommons.org/licenses/by/4.0/)

<i class="fa fa-money-bill"></i> **Funding:**  

<i class="fa fa-life-ring"></i> **Acknowledgement**: 

 * [ELIXIR Belgium](https://www.elixir-belgium.org/)
 * [VIB Technologies](https://www.vib.be/)
 * [VIB Training & Conferences](https://www.vibtrainingandconferences.be/#/)

<i class="fa fa-anchor"></i> **PURL**: to be added 

### Authors

| | | |
|---|---|---| 
| [![ORCID](https://raw.githubusercontent.com/vibbits/rdm-introductory-course/main/images/logos/32px-ORCID_iD.svg.png)](https://orcid.org/0000-0001-6691-4233)Alexander Botzki | [![ORCID](https://raw.githubusercontent.com/vibbits/rdm-introductory-course/main/images/logos/32px-ORCID_iD.svg.png)](https://orcid.org/0000-0000-0000-0000)Benjamin Pavie | [![ORCID](https://raw.githubusercontent.com/vibbits/rdm-introductory-course/main/images/logos/32px-ORCID_iD.svg.png)](https://orcid.org/0000-0000-0000-0000)Sebastian Munck |
| [![ORCID](https://raw.githubusercontent.com/vibbits/rdm-introductory-course/main/images/logos/32px-ORCID_iD.svg.png)](https://orcid.org/0000-0000-0000-0000)Tatiana Woller | [![ORCID](https://raw.githubusercontent.com/vibbits/rdm-introductory-course/main/images/logos/32px-ORCID_iD.svg.png)](https://orcid.org/0000-0001-5958-0669)Bruna Piereck | [![ORCID](https://raw.githubusercontent.com/vibbits/rdm-introductory-course/main/images/logos/32px-ORCID_iD.svg.png)](https://orcid.org/0000-0000-0000-0000)Janick Mathijs |

### Contributors

Part of this training was reused from the ["HPC training Bio-imaging"](https://liascript.github.io/course/?https://raw.githubusercontent.com/vib-bic-training/HPC_training_bioimaging_1/refs/heads/main/README.md#1)

### Citing this lesson

Please cite as:

> Session under development

  1. ....

## Schedule

Half day Schedule:

- 13:00 - 13:30 - Introduction
- 13:30 - 15:00 - Accessing in the terminal and OnDemand
- 15:00 - 15:15 - Coffee Break
- 15:15 - 16:00 - Interactive sessions (debug and testing)
- 16:00 - 16:30 - Querying and using modules in the HPC
- 16:30 - 17:00 - Submitting and managing jobs

</section>
