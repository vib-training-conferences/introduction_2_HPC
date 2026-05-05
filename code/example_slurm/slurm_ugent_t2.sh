#!/bin/bash
#SBATCH --job-name=NEW_job_hello-world
#SBATCH --partition=donphan
#SBATCH --mem=8G
#SBATCH -e "slurm_%x_%j.error"  ## %x takes job name; %j takes job ID
#SBATCH -o "slurm_%x_%j.out"
#SBATCH --time=00:05:00

# Define variables
DOCKER_IMG="docker://hello-world"

# Best practice to purge all loaded modules first
module purge

# Pull minimal Docker image using Singularity
singularity pull $DOCKER_IMG

# Sleep for 60 seconds so there is time to see the job via `squeue`
echo 'Going to sleep for 60 seconds... ZZZzzzzz....'
sleep 60

# Execute the hello world image. The Docker deamon will create a new container wich has an executable inside that will display text in your terminal:
singularity run hello-world_latest.sif