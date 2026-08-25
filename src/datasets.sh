#!/bin/bash
#SBATCH --job-name=dataset
#SBATCH --account=project_2020425
#SBATCH --partition=small
#SBATCH --time=00:05:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=1000M

# Run the program
srun python dataset.py
