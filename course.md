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

<!-- GENERATED FILE - DO NOT EDIT.
     Built by .github/scripts/build_course.py from README.md and docs/chapters/*.md.
     Edit those files instead; this one is regenerated on every push to main. -->

# High Performance Computing: structure and practice

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
> <i class="fa fa-asterisk"></i> **Requirements:** The (technical) installation requirements are described in the chapter [Get ready](#get-ready-for-the-course-instalation-and-accounts)
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
> <i class="fa fa-anchor"></i> **PURL**:  [<img src="https://zenodo.org/badge/DOI/10.5281/zenodo.21919181.svg" width="200"/>](https://zenodo.org/records/21919181)
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
> Piereck Moura, B., Mathys, J.& Depoortere, B. (2026). High Performance Computing: structure and practice essentials (Version V2026.05.07) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.21919181
>
> # Chapters List
> 
> | Chapter | Title |
> | :---    | :---  |
> |1        |[Get ready for the course, instalation and accounts](#get-ready-for-the-course-instalation-and-accounts)|
> |2        |[HPC Infrastructure](#hpc-infrastructure)|
> |3        |[Connecting to HPCs](#connecting-to-hpcs)|
> |4        |[VIB Data Core Compute](#vib-data-core-compute)|
> |5        |[Transferring Data](#transferring-data)|
> |6        |[Software on HPCs](#software-on-hpcs)|
> |7        |[Jupyter Notebooks](#jupyter-notebooks)|

# Get ready for the course, instalation and accounts

## Installations

Please read this page carefully **before** the start of the workshop.

In this session you will find what you need to install in your computer additionally to complementary training material to be completed prior to course.

<img src="images/website-setup-concept-landing-page/3012965.jpg" alt="set up" width="300"/>

[Image](https://www.freepik.com/free-vector/website-setup-concept-landing-page_5823714.htm#fromView=search&page=1&position=3&uuid=8e36a5ee-39d5-4073-bfcc-47f4c8a009c0&query=intallation+computer) designed by [Freepik](https://www.freepik.com/)

### 1. You must have Unix command line experience

If you don't have experience or need to refresh your memory, please check our online, self-paced [Introduction to Linux Command Line](https://elearning.vib.be/courses/linux/) course

Some students have reported around 4h of investment in this material, but take your time to get comfortable with the concepts and commands. Think of the folder structure and how to navigate in the computer within a terminal.

<img src="images/laptop-with-program-code-isometric-icon-software-development-programming-applications-dark-neon/971.jpg" alt="programming" width="300"/>

[Image](https://www.freepik.com/free-vector/laptop-with-program-code-isometric-icon-software-development-programming-applications-dark-neon_4102879.htm#fromView=search&page=1&position=0&uuid=d5d9c586-a6c9-4476-97a9-ff0ca4dc781d&query=linux) designed by [Fullvector](https://www.freepik.com/author/fullvector) at [Freepik](https://www.freepik.com/)

### 2. Get access to an HPC

Request access to one of the two HPC options in preparation of the course since it might take some time to process and activate. 

#### Flemish Supercomputer (VSC)

##### a. Register for an [HPC account](https://docs.vscentrum.be/access/vsc_account.html) 

>
> P.s.: If you are from industry or in any other situation where you are not linked to an academic institution we can only help you get an account when registered in the workshop, check availability in [the website](https://www.vibtrainingandconferences.be/#/).
>
> In that case the trainer needs to request a temporary account for you to participate in the training activities.
>

Once you have an account, you can [access it](https://account.vscentrum.be/), and you will be able to see your VSC ID, and other information about your account. Eventually you might want to add an SSH key to connect remotely. You will not need this for this session.

##### b. Test your account:

**connecting at UGent instance of VSC**

Visit [login page](https://login.hpc.ugent.be) , the 1st time you do it permission will be requested to let the web portal access some of your personal information, authorize it!!  Once logged in, you should see this start page!

<center><img src="images/permission_VSC.png" width="300"/></center>

Once you are logged in, you should see this page:

<center><img src="images/login_ugentvsc.png" width="300"/></center>

All good, you can get started!

**connecting at KULeuven instance of VSC**

Visit [login page](https://auth.vscentrum.be/auth/login)  the 1st time you do it permission will be requested to let the web portal access some of your personal information, authorize it!!  Once logged in, you should see this start page!

<center><img src="images/permission_VSC.png" width="300"/></center>

Once you are logged in, you should see this page:

<center><img src="images/KULeuven_ondemand.png" width="300"/></center>

All good, you can get started!

#### VIB Data Core Compute Cluster

Researchers from VIB (and therefore have a `@vib` email address) can follow this course using the VIB Data Core Compute Cluster. 


##### a. Request an account 

If you don't have an account yet, make sure to fill in [this form](https://connect.vib.be/services/command-line-analysis) in advance. See [the page on the Compute Cluster](#vib-data-core-compute) for more details.

##### b. Test your account:

**Connecting to the Compute Cluster**

- To test your command line access, see https://docs.datacore.vib.be/compute-cluster/entrypoints/command-line-access#connect-with-ssh
- To test your access to the web interface of Compute (Open OnDemand), see https://docs.datacore.vib.be/compute-cluster/entrypoints/open-on-demand/

# HPC Infrastructure

## What is a High-Performance Computing system ?

A HPC brings together several technologies such as computer architecture, algorithms, programs and electronics, and system software to solve advanced problems effectively and quickly. A HPC uses clusters of powerful processors, working in parallel, to process massive multi-dimensional datasets (big data) and solve complex problems at extremely high speeds. HPC systems typically perform at speeds more than one million times faster than the fastest commodity desktop, laptop or server systems. [https://www.ibm.com/topics/hpc].

Among the technologies integrated in a HPC system it can include

**High-end compute nodes:** multicore processors.

**Fast interconnect:** multiple processor cores work together through parallel processing. Fast connections between the nodes are necessary to make quick data exchange possible.

**Parallel shared filesystem:** the compute nodes are connected to a shared filesystem for storing input data, temporary data, and final calculation results.

**High-memory nodes:** some nodes are equipped with lots of RAM memory, mitigating low disk reads impacting analysis that generate large amounts of intermediary results.

**GPU (Graphical processing units) nodes:** are specialized processors, ideally suited for highly demanding data processing tasks.


## Infrastructure

The european model for HPC classifies that different offers in HPC resource and accessibility in different levels called **Tiers**.

_ 

<img src="images/tierEuropeanHPCsytem.svg" width="500"/>

_ 

* **Tier-0** clusters are ***Very large*** computing infrastructure available at EU level, for example [PRACE association](https://prace-ri.eu/prace-association/) (Partnership for advanced computing in Europe) has [6 partners](https://prace-ri.eu/prace-archive/infrastructure-support/prace-hpc-infrastructure/) offering a Tier-0 cluster. Belgium is not hosting a Tier-0 but is one of ~25 member in PRACE.

* **Tier-1** clusters are clusters with services at the level of a region/country because it exceeds the capacity of an institution in terms of needs/costs. For example in the [VSC (Vlaams Supercomputer Centrum)](https://www.vscentrum.be/compute) there is [Hortense](https://www.vscentrum.be/compute), the Tier-1 computer cluster hosted by UGent university 

* **Tier-2** clusters are available at research institutions level. There are [4 Tier-2 cluster in Flandres](https://docs.vscentrum.be/hardware-tier2.html#), hosted by the universities UAntwerp, VUB, UGent and KULeuven.

* **Tier-3** is representing your personal computer, can be a desktop or a laptop. But is mainly for personal use and has limited resources.

* In **VIB** such HPC system is offered by [Data Core](https://datacore.sites.vib.be/en) as a centralized Compute solution. The VIB Data Core Compute Cluster is a cluster of computers that provides multicore processor nodes grouped in debug, high memory (CPU) and GPU partitions in order to achieve high performance computing. This service is offered only to VIB members.


>> _
>>
>> In this course we will detail more the resources of UGent, KULeuven and VIB instances.
>>
>> However all along we will try to explain the building blocks allowing you easily understand and adapt to other HPC instances.
>>
>> _

### Storage and Computer Nodes systems

A HPC needs different types of storage to maintain the efficiency of its vast and complex infrastructure. Each instance will possibly name them differently, but they have defined purposes that you need to take in account when using their environment. On top of the filesystem, each node will have different computational powers, therefore, depending on your needs, you can choose the one that most suits you.

It means that the files and storage systems in place **will vary**. Knowing this what storages, their purpose and maintenance will be important to understand ***how*** and ***where*** to keep, analyze and backup your data. Additionally, as you probably already guessed, there is a difference if we are talking about personal use and project wise. Specific projects might request specific resources and will define who can access it.

Generally is good to keep in mind that when you connect to the HPC, the area you start at is like the hall of a house, you should not keep too many things there or do tasks in this location. You will also have a long-term storage, where you can keep your data, but also not where your tasks will be done. Last you will have a temporary large storage place that can be access when using your tasks


<!-- style="color: #7CA1CC;" --> \** Storage space for a group of users (Virtual Organization or VO for short) in VSC can be increased significantly on request, check for [more information](https://docs.vscentrum.be/gent/tier1_hortense.html#system-specific-aspects) if you need.


#### VIB Data Core Compute Cluster 

Learn about Compute's hardware here: https://docs.datacore.vib.be/compute-cluster/#hardware

#### UGent instances of the VSC


Tier-1 instance of UGent
-------------------------

You can find more details about the Tier1 of the [VCS ](https://www.vscentrum.be/), but we try to summarize some aspects here. Keep in mind that most updated information will be found in the links. In the Tier-1 instance, additionally to the nodes listed bellow you can request 2 other nodes that are a combination for high demand analysis; **(1)** `cpu_rome_all` corresponds to a combination of `cpu_rome` and `cpu_rome_512`; **(2)** `gpu_rome_a100_all` corresponds to a combination of `gpu_rome_a100_40` and `gpu_rome_a100_80`.

| Cluster name  | Memory (GiB) | Disk space (GB) SSD  |  GPU | GPU memory (GiB)|
|---|---|---|---|---|
| cpu_rome | 256 | 480 | - | - |
| cpu_rome_512| 512 | 480 | - | - |
| cpu_milan | 256 |480| - | - |
| gpu_rome_a100_40| 256 | 480 | 4 NVIDIA A100  | 40 |
| gpu_rome_a100_80 | 512 | 480 | 4 NVIDIA A100  | 80 |
| debug_rome ** | 256| 100 | 1 NVIDIA Quadro P1000 | 4|

for more information in different partitions: [vscentrum.be general-information](https://docs.vscentrum.be/en/latest/gent/tier1_hortense.html#general-information)

At the UGent system you will have 4 storages with different purposes


| Filesystem name  | Intended usage | Personal storage space | VO storage space **|
| ------------- | ------------- | ------------- | ------------- |
| $VSC_HOME | Home directory | 3GB (fixed) | :x: |
| $VSC_SCRATCH | Entry point to the system |  3GB (fixed) | :x: |
| $VSC_DATA | Long-term storage of large data files |  Depend of you account(Leuven/Gent, see above) | :x: |
| $VSC_SCRATCH_PROJECTS_BASE/2024_300/| Temporary fast storage of ‘live’ data for calculations |  20TB | upon request |

Tier-2 instance of UGent 
-------------------------

You can find more details about the [UGent instance](https://docs.vscentrum.be/gent/tier2_hardware.html) but we try to summarize some aspects here. Keep in mind that most updated information will be found in the links. 

These are the nodes available at Tier-2 UGent and you can see they will vary in memory, disk space and if they have or not GPUs. I want you to pay special attention to [**donphan**](https://docs.hpc.ugent.be/Linux/interactive_debug/), this is the debug and testing node, is also the one using during training sessions.


| Cluster name  | Memory (GiB) | Disk space  |  GPU |
|---|---|---|---|
| swalot | 116 | 1 TB | - |
| skitty | 177 | 1 TB + 240 GB SSD | - |
| victini | 88 | 1 TB + 240 GB SSD | - |
| joltik | 256 | 800 GB SSD | 4 NVIDIA V100 |
| doduo | 250 | 180 GB SSD | - |
| accelgor | 500 | 180 GB SSD | 4 NVIDIA A100 |
| donphan ** | 738 | 1.6 TB NVME | 1 shared NVIDIA Ampere A2 |
| gallade | 940 | 1.5 TB NVME | - |

Filesystems specifics
---------------------------

| Filesystem name  | Intended usage | Total storage space | Personal storage space | VO storage space (*)|
| ------------- | ------------- | ------------- | ------------- | ------------- |
| $VSC_HOME | Home directory, entry point to the system | 51 TB | 3GB (fixed) | :x: |
| $VSC_DATA | Long-term storage of large data files | 1.8 PB | 25GB (fixed) | 250GB |
| $VSC_SCRATCH | Temporary fast storage of ‘live’ data for calculations | 1.9 PB | 25GB (fixed) | 250GB |
| $VSC\_SCRATCH\_ARCANINE | Temporary very fast storage of ‘live’ data for calculations (recommended for very I/O-intensive jobs) | 70 TB  | (none) | upon request |
(*) Storage space for a group of users (Virtual Organization or VO for short) can be increased significantly on request.

Source : https://docs.vscentrum.be/en/latest/gent/tier2_hardware.html?highlight=VSC_DATA#shared-storage

#### KULeuven section of the VSC

If you need to use the KULeuven instance of the [VSC](https://www.vscentrum.be/), it's most likely need to be part of a group which has credits to use the resources. If it is part of a training they need to include you in their list, in this case you use training credits and has priorities in the reserved cluster. 

As you already could see for the previous instances, each has different resources, for this case is not different, they have a file system and each of the two instances will have different resources.

Filesystems specifics

| Filesystem name  | Intended usage | Total storage space | Personal storage space | VO storage space (*)|
| ------------- | ------------- | ------------- | ------------- | ------------- |
| $VSC_HOME | Home directory, entry point to the system | ? | 3GB (fixed) | :x: |
| $VSC_DATA | Long-term storage of large data files | ? | 75GB (fixed) | :x: |
| $VSC_SCRATCH | Temporary fast storage of ‘live’ data for calculations | ? | 500GB | ? |

Projects and reservation for Tier-2 KU Leuven

Running calculations on Tier-2 KU Leuven requires credits. New users obtained 2 millions free credits (introduction) that are valid during 6 months.
Credits can be obtained through various type of research projects (through university, FWO, EU level). Subset of Tier-2 KUL can be reserved for research events or training events.


Tier 2 KULeuven - Genius
------------------------

| Cluster name | Memory (GiB) | Disk space  | GPU | GPU memory (GiB)|
|---|---|---|---|---|
| batch/batch_long | 192 | 200 GB SSD | - | -|
| interactive | 192 | 200 GB SSD | - | -|
| bigmem| 768 | 200 GB SSD | - | - |
| gpu_p100 | 192 | 200 GB SSD | 4 NVIDIA P100 |16|
| GPU_v100 | 768 | 200 GB SSD | 8 NVIDIA V100 | 32|
|amd| 256 | 200 GB SSD | - |-|

Tier 2 KULeuven - wICE
-------------------

| Cluster name | Memory (GiB) | Disk space  | GPU | GPU memory (GiB)|
|---|---|---|---|---|
| batch/batch_long | 256 | 960 GB SSD | - | -|
| batch_sapphirerapids/batch_sapphirerapids_long| 256 | 960 GB SSD | - | -|
| bigmem | 256 | 2048 GB SSD | - | - |
| hugemem | 960 | 8000 GB SSD | - | -|
| gpu | 512| 960 GB SSD | 4 NVIDIA A100 SXM4 | 80 |
| gpu_h100 | 768 | 960 GB SSD | 4 NVIDIA H100 | 80|
| interactive and gpu_a100_debug | 512| 960 GB SSD | 1 NVIDIA A100 | 80 |

> Source : https://docs.vscentrum.be/en/latest/leuven/tier2_hardware/kuleuven_storage.html?highlight=VSC_DATA#ku-leuven-storage

### Summary

With this overview you should be able to observe that every HPC instance will need a file system that should have at least 3 main locations

1. The entrypoint for you to communicate to the larger part of the system
2. A long term storage where most of the data should be kept
3. A low term temporary storage with more space to keep temporary files and outputs of your analysis but needs frequent back up in order not to loose your data.

In some cases other spaces are reserved for more intense analysis for example.

You should also observe that all resources will have different nodes that will differ in memory, disk space, etc. This might be challenging at first to know what to choose, but with time you will learn how much resource each analysis takes depending on the tools, input and output that will be linked to this. Optimizing your analysis to the correct resources will make your use more efficient and the whole community will benefit from this good practice.

It is important to remember that the access to different resources will vary, for some you will have to buy credits and pay for the storage. For others the access is granted based in other parameters. Always check beforehand what is needed so you take the best approach.

# Connecting to HPCs

## Request an account

You can see how to request a VSC account in [chapter02](#a-register-for-an-hpc-account).

To request an account at VIB, checkout [the following section in chapter02](#a-request-an-account).

## Connecting to use HPC services

You have different ways to connect and access the resources of the HPC. You can use your browser and connect using OnDemand or you connect from your local computer using SSH key credentials. We will see how to use both.

The OnDemand service allows a friendly interface to be used in your browser. It is specially interesting if you need to have images, visuals or wants to use Jupyter.  As you can already guess, not every instance offers the same service, so you need to check if the instance you are connecting to has what you are expecting to use.

For the case of using OnDemand you don't need an SSH-key, however to access from your computer terminal you will need to create an SSH-key, which works as an address to your computer, allowing the communication with remote machines. It is essential that you remember this is an address that gives access to you computer, so when you do think of a good password. I'll give you more details in the specific session.

### Connect with Open OnDemand

Once you are logged in on one of the HPC instances using OnDemand you can find a list of interactive apps that can include Jupyter notebook, RStudio, VSCode Tunnel among others. 

<center><img src="images/KULeuven_ondemand.png" width="500"/></center>

You will also find a shortcut for their terminal cluster. You can open the terminal in your home directory (also known as `$HOME` or `~`) or request an interactive session in one specific node that contains the resources you need. Before we get into this level, let's see how we can connect to OnDemand.

* VIB Data Core Compute Cluster: https://compute.vib.be/

* UGent Tier-1: https://tier1.hpc.ugent.be/ 

* UGent Tier-2: https://login.hpc.ugent.be

* KULeuven Tier-2: https://ondemand.hpc.kuleuven.be/ 

Each link will take you to enter with the account you registered with and will follow the procedures described in chapter02: [Get Ready for the course](#get-ready-for-the-course-instalation-and-accounts).

Once you are connected you will find the menu bar on top where you have **Interactive APPs** and you can check what each instance has to offer. See for example in UGent Tier-2:

<center><img src="images/UGent-tier2-interactiveapps.png" width="500"/></center>

Print from march-2025.

Once you choose the app you will need to define the resources you need. You can do that by informing the Cluster name, to be sure you should check the documentation since the summary in chapter03: [Infrastructure](#hpc-infrastructure) could be outdated. You also have to define for how many hours, cores and memory you need for this session.

<center><img src="images/UGent-tier2-resources-request.png" width="500"/></center>

Print from march-2025.

When you do so, there is a high chance that you will go into a waiting line. The resources are not always immediately available. Despite of sometimes having the feeling that it is an infinite resource, it could have a high demand. 

The more resources you request, the longer is the waiting time usually, also if you request very often you could lose some priority. Thus, be mindful.

If you are in a training session ask your trainer what resources you need to request and if there is a priority list for the course. In the case of a priority list, the trainer will share a priority code that you will include in the specs so your waiting time is smaller.

If you go to **My interactive sessions** in the menu bar you will be redirect to a page with the list of resources and will follow the same step-by-step procedure.

>
> For this session, let's connect with VSCode
> Activity:
>
>

### Connect with a Terminal

To work from the terminal the first thing you are going to need is to create an authenticated connection between your machine and the HPC. Yes! We are talking about the SSH-key. As I said before the SSH-key is like an address that will allow communication between your computer and the computer cluster.

That is important to keep in mind due some implications, first of all for this to be a safe connection you will create a strong password when you are asked during the procedure. Second, it means sharing this key, you will generate two keys and you can only share the public key, that is the one meant for sharing. Third, this means for each computer you will have a different one; So, if you are using your working computer and your personal computer it means following the steps in each of them.

How you can generate this key is a bit different for each operational system. Check which one you need.

### Create SSH key

On Windows
-------------------------------

For Windows system you have two ways to do it.

1. Using [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) app. And for all details please [check on VSC](https://docs.vscentrum.be/access/generating_keys_with_putty.html#generating-keys-putty) and how they advise you to do it.


#### Putty setting
![vsc_ssh_putty_config_01](https://user-images.githubusercontent.com/1775952/232025747-8494a5f8-77cd-4d26-a493-c11bab897c0c.png)

![vsc_ssh_putty_config_02](https://user-images.githubusercontent.com/1775952/232025825-3fb4ac9c-8394-4c5c-90c0-aad6c30de7c6.png)


On MAC and Linux, using OpenSSH
-------------------------------
 
 First check if you already have a key

 ```
 $ ls ~/.ssh
 authorized_keys   id_rsa   id_rsa.pub   known_hosts
 ```

If you have one, like in the example above you can share you SSH-key with VSC. If you don't have then you need to follow the steps:

```
$ ssh-keygen -t rsa -b 4096
Generating public/private rsa key pair.
```

Don't change the name of the file that is being created, but make sure to have a strong password. You will not see any symbols while typing the password! But this is standard behavior of unix systems to protect you from people even knowing how many characters there are in your password. Trust the process and repeat the same password twice

```
Enter file in which to save the key (/home/bruna/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again:
```

Check again and you should see one `id_rsa` and one `id_rsa.pub`, the second one is your **pub**lic key. That is the one you need to share with VSC or VIB clusters.

you can print then so you can copy-past

```
$ cat ~/.ssh/id_rsa.pub
ssh-rsa AA...........................
.....................................
.....................................
.....................................
....................bruna@DESKTOP....
```

You will see something like this. Starting with ssh-rsa followed by several characters that were **replaced** by points, and the name of your computer. If you see in the first line `--BEGIN OPENSSH PRIVATE KEY--`, go back! This file data should **NOT** be shared. 

if you want more details check the [VSC documentation](https://docs.vscentrum.be/access/generating_keys_with_openssh.html#generating-keys-linux)

### Share the SSH public key 

Different HPC center around the globe might give you different directions. It could be done on the command line or by sharing in a centralized page or using apps as PuTTY. 

This bit is important because it is used for authorization and giving directions so communication can be established to the remote connection.

VIB procedure
-------------------------
The VIB Single Sign-on (SSO) is leveraged through a program called Smallstep. Installation procedures can be found in [the Data Core documentation](https://docs.datacore.vib.be/compute-cluster/entrypoints/command-line-access/#installing-smallstep). 

VSC procedure
-------------------------

For all instances of VSC you have a centralized control. That means that once you have done it for VSC you can use the same credentials and same account to connect to Tier-1 and Tier-2 of UGent, KULeuven and others.

So far you have created an account, you have created the SSH-key, now you need to access the [vsc account webpage](https://account.vscentrum.be/), you will find a top bar menu. 

<center><img src="images/VSC_accountWebpage.png" width="500"/></center>

Print from march-2025.

If you go to the tab **Edit Account** and scroll down, you will find the option **Add public key**

![vsc_add_ssh_pub_key](https://user-images.githubusercontent.com/1775952/232023753-4b172e36-58ea-4aa6-bef8-94178406d31d.png)

In the **View Account** tab you will find information about your account, among these you will know your VSC-Uid that has a format as **vsc00000**, you might be requested to share this ID in order to be added to a project or priority list of a training session. You will also find the path to your `$HOME`, `$DATA` and `$SCRATCH` directory that is linked to your institution, in my case is UGent.

**Home directory: /user/gent/000/vsc00000**
**Data directory: /data/gent/000/vsc00000**
**Scratch directory: /scratch/gent/000/vsc00000**

# VIB Data Core Compute

## VIB Data Core Compute Cluster

### Request a Compute Account 
- Through Connect: https://connect.vib.be/services/command-line-analysis

Two main entrypoints to interact with the Compute Cluster:

- Command line access through SSH
- Browser via Open OnDemand

Relevant Data Core documentation: https://docs.datacore.vib.be/compute-cluster/entrypoints/

### Connect to Compute via SSH

Follow the guide that fits your Operating System from: https://docs.datacore.vib.be/compute-cluster/entrypoints/command-line-access#connect-with-ssh. It walks you through the installation of [Smallstep](https://docs.datacore.vib.be/compute-cluster/entrypoints/command-line-access#installing-smallstep) which leverages the VIB Single-Sign On (SSO) to securely connect you to Compute. Depending on your workstation, its operating system and by who it is managed, **you might need admin privileges in order to install the step command**, so permission might be required by your local IT helpdesk.

#### Login

```sh
ssh -p2022 firstname.lastname@compute.vib.be
```

As your home folder is limited in capacity, as it is meant for configuration files and not for any type of analysis data, you should work in your group or project folder. This is the performant storage option Compute Storage provided by Data Core, where the following documentation entry shows you how to identify yours and how much storage they have: https://docs.datacore.vib.be/data-storage/compute-storage/#directory-structure. For more information on data organization on Compute, see https://docs.datacore.vib.be/compute-cluster/data-organization.


### Connect to Compute via the web browser (Open OnDemand)
- Link to VIB Compute's Open OnDemand: https://compute.vib.be, where you can log in with your @vib.be email using the VIB SSO.

### Request a Secure Compute Account
If you are working with **GDPR Sensitive Data**, you should work on the VIB Data Core Secure Compute. Access should be requested by the Group Leader and can be done via the same VIB Connect link found at the top of this page.

# Transferring Data

### Data transfer

There are different ways to transfer data in and out of the Cluster. But the safest way to transfer big chunks of data is using Globus.
​Globus is a research cyberinfrastructure, developed and operated as a not-for-profit service by the University of Chicago.
Globus enables to transfer, share and back-up data regardless of its size and its location 
(i.e. from a supercomputer, drive, laptop, cloud and machines such as a microscope).
In addition, several repositories such as EMPIAR or Bioimage archive are using or implementing Globus for data deposition/transfer
Data transfers through Globus can be executed through a web interface or through commandline, with and without human interaction.
There is a general session and one session approaching some specifics for Bioimaging.

#### Globus setup 


Authentication
----------------------

**$\textcolor{red}{\textsf{Warning}}$** : via the web interface, you can only download one file at a time, see [VSC & Globus](https://docs.vscentrum.be/en/latest/globus/using_globus_via_web.html)

1. Browse to the [Globus](https://www.globus.org/) website.
2. Go to Log in (right upper corner)
3. Select your organization e.g. KU Leuven association/ UGent/ UAntwerp /VIB and click on Continue
4. Follow KU Leuven login procedure via the KU Leuven Authenticator e.g. Scan QR
5. Accept Information to be Provided to Service (always or one time only) and click on Accept
6. Globus App File Manager will be displayed in the browser tab.

Installation Globus Connect Personal
--------------------------------------------------------------

1. Download Globus Connect Personal on your computer:
  - Windows:  https://docs.globus.org/globus-connect-personal/install/windows/ 
  - MacOS: https://docs.globus.org/globus-connect-personal/install/mac/
  - Linux: https://docs.globus.org/globus-connect-personal/install/linux
2. Install Globus Connect Personal in a folder where you have administrator rights (for KUL in My_Programs or My_Downloads) when the VPN is off.
3. Authenticate


.... 

#####  Transferring to active storage (VSC)

<!-- style="color: magenta ;" --> Intro or image to be added

###### From your computer to active storage (VSC)

1. After authentication, Globus App File Manager will be displayed in the browser tab.
2. Follow Globus file transfer [tutorial](https://vlaams-supercomputing-centrum-vscdocumentation.readthedocs-hosted.com/en/latest/globus/managing_and_transferring_files.html#globus-collections-and-endpoints)
3. Use **VSC UGent Tier1 projects** as endpoint and the exact name of the project is "2024_300"

![image](https://user-images.githubusercontent.com/1775952/213488568-e32e144b-d017-4996-85c8-aa82b1266340.png)
  <img width="1216" alt="image" src="https://github.com/vib-bic-training/HPC_training_bioimaging_1/assets/103046100/f2e2734d-400f-4f23-8bfc-bf907071351d">


 You may authorize the access the first time you login:
 
![image](https://user-images.githubusercontent.com/1775952/213488674-06a2dc3c-664a-409a-bef7-acbbbef2dd43.png)
![image](https://user-images.githubusercontent.com/1775952/213488742-1326bace-f6cb-4f63-9de2-2dcb06d4ae73.png)
![image](https://user-images.githubusercontent.com/1775952/213488873-53e05bd1-5cba-48e8-98f4-9eb2cf81fd74.png)

4. Guidelines for where to store your data are explained [here](https://vlaams-supercomputing-centrum-vscdocumentation.readthedocs-hosted.com/en/latest/access/where_can_i_store_what_kind_of_data.html).

5. You can store data at different places, for example:
- low memory storage backed-up (<3 GB) /dodrio/scratch/users/$VSC_NUMBER/Desktop (= $VSC_SCRATCH/Desktop)
- low memory storage backed-up (<3 GB) /dodrio/scratch/users/$VSC_NUMBER/Ondemand (= $VSC_SCRATCH/Ondemand)
- your own data folder from your institution (=$VSC_DATA)
- active storage that is not backed-up:  /dodrio/scratch/project/starting_2024_300/username (= $VSC_SCRATCH_PROJECTS_BASE/2024_300/username)
- backed-up data: /vsc/home/t1_col_2024_01 (Tier 1 data)

![image](https://user-images.githubusercontent.com/1775952/213489574-493782a0-724e-4c2c-9d44-97b6e20d3f62.png)
<img width="1215" alt="image" src="https://github.com/vib-bic-training/HPC_training_bioimaging_1/assets/103046100/00f6a18e-d8b8-482a-8fbd-a4c860a77c42">

These folders are accessible via the File Manager in the Bioimage ANalysis Desktop:

![image](https://user-images.githubusercontent.com/1775952/213487170-89eafc68-9b07-42c1-9cc8-1be64b5e1660.png)

6. Checking your disk usage is explained here: https://vlaams-supercomputing-centrum-vscdocumentation.readthedocs-hosted.com/en/latest/access/managing_disk_usage.html

7. Other endpoints:
- `VSC KU Leuven tier2 scratch (Tier-2 KUL)`: /scratch/xxx/vscxxxyy
- `VSC UGENT Tier2 filesystem (Tier-2 UGent)`: /scratch/gent
- `KU Leuven L drive (LUNA)`
- `KU Leuven OneDrive`
- `VIB shared files`
- `EMPIAR`
- `BioImage archive`
---------------------------------------------------

### Research data management
#### ManGO
ManGO is developed by KU Leuven as a middleware on the top of iRODS (an open source data management software). 
ManGO is data agnostic and used in different fields (exact science, life science, humanities) and implemented on VSC, University of Wageningen and National Cancer institute in the Netherlands.
Thanks to ManGO, the metadata can be extracted automatically through workflows, the metadata can be added through schema and archived with ease.  
#### DataHub
Solution provided by ELIXIR and VIB Data Core (for more info, contact Data Core)
#### GitHub
Code should shared on GitHub (Bic code, Bic training and ...)

<!-- style="color: magenta ;" --> 

##  NEW ADDS MERGING FILES NEED TO BE CHECKED

### Steps

**$\textcolor{red}{\textsf{Warning}}$** : via the web interface, you can only download one file at a time, see [VSC & Globus](https://docs.vscentrum.be/en/latest/globus/using_globus_via_web.html)

1. Browse to the [Globus](https://www.globus.org/) website.
2. Go to Log in (right upper corner)
3. Select your organization e.g. KU Leuven association and click on Continue
4. Follow KU Leuven login procedure via the KU Leuven Authenticator e.g. Scan QR
5. Accept Information to be Provided to Service (always or one time only) and click on Accept
6. Globus App File Manager will be displayed in the browser tab.
7. Follow Globus file transfer [tutorial](https://vlaams-supercomputing-centrum-vscdocumentation.readthedocs-hosted.com/en/latest/globus/managing_and_transferring_files.html#globus-collections-and-endpoints)
8. Use **VSC UGent Tier1 projects** as endpoint and the exact name of the project is "starting_2023_001"

![image](https://user-images.githubusercontent.com/1775952/213488568-e32e144b-d017-4996-85c8-aa82b1266340.png)

 You may authorize the access the first time you login:
 
![image](https://user-images.githubusercontent.com/1775952/213488674-06a2dc3c-664a-409a-bef7-acbbbef2dd43.png)
![image](https://user-images.githubusercontent.com/1775952/213488742-1326bace-f6cb-4f63-9de2-2dcb06d4ae73.png)
![image](https://user-images.githubusercontent.com/1775952/213488873-53e05bd1-5cba-48e8-98f4-9eb2cf81fd74.png)

9. Guidelines for where to store your data are explained [here](https://vlaams-supercomputing-centrum-vscdocumentation.readthedocs-hosted.com/en/latest/access/where_can_i_store_what_kind_of_data.html).

10. You can store data at different places, for example:
- /dodrio/scratch/users/$VSC_NUMBER/Desktop (= $VSC_SCRATCH/Desktop)
- /dodrio/scratch/users/$VSC_NUMBER/ondemand (= $VSC_SCRATCH/ondemand)
- /dodrio/scratch/project/starting_2023_001 (= $VSC_SCRATCH_PROJECTS_BASE/starting_2023_001)

![image](https://user-images.githubusercontent.com/1775952/213489574-493782a0-724e-4c2c-9d44-97b6e20d3f62.png)

These folders are accessible via the File Manager in the Bioimage ANalysis Desktop:

![image](https://user-images.githubusercontent.com/1775952/213487170-89eafc68-9b07-42c1-9cc8-1be64b5e1660.png)

11. Checking your disk usage is explained here: https://vlaams-supercomputing-centrum-vscdocumentation.readthedocs-hosted.com/en/latest/access/managing_disk_usage.html

12. Other endpoints:
- VSC KU Leuven tier2 scratch (Tier-2 KUL): /scratch/xxx/vscxxxyy
- VSC UGENT Tier2 filesystem (Tier-2 UGent): /scratch/gent
- VIB Data Core Compute Storage for controlled access data, groups and projects, reference data
- VIB Data Core Project Storage

# Software on HPCs

## Software
The easiest way to use software on the VSC, is to use the pre-installed software, that is installed as an EasyBuild module.
Alternatively, you could create your own conda/mamba environment and use it in a python script or a jupyter notebook.
More advanced ways to use/run software are: 
- using singularity containers
- running Nextflow workflow
  
### CPU vs. GPU

Not all software are relying on GPU.
- CPU software: Fiji, QuPath
- GPU software: Cellpose, Omnipose, Napari and its plugins, Ilastik, ...

### Installed software

<!-- style="color: magenta ;" --> 
#### How to use a Easy Build module in command line (add a ! to use this command in a jupyter notebook)
- See loaded modules
```
ml
module list
```
- See available modules 
```
module avail
```
- Search for a module X
```
module av |& grep -i X
```
- Search for a module X and get details
```
module spider X
```
- Load a module X
```
module load x
```
- Unload a module X
```
module unload x
```
- Swap a module Y to X
```
module swap Y  X
```
- Remove all loaded modules except the cluster one
```
module purge
```
:warning: Do not load modules built with intel and foss toolchains

🗎 https://docs.vscentrum.be/software/software_stack.html#using-the-module-system

#### How to load module in jupyter notebook
Select the appropriate version of the jupyter notebook and load the easy build module accordingly

![image](https://github.com/vibbits/bioimaging-starting-grant/assets/103046100/70dfd6f5-becc-4fb5-9a8a-6b4274a54bad)

i.e. 6.4.0 GCC core 11.3.0 IPython 8.5.0 is compatible with foss-2022a or intel 2022a modules (see compatibility table below)
| FOSS  | GCC |  CUDA | OpenMPI | OpenBLAS | FFTW | ScaLAPACK |
| ------| --- | ----- | ------- | -------- | ---- | --------- |
| 2022b | 12.2.0 | 12.0.0 | 4.1.4 | 0.3.21 | 3.3.10 | 2.2.0-fb |
| 2022a | 11.3.0 | 11.7.0 | 4.1.4 | 0.3.20 | 3.3.10 | 2.2.0-fb |
| 2021b | 11.2.0 | - | 4.1.1 | 0.3.18 | 3.3.10 | 2.1.0-fb |
| 2021a | 10.3.0 | - | 4.1.1 | 0.3.15 | 3.3.9 | 2.1.0-fb |
| 2020b | 10.2.0 | - | 4.0.5 | 0.3.12 | 3.3.8 | 2.1.0 |
| 2020a | 9.3.0 | - | 4.0.3 | 0.3.9 | 3.3.8 | 2.1.9 |
| 2019b | 8.3.0 | - | 3.1.4 | 0.3.7 | 3.3.8 | 2.0.2 |

For more information about modules: https://hprc.tamu.edu/kb/Software/GNU-Compiler-Collection/ 

#### Compatibility python version - GCCcore on Tier-1 (Hortense)
 Table for jupyter notebook
 
| IPython version  | Python |GCCcore |
| ------------- | ------------- |-------------|
| 7.25.0-GCCcore-10.3.0 | Python 3.9.5 | GCCcore-10.3.0|
| 6.4.0-GCCcore-11.2.0  | Python 3.9.6 | GCCcore-11.2.0|
| 8.5.0-GCCcore-11.3.0 | Python 3.10.4 | GCCcore-11.3.0|
| 7.0.3 GCCcore 12.2.0 | Python 3.10.8 | GCCcore 12.2.0|
| 7.0.2 GCCcore 12.3.0 | Python 3.11.3 | GCCcore 12.3.0|


 How to see what is loaded with the module:
 ``` ml show  IPython/8.5.0-GCCcore-11.3.0 ```

#### Modules for bioimage analysis in python
1. [Napari](https://github.com/napari/napari): Napari/0.4.15-foss-2021b or Napari/0.4.18-foss-2022a
2. [Cellpose](https://github.com/MouseLand/cellpose): Cellpose/2.2.2-foss-2022a or Cellpose/2.2.2-foss-2022a-CUDA-11.7.0
3. Omnipose:  Omnipose/0.4.4-foss-2022a-CUDA-11.7.0 or  Omnipose/0.4.4-foss-2022a
4. [stardist](https://github.com/stardist/stardist): stardist/0.8.3-foss-2021b-CUDA-11.4.1 or stardist/0.8.3-foss-2021b
5. [AICSImageIO](https://github.com/AllenCellModeling/aicsimageio) : AICSImageIO/4.14.0-foss-2022a
6. [devbio-napari](https://github.com/haesleinhuepf/devbio-napari) : devbio-napari/0.10.1-foss-2022a-CUDA-11.7.0
7. [n2v](https://github.com/juglab/n2v) : n2v/0.3.2-foss-2022a-CUDA-11.7.0
8. Monai: MONAI/1.0.1-foss-2022a
9. QuPath: QuPath/0.5.0-GCCcore-12.3.0-Java-17

#### Module for spatial omics in python
1. [Scanpy](https://github.com/scverse/scanpy): scanpy/1.9.1-foss-2021b
2. Seurat: Seurat/4.3.0-foss-2021b-R-4.1.2
3. Squidpy: Squidpy/1.2.2-foss-2021b
4. [Giotto](https://drieslab.github.io/Giotto/): Giotto-Suite/3.0.1-foss-2022a-R-4.2.1

#### Module for bio-image analysis tools
1. Fiji: Fiji/2.9.0-Java-1.8
2. Cellprofiler: CellProfiler/4.2.4-foss-2021a

#### General libraries 
1. Scikit-learn: scikit-learn/1.1.2-foss-2022a or scikit-learn/1.0.1-foss-2021b
2. Scikit-image: scikit-image/0.19.3-foss-2022a or scikit-image/0.19.1-foss-2021b
3. scipy: SciPy-bundle/2022.05-foss-2022a, SciPy-bundle/2021.10-foss-2021b
4. seaborn: Seaborn/0.11.2-foss-2021b
5. tifftile: Scikit-image/0.19.1-foss-2021b 
6. tensorflow: TensorFlow/2.7.1-foss-2021b-CUDA-11.4.1 or TensorFlow/2.7.1-foss-2021b
7. R : R/4.2.1-foss-2022a or R/4.0.0-foss-2020a
8. R studio: RStudio-Server/1.3.959-foss-2020a-Java-11-R-4.0.0 
9. Jupyter notebook: JupyterLab/3.1.6-GCCcore-11.2.0
10. Matplotlib: matplotlib/3.5.2-foss-2022a or matplotlib/3.4.3-intel-2021b
11. Bioconductor:  R-bundle-Bioconductor/3.14-foss-2021b-R-4.1.2

### How to create your own conda or mamba environment

## Install miniconda    

- Connect to [Tier2 via ondemand](https://ondemand.hpc.kuleuven.be/) (or to [Tier2 Ghent](https://login.hpc.ugent.be/))
- Open an `Interactive Shell` 
  ![image](https://github.com/vibbits/reprohack_bioimaging/assets/1775952/270dfc7f-3cbf-4d4c-943f-fb276008e8c3)
- Go to the $VSC_DATA location and install miniconda
```
cd $VSC_DATA 
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p $VSC_DATA/miniconda3
```
-Make conda available to the path:
```
export PATH="${VSC_DATA}/miniconda3/bin:${PATH}"
```

## Install mambaforge
Mamba is a reimplementation of the Conda package manager in C++.
It allows parallel downloading of repository data and package files using multi-threading and use libsolv for much faster dependency solving
```bash
cd $VSC_DATA 
wget "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
bash Mambaforge-$(uname)-$(uname -m).sh
export PATH="${VSC_DATA}/mambaforge/bin:${PATH}"
```

## Create the conda environment
- Create the conda environment from the yaml file
```
conda env create -f cellpose-omnipose-gpu.yml
```
or
```
mamba env create -f cellpose-omnipose-gpu.yml
```
- Make it available for the jupyter notebook
```
source activate cellpose-omnipose-gpu
export PATH="${VSC_DATA}/miniconda3/bin:${PATH}
conda install ipykernel
python -m ipykernel install  --prefix=${VSC_HOME}/.local/ --name 'cellpose'
```
In this example, the conda environment will be accessible under the name `cellpose`

## Use the conda enviroment with a jupyter notebook

- After connecting to JupyterLab
![image](https://github.com/vibbits/reprohack_bioimaging/assets/1775952/8ee777a7-2498-43a7-ade6-c063ea96d4de)
- Create a new notebook `File > New > Notebook`
![image](https://github.com/vibbits/reprohack_bioimaging/assets/1775952/39470a8d-424f-4c79-a9f6-d2a7a3f59774)
- Select the newly create conda enviroment (e.g. here, `cellpose`)
![image](https://github.com/vibbits/reprohack_bioimaging/assets/1775952/4db7fde7-ff6e-4287-b17c-decc1a641525)
- Start to write the notebook

# Jupyter Notebooks

## Jupyter notebook

### How to start Jupyter notebook
Go to [the Open On Demand portal](https://tier1.hpc.ugent.be/) and log in after multifactor-authentification

Select **Jupyter notebook** or Jupyterlab (maybe more **Jupyter notebook** since you can modify the `Working Directory`) with the following specifications: 
![image](https://github.com/vib-bic-training/HPC_training_bioimaging_1/assets/103046100/2dd8d125-d679-4837-9798-07b78b2b0bbd)
![image](https://github.com/vib-bic-training/HPC_training_bioimaging_1/assets/103046100/31182681-1283-47ec-ad04-a43efffeb34a)



Required modules:
- `module load n2v/0.3.2-foss-2022a-CUDA-11.7.0`
- `module load matplotlib/3.5.2-foss-2022a`

### Get the notebook
The notebooks are located in https://github.com/vib-bic-training/HPC_training_bioimaging_1/tree/main/code/notebooks

Download both of them and upload them to your local storage on the VSC using the jupyter interface:
![Exclude labels on edge](images/jupyter/02_jupyter_notebooks.png)

Then double click on the notebook `n2v_demo_01_training.ipynb` to open it and edit it to change `output_folder`:
```python
output_folder = '/dodrio/scratch/projects/2024_300/<YOUR_NAME>/nv2' #TO CHANGE
```

> [!TIP]
> 
> you could select another place as a `Working Directory`, byt modifying the value when you configure the launch of the jupyter interface
>
> ![Jupyter Working Directory](images/jupyter/03_jupyter_notebooks.png)
> 

### Additional resources

#### Jupyter Notebook 
- Deep learning : https://github.com/HenriquesLab/ZeroCostDL4Mic 
- Pipeline: https://github.com/BiaPyX/BiaPy
​- Super-resolution imaging: https://github.com/HenriquesLab/NanoPyx 

#### Napari notebooks: ​
- https://github.com/BiAPoL/Bio-image_Analysis_with_Python
- https://biapol.github.io/PoL-BioImage-Analysis-TS-GPU-Accelerated-Image-Analysis/intro.html
- https://biapol.github.io/PoL-BioImage-Analysis-TS-Early-Career-Track/intro.html
- https://github.com/FrancisCrickInstitute/cbias-napari

##### BIC code
- notebooks: https://github.com/vib-bic-code/notebooks
- conda environment: https://github.com/vib-bic-code/conda_environments

#### Bioimage model zoo :​
- General one: ​ https://bioimage.io/#/​

# Workshop and Material organization

> We are using the interactive Open Educational Resource online/offline course infrastructure called LiaScript.
> It is a distributed way of creating and sharing educational content hosted on github.
> To see this material as an interactive LiaScript rendered version, with all chapters
> in the sidebar, click on the following link/badge:
>
> [![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://raw.githubusercontent.com/vib-training-conferences/introduction_2_HPC/main/course.md)
>
> LiaScript builds its chapter sidebar from the headings of a single document, and its
> `import:` directive only shares header definitions rather than content. The course is
> therefore assembled into [`course.md`](./course.md) by
> [`.github/scripts/build_course.py`](./.github/scripts/build_course.py), which runs
> automatically on every push to `main`.
>
> **Edit `README.md` and the files in `docs/chapters/`; never edit `course.md` by hand.**
> A chapter becomes part of the course by being listed in the Chapters List table above.
> To rebuild locally, run `python3 .github/scripts/build_course.py`.

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
    "How to manage and debug Jobs",
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
