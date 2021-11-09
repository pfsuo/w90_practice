set style data dots
set nokey
set xrange [0: 8.57088]
set yrange [-13.63373 : 19.70190]
set arrow from  1.71141, -13.63373 to  1.71141,  19.70190 nohead
set arrow from  2.56712, -13.63373 to  2.56712,  19.70190 nohead
set arrow from  4.04926, -13.63373 to  4.04926,  19.70190 nohead
set arrow from  4.52162, -13.63373 to  4.52162,  19.70190 nohead
set arrow from  6.23303, -13.63373 to  6.23303,  19.70190 nohead
set arrow from  7.08874, -13.63373 to  7.08874,  19.70190 nohead
set xtics ("G"  0.00000,"K"  1.71141,"M"  2.56712,"G"  4.04926,"A"  4.52162,"H"  6.23303,"L"  7.08874,"A"  8.57088)
 plot "graphite_band.dat"
