reset
set terminal svg
set output "output.svg"
set xrange [0:100]
set yrange [0:100]
plot "draw.txt" with linespoints linewidth 3 pointsize 1 pointtype 5
