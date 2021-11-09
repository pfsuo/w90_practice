from gpaw import GPAW, PW, FermiDirac
from ase.io import read

atoms = read('../POSCAR')
calc = GPAW(mode=PW(520),
            xc='LDA',
            kpts=(15,15,3),
            occupations=FermiDirac(0.01),
            convergence={'density':1e-6},
            txt='scf.out')
atoms.calc = calc
atoms.get_potential_energy()
calc.write('scf.gpw')
calc.fixed_density(
            symmetry='off',
            nbands=20,
            convergence={'bands':16},
            txt='nscf.out').write('nscf.gpw','all')
