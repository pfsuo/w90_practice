#!/bin/bash
#SBATCH -J graphene
#SBATCH -N 1
#SBATCH -n 16
#SBATCH -o out
#SBATCH -w cu[18]

#gpaw -P $SLURM_NTASKS python scf.py
#python wann.py
#cp templete gra.win
mpirun -np 16 wannier90.x gra
#gpaw -P $SLURM_NTASKS python band.py
python w90_vs_GPAW.py
