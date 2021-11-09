from ase.calculators.vasp import Vasp
import numpy as np
from ase.io import read

atoms = read('../../POSCAR')
calc = Vasp(
        command='mpirun -n 20 /opt/vasp.5.4.4_w90-2.1/bin/vasp_std',
        xc='LDA',
        setups='recommended',
        kpts=(15,15,1),
        istart=1,
        icharg=11,
        encut=520,
        ismear=0,
        sigma=0.1,
        prec='Accurate',
        ediff=1e-8,
        nbands=20,
        lwave=False,
        lcharg=False,
        lwannier90=True)

atoms.calc = calc
atoms.get_potential_energy()
