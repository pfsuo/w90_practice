set style data dots
set nokey
set xrange [0: 8.57087]
set yrange [-15.83253 : 17.60433]
set arrow from  1.71141, -15.83253 to  1.71141,  17.60433 nohead
set arrow from  2.56712, -15.83253 to  2.56712,  17.60433 nohead
set arrow from  4.04925, -15.83253 to  4.04925,  17.60433 nohead
set arrow from  4.52162, -15.83253 to  4.52162,  17.60433 nohead
set arrow from  6.23303, -15.83253 to  6.23303,  17.60433 nohead
set arrow from  7.08873, -15.83253 to  7.08873,  17.60433 nohead
set xtics ("G"  0.00000,"K"  1.71141,"M"  2.56712,"G"  4.04925,"A"  4.52162,"H"  6.23303,"L"  7.08873,"A"  8.57087)
 plot "wannier90_band.dat"
