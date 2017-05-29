#!/bin/bash
#SBATCH --job-name=python
#SBATCH --time=01:00:00
#SBATCH --ntasks=1

module purge
module add apps/python/3.5.1

python imageProcessing.py
