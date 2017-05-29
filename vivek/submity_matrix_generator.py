#!/bin/bash
#
#SBATCH --comment=r-test
#SBATCH --ntasks=1
#SBATCH --job-name=y_matrix_generator
#SBATCH --output=output.%j.r-test
#SBATCH --time=01:00:00
#SBATCH --mem=10G

#### SLURM 4 processor R test to run for 1 hour.

module purge
module add apps/python/3.5.1

python y_matrix_generator.py home/cis1024/sample_images_clean home/cis1024/
