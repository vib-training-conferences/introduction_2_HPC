#!/bin/bash
#SBATCH --job-name=test_job_submission
#SBATCH --partition=debug_28C_56T_750GB
#SBATCH --mem=8G
#SBATCH --time=00:05:00
#SBATCH --account=<slurm_account>
# Read how you can find your Slurm account in the Data Core docs: https://docs.datacore.vib.be/compute-cluster/job-scheduling/#find-your-slurm-account

# Define variables
DOCKER_IMG="docker://hello-world"

# Best practice to purge all loaded modules first
module purge

# Load necessary modules (none needed for this example), example line below:
# module load Python/3.13.1-GCCcore-14.2.0

# Pull minimal Docker image using Singularity
singularity pull $DOCKER_IMG

# Sleep for 20 seconds so there is time to see the job via `squeue`
echo 'Going to sleep for 20 seconds... ZZZzzzzz....'
sleep 20

# Execute the hello world image. The Docker deamon will create a new container wich has an executable inside that will display text in your terminal:
singularity run hello-world_latest.sif

# Submit this Slurm launch script using the following command (from the same directory this file is in):
# sbatch slurm_vib.sh
