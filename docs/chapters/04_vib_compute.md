# VIB Data Core Compute Cluster

## Request a Compute Account 
- Through Connect: https://connect.vib.be/services/command-line-analysis

Two main entrypoints to interact with the Compute Cluster:

- Command line access through SSH
- Browser via Open OnDemand

Relevant Data Core documentation: https://docs.datacore.vib.be/compute-cluster/entrypoints/

## Connect to Compute via SSH

Follow the guide that fits your Operating System from: https://docs.datacore.vib.be/compute-cluster/entrypoints/command-line-access#connect-with-ssh. It walks you through the installation of [Smallstep](https://docs.datacore.vib.be/compute-cluster/entrypoints/command-line-access#installing-smallstep) which leverages the VIB Single-Sign On (SSO) to securely connect you to Compute. Depending on your workstation, its operating system and by who it is managed, **you might need admin privileges in order to install the step command**, so permission might be required by your local IT helpdesk.

### Login

```sh
ssh -p2022 firstname.lastname@compute.vib.be
```

As your home folder is limited in capacity, as it is meant for configuration files and not for any type of analysis data, you should work in your group or project folder. This is the performant storage option Compute Storage provided by Data Core, where the following documentation entry shows you how to identify yours and how much storage they have: https://docs.datacore.vib.be/data-storage/compute-storage/#directory-structure. For more information on data organization on Compute, see https://docs.datacore.vib.be/compute-cluster/data-organization.


## Connect to Compute via the web browser (Open OnDemand)
- Link to VIB Compute's Open OnDemand: https://compute.vib.be, where you can log in with your @vib.be email using the VIB SSO.

## Request a Secure Compute Account
If you are working with **GDPR Sensitive Data**, you should work on the VIB Data Core Secure Compute. Access should be requested by the Group Leader and can be done via the same VIB Connect link found at the top of this page. 
