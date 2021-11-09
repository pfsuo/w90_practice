#!/bin/bash
#SBATCH -J graphene
#SBATCH -N 1
#SBATCH -n 24
#SBATCH -o out

mpirun -n $SLURM_NTASKS /opt/vasp.5.4.4_w90-2.1/bin/vasp_std
