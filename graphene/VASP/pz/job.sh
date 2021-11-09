#!/bin/bash
#SBATCH -J graphene
#SBATCH -N 1
#SBATCH -n 24
#SBATCH -o out

#python nscf.py
python VASP_band.py
