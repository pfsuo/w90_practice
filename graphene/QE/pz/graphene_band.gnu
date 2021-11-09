set style data dots
set nokey
set xrange [0: 4.04972]
set yrange [-13.00972 :  8.09267]
set arrow from  1.71161, -13.00972 to  1.71161,   8.09267 nohead
set arrow from  2.56741, -13.00972 to  2.56741,   8.09267 nohead
set xtics ("G"  0.00000,"K"  1.71161,"M"  2.56741,"G"  4.04972)
 plot "graphene_band.dat"
