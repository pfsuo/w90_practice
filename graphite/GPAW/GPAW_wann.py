import os
import gpaw.wannier90 as w90
from gpaw import GPAW, mpi

seed = 'gra'
orbitals_ai = [[2],[2],[2],[2]]

if __name__=="__main__":
    calc = GPAW('nscf.gpw')
    w90.write_input(calc,orbitals_ai=orbitals_ai,
            bands=range(2,16),
            seed = seed,
            num_iter = 200,
            dis_num_iter = 1e4,
            write_xyz=True)
    os.system('wannier90.x -pp ' + seed)

    w90.write_projections(calc,orbitals_ai=orbitals_ai,seed=seed)
    w90.write_eigenvalues(calc,seed=seed)
    w90.write_overlaps(calc,seed=seed)
