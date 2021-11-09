from ase.calculators.espresso import Espresso
from ase.io import read
import os

atoms = read('../POSCAR')
pseudo_dir='/opt/LDA'
pseudopotentials={'C':'C.pz-n-kjpaw_psl.1.0.0.UPF'}

def calc_qe(mode='scf',kpts=(15,15,3),ecut=60,conv=1e-12):
    calc = Espresso(calculation=mode,
                label=mode,
                outdir='./tmp',
                prefix='graphite',
                pseudo_dir=pseudo_dir,
                pseudopotentials=pseudopotentials,
                kpts=kpts,
                occupations='smearing',
                smearing='gauss',
                degauss=1e-1,
                ecutwfc=ecut,
                ecutrho=8*ecut,
                ibrav=4,
                conv_thr=conv)
    return calc

atoms.calc = calc_qe()
atoms.get_potential_energy()
