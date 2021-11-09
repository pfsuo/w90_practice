#!/bin/bash
#SBATCH -J QE_2D
#SBATCH -N 1
#SBATCH -n 24
#SBATCH -o out
#SBATCH -x cu[09-18]

#python scf.py
mpirun -n $SLURM_NTASKS pw.x -inp scf.pwi > scf.pwo
mpirun -n $SLURM_NTASKS pw.x -inp nscf.pwi > nscf.pwo
#python QE_band.py
