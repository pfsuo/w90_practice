#!/bin/bash
#SBATCH -J graphite
#SBATCH -N 1
#SBATCH -n 16
#SBATCH -o out

rm -f *png gra* *.out *gpw *dat FERMI_ENERGY
gpaw -P $SLURM_NTASKS python GPAW_scf.py
python GPAW_wann.py
cp templete gra.win
mpirun -np 16 wannier90.x gra
gpaw -P $SLURM_NTASKS python GPAW_band.py
python w90_vs_GPAW.py
