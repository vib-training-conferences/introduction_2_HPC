#!/bin/bash
#SBATCH --job-name=-NEWreport
#SBATCH --partition=donphan
#SBATCH --mem=4G
## SBATCH --mail-user=bruna.piereckmoura@vib.be
## SBATCH --mail-type=end #### NONE, BEGIN, END, FAIL, REQUEUE, ALL
#SBATCH -e "slurm_%x_%j.error"  ## %x takes job name; %j takes job ID
#SBATCH -o "slurm_%x_%j.out"
#SBATCH --time=00:05:00

# Define variables
DOCKER_IMG="docker://hello-world"

# Best practice to purge all loaded modules first
module purge

# Pull minimal Docker image using Singularity
singularity pull $DOCKER_IMG

# Sleep for 40 seconds so there is time to see the job via `squeue`
echo 'Going to sleep for 40 seconds... ZZZzzzzz....'
sleep 40

# Execute the hello world image. The Docker deamon will create a new container wich has an executable inside that will display text in your terminal:
singularity run hello-world_latest.sif

# Sleep 5 seconds before creating report
sleep 5

# Creating resources report
echo "=== Report resources usage ==="
sacct -j $SLURM_JOBID  --format=jobid,partition,elapsed,state,totalcpu,maxrss,averss
