#!/bin/bash
#SBATCH -J graphite
#SBATCH -N 1
#SBATCH -n 20
#SBATCH -o out

mpirun -n $SLURM_NTASKS /opt/vasp.5.4.4/bin/vasp_std
