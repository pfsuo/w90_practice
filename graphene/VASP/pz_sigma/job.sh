#!/bin/bash
#SBATCH -J graphene
#SBATCH -N 1
#SBATCH -n 20
#SBATCH -o out

#python nscf.py
#mpirun -n $SLURM_NTASKS wannier90.x wannier90
python VASP_band.py
python w90_vs_VASP.py
