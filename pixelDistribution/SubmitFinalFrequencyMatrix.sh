#!/bin/bash
#SBATCH --job-name=python
#SBATCH --time=05:00:00
#SBATCH --ntasks=1

module purge
module add apps/python/3.5.1

python FinalFrequencyMatrix.py
