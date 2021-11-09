set style data dots
set nokey
set xrange [0: 8.57087]
set yrange [ -3.26058 : 18.86840]
set arrow from  1.71141,  -3.26058 to  1.71141,  18.86840 nohead
set arrow from  2.56712,  -3.26058 to  2.56712,  18.86840 nohead
set arrow from  4.04925,  -3.26058 to  4.04925,  18.86840 nohead
set arrow from  4.52162,  -3.26058 to  4.52162,  18.86840 nohead
set arrow from  6.23303,  -3.26058 to  6.23303,  18.86840 nohead
set arrow from  7.08873,  -3.26058 to  7.08873,  18.86840 nohead
set xtics ("G"  0.00000,"K"  1.71141,"M"  2.56712,"G"  4.04925,"A"  4.52162,"H"  6.23303,"L"  7.08873,"A"  8.57087)
 plot "gra_band.dat"
