import numpy as np
from ase.io import read
import sys

seedname = sys.argv[1]
num_bands = 16
num_wann = 4
dis_num_iter = 1e4
dis_win_max = 21.5
kpts = [15,15,3]
kpath=np.array([[0.,0.,0.],
                [1/3,1/3,0.],
                [.5,0.,0.],
                [0.,0.,0.],
                [0.,0.,.5],
                [1/3,1/3,.5],
                [.5,0.,.5],
                [0.,0.,.5]])
X = ['G','K','M','G','A','H','L','A']

atoms = read('scf.pwo')
f = open( seedname + '.win', 'w')

def proj_set(mode='projection'):
    print('num_bands\t=\t%d' % num_bands,file=f)
    print('num_wann\t=\t%d' % num_wann,file=f)
    print('num_iter\t=\t200' ,file=f)
    print('dis_num_iter\t=\t%d' % dis_num_iter,file=f)
    print('kmesh_tol\t=\t0.0001' ,file=f)
    print(file=f)
    if mode == 'scdm':
        print('auto_projections = .true.',file=f)
    elif mode == 'projection':
        print('dis_win_max\t=\t%.1f' % dis_win_max, file=f)
        print('begin projections',file=f)
        print('C:pz',file=f)
        print('end projections',file=f)
    print(file=f)

def band_plot():
    print('write_xyz = .true.',file=f)
    print('bands_plot = .true.',file=f)
    print('bands_num_points = 100',file=f)
    print('bands_plot_format = gnuplot',file=f)
    print(file=f)
    print('begin kpoint_path',file=f)
    for i in range(len(X)-1):
        print('%s%10.5f%10.5f%10.5f   %s%10.5f%10.5f%10.5f' % \
(X[i],kpath[i][0],kpath[i][1],kpath[i][2],X[i+1],kpath[i+1][0],kpath[i+1][1],kpath[i+1][2]),file=f)
    print('end kpoint_path',file=f)
    print(file=f)

def atoms_pos():
    natom = atoms.get_global_number_of_atoms()
    atom_symbols = atoms.get_chemical_symbols()
    print('begin atoms_cart',file=f)
    for i in range(natom):
        print(atoms.get_chemical_symbols()[i],end='\t',file=f)
        for j in range(3):
            print('%12.8f' % atoms.positions[i][j],end='\t',file=f)
        print(file=f)
    print('end atoms_cart',file=f)
    print(file=f)

def unit_cell():
    print('begin unit_cell_cart',file=f)
    for i in range(3):
        for j in range(3):
            print('%12.8f' % atoms.cell[i][j],end='\t',file=f)
        print(file=f)
    print('end unit_cell_cart',file=f)
    print(file=f)

def kpoints():
    print('mp_grid:  %d  %d  %d' % (kpts[0],kpts[1],kpts[2]),file=f)
    print(file=f)
    print('begin kpoints',file=f)
    for i in range(kpts[0]):
        for j in range(kpts[1]):
            for k in range(kpts[2]):
                print('%12.8f%12.8f%12.8f' % (i/kpts[0],j/kpts[1],k/kpts[2]),file=f)
    print('end kpoints',file=f)

def tb_para():
    print('write_hr = .true.',file=f)
    print('write_tb = .true.',file=f)
    print('write_hr_diag = .true.',file=f)
    print(file=f)

if __name__=="__main__":
    proj_set()
    band_plot()
    tb_para()
    atoms_pos()
    unit_cell()
    kpoints()
    f.close()
