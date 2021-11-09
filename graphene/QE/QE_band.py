from ase.calculators.espresso import Espresso
from ase.io import read
import os
import numpy as np

seed = 'graphene'
kpath = 'GKMG'
nbands = 16
npoints = int([line for line in open(seed+'_band.kpt')][0])
ef = float([line for line in open('scf.pwo') if 'Fermi' in line][0].split()[-2])
with open('FERMI_ENERGY','w') as f:
    print('# Fermi Energy in scf calculation',file=f)
    print('%10.6f' % ef,file=f)

atoms = read('../POSCAR')
pseudo_dir='/opt/LDA'
pseudopotentials={'C':'C.pz-n-kjpaw_psl.1.0.0.UPF'}

kpts={'path':kpath, 'npoints':npoints}
path = atoms.cell.bandpath(kpath,npoints=npoints)
x, X, _ = path.get_linear_kpoint_axis()
with open('kpath.dat','w') as f:
    for k in x:
        print(k,file=f)
with open('highk.dat','w') as f:
    for k in X:
        print(k,file=f)

def calc_qe(mode='bands',ecut=60,conv=1e-12):
    calc = Espresso(calculation=mode,
                label=mode,
                outdir='./tmp',
                prefix='graphene',
                verbosity='high',
                pseudo_dir=pseudo_dir,
                pseudopotentials=pseudopotentials,
                kpts=kpts,
                nbnd=nbands,
                occupations='smearing',
                smearing='gauss',
                degauss=1e-1,
                ecutwfc=ecut,
                ecutrho=8*ecut,
                ibrav=4,
                assume_isolated = '2D',
                conv_thr=conv)
    return calc

calc = calc_qe()
atoms.calc = calc
calc.calculate(atoms)
e_nk = calc.band_structure().energies[0].T - ef
np.savetxt('e_nk.dat', e_nk)
