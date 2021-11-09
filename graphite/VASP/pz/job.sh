#!/bin/bash
#SBATCH -J nscf
#SBATCH -N 1
#SBATCH -n 20
#SBATCH -o out

#mpirun -n $SLURM_NTASKS vasp_std
python VASP_band.py
python w90_vs_VASP.py
