#!/bin/sh
#SBATCH --job-name=g7_pqqg
#SBATCH --output=%j_g7_pqqg.out
#SBATCH --error=%j_g7_pqqg.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --partition=kite
#SBATCH --time=1:00:00

#load necessary modules
source activate /project2/rossby/group07/.conda

ncores=16
#file=/project2/rossby/group07/analysis/model_runner_parallel.py
file=/project2/rossby/group07/analysis/model_runner_parallel_SO.py

python $file $ncores

