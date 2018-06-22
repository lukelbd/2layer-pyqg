#!/bin/sh
#SBATCH --job-name=g7_pqqg
#SBATCH --output=out/%j_g7_pqqg.out
#SBATCH --error=out/%j_g7_pqqg.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem-per-cpu=2000M
#SBATCH --account=rossby
#SBATCH --partition=rossby
#SBATCH --time=1:00:00

#load necessary modules
source activate /project2/rossby/group07/.conda

ncores=16
#file=/project2/rossby/group07/analysis/model_runner_parallel.py
file=/project2/rossby/group07/analysis/model_runner_parallel_atm.py

python $file $ncores

