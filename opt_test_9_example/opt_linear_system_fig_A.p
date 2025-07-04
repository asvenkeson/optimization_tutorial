set terminal postscript eps size 3.4, 2.1 enhanced color font 'Helvetica,15'
set output 'opt_linear_system_fig_A.eps'

set xlabel "Time, n"
set ylabel "System state, x(n)"

#set format x "%.1tx10^{%S}"
#set format y "%.1tx10^{%S}"

unset key
set key right

unset label
#set label "({/Symbol a}=0.50)" at graph 0.6, graph 0.5

unset yrange
#set yrange [0:2]


plot "opt_linear_system_A.txt" using 1:2 with points title "state, x(n)", "opt_linear_system_A.txt" using 1:3 with points title "target, x_t"    
