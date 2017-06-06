#!/bin/bash
#
#SBATCH --comment=r-test
#SBATCH --ntasks=1
#SBATCH --job-name=all_models_patient_level
#SBATCH --output=output.%j.r-test
#SBATCH --time=4:00:00
#SBATCH --mem=20G

#### SLURM 4 processor R test to run for 1 hour.

module purge
module add apps/python/3.5.1

python all_models_patient_level.py /work/v/vivek4/stage1_clean_bak
