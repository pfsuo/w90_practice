set style data dots
set nokey
set xrange [0: 4.04972]
set yrange [-11.45058 :  9.76659]
set arrow from  1.71161, -11.45058 to  1.71161,   9.76659 nohead
set arrow from  2.56741, -11.45058 to  2.56741,   9.76659 nohead
set xtics ("G"  0.00000,"K"  1.71161,"M"  2.56741,"G"  4.04972)
 plot "wannier90_band.dat"
