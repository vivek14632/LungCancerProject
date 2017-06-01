#!/bin/bash
#
#SBATCH --comment=r-test
#SBATCH --ntasks=1
#SBATCH --job-name=y_matrix_generator.py
#SBATCH --output=output.%j.r-test
#SBATCH --time=1:00:00
#SBATCH --mem=10G

#### SLURM 4 processor R test to run for 1 hour.

module purge
module add apps/python/3.5.1

python patient_label_generator.py /work/v/vivek4/stage1_clean_bak /work/v/vivek4/stage1_clean_bak_Y_matrix 
#python test.py
