import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('Agg')
from GPAW_wann import seed, orbitals_ai
from gpaw import GPAW

nwan = 0
for orbital in orbitals_ai:
    nwan += len(orbital)

lw = 1.2
fontsize = 15
title = 'w90 vs DFT'

ef = np.loadtxt('FERMI_ENERGY')
kx = np.loadtxt('kpath.dat')
X = np.loadtxt('highk.dat')
e_nk = np.loadtxt('e_nk.dat')
klabels = [r'$\Gamma$','K','M',r'$\Gamma$','A','H','L','A']

## read band data from _band.dat file
ewan_kn=np.zeros((len(kx),nwan),dtype=float)
f=open(seed+'_band.dat')
for i in range(nwan):
    for j in range(len(kx)):
        l=f.readline()
        ewan_kn[j,i]=float(l.split()[1]) - ef
    l=f.readline()
f.close()
ewan_nk = ewan_kn.T

## plot the bandstructrue
def plot_band(window=False):
    for e_k in e_nk:
        plt.plot(kx,e_k,c='r',lw=1.2)
    plt.plot(-1,-1,c='r',lw=1.2,label='DFT')
    for ewan_k in ewan_nk:
        plt.plot(kx,ewan_k,c='b',lw=1.2,ls='--')
    plt.plot(-1,-1,c='b',lw=1.2,ls='--',label='w90')
    for k in X[1:-1]:
        plt.axvline(x=k,c='k',lw=0.5,ls='--')
    plt.axhline(y=0,c='k',lw=0.5,ls='--')
    plt.xticks(X,klabels,size=15)
    plt.yticks(size=10)
    plt.ylabel(r'$\varepsilon_n(k) - \varepsilon_{\mathrm{F}}$ (eV)',size=15)
    plt.title(title, size=18)
    plt.xlim([0,kx[-1]])
    plt.legend(fontsize=12)
    if window:
        plt.axis([0,kx[-1],-5,5])

plt.figure(figsize=(9,4))
plt.subplot(121)
plot_band()
plt.subplot(122)
plot_band(True)
plt.tight_layout()
plt.savefig('GPAW_graphite_pz.png',dpi=600)
plt.close()
