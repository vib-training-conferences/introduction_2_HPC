# VIB Data Core Compute Cluster

## Request a Compute Account 
- Link: https://connect.vib.be/services/command-line-analysis

Two main entrypoints to interact with the Compute Cluster:

- Command line access through SSH
- Browser via Open OnDemand

Relevant Data Core documentation: https://docs.datacore.vib.be/compute-cluster/entrypoints/

## Connect to Compute via SSH

See https://docs.datacore.vib.be/compute-cluster/entrypoints/command-line-access#connect-with-ssh

Only requirement is installation of [Smallstep](https://docs.datacore.vib.be/compute-cluster/entrypoints/command-line-access#installing-smallstep). 

### Login

```sh
ssh -p2022 firstname.lastname@compute.vib.be
```

Work in your group folder, which is Compute Storage. Check via the `groups` command which group you belong to. 
Check on one of the login nodes with the `groupquotas` command how much quota your group folder has and how much there is left. 

You can read more about Compute Storage here: https://docs.datacore.vib.be/data-storage/compute-storage/#directory-structure

Data organization on Compute: https://docs.datacore.vib.be/compute-cluster/data-organization


## Connect to Compute via the web browser (Open OnDemand)
- Link to VIB Compute's Open OnDemand: https://compute.vib.be and log in with your VIB credentials.
