from gpaw import GPAW, PW, FermiDirac, mpi
import numpy as np
from ase.io import read
from ase.parallel import paropen
from GPAW_wann import seed

## band structure calculation
npoints = int([line for line in open(seed+'_band.kpt')][0])
atoms = read('scf.out')
path = atoms.cell.bandpath('GKMGAHLA',npoints=npoints)
calc = GPAW('scf.gpw').fixed_density(symmetry='off',
                        kpts=path.kpts,
                        nbands=16,
                        txt='band.out')
## save the data of band structure
x, X, _ = path.get_linear_kpoint_axis()
with paropen('kpath.dat','w') as f:
    for k in x:
        print(k,file=f)

with paropen('highk.dat','w') as f:
    for k in X:
        print(k,file=f)

ef = calc.get_fermi_level()
e_nk = calc.band_structure().energies[0].T - ef
if mpi.world.rank == 0:
    with open('FERMI_ENERGY','w') as f:
        print('# Fermi level in scf calculation',file=f)
        print('%10.6f' % ef,file=f)
    np.savetxt('e_nk.dat', e_nk)
