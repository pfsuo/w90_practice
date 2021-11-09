from ase.calculators.vasp import Vasp
from ase.io import read
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('Agg')
nbands = 20
npoints = int([line for line in open('wannier90_band.kpt')][0])
def calc_scf():
    calc = Vasp(
            command = 'mpirun -n %d vasp_std' % nbands,
            xc = 'LDA',
            setups='recommended',
            kpts=(15,15,1),
            istart=0,
            icharg=2,
            encut=520,
            ncore=4,
            ismear=0,
            sigma=0.1,
            prec='Accurate',
            ediff=1e-6)    
    return calc

## bandstructure calculation
def band_calc(atoms):
    calc = calc_scf()
    atoms.calc = calc
    calc.set(
            directory='band')
    atoms.get_potential_energy()
    efermi = float([line for line in open('band/DOSCAR') if line.strip()][5].split()[-2])
    with open('FERMI_ENERGY','w') as f:
        print('# Fermi level in scf calculation',file=f)
        print('%10.6f' % efermi,file=f)
    calc.set(isym=0,
            kpts={'path':'GKMG','npoints':npoints},
            istart=1,
            icharg=11,
            ismear=0,
            sigma=0.1,
            lorbit=10,
            nbands=nbands,
            lwave=False,
            lcharg=False)
    atoms.get_potential_energy()
    e_nk = calc.band_structure().energies[0].T - efermi     # get band data with reference to efermi
    path = atoms.cell.bandpath('GKMG',npoints=npoints)
    x, X, _ = path.get_linear_kpoint_axis()
    np.savetxt('e_nk.dat',e_nk)           # save the band data
    with open('kpath.dat','w') as f:
        for k in x:
            print(k,file=f)          # save the kpath axis data
    with open('highk.dat','w') as f:
        for k in X:
            print(k,file=f)         # save the high K data

## plot bandstructure
def plot_band(figsize=(6,5)):
    plt.figure(figsize=figsize)
    e_nk = np.loadtxt('e_nk.dat')
    x = np.loadtxt('kpath.dat')
    X = np.loadtxt('highk.dat')
    for e_n in e_nk:
        plt.plot(x, e_n, c='r', lw=2)
    plt.axhline(y=0,c='k',alpha=0.5,lw=1,ls='--')
    for i in X:
        plt.axvline(x=i,c='k',alpha=0.5,lw=1,ls='--')
    plt.axis([x[0],x[-1],-5,5])
    plt.xticks(X,[r'$\Gamma$','K','M',r'$\Gamma$'],size=15)
    plt.yticks(size=14)
    plt.ylabel(r'$\varepsilon_n(k) - \varepsilon_{F}$ (eV)', size=20)
    plt.title('band structure of graphene',size=20)
    plt.savefig('band/band_graphene.png',dpi=600)
    plt.close()

if __name__=='__main__':
    atoms = read('../POSCAR')
    band_calc(atoms)
    plot_band() 
