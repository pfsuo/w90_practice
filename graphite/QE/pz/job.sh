#!/bin/bash
#SBATCH -J pz
#SBATCH -N 1
#SBATCH -n 24
#SBATCH -o out
#SBATCH -x cu[09-18]

rm -f QE* *mmn *amn *eig *nnkp
wannier90.x -pp graphite
mpirun -n $SLURM_NTASKS pw2wannier90.x -inp pw2wan.inp > pw2wan.out
mpirun -n $SLURM_NTASKS wannier90.x graphite
