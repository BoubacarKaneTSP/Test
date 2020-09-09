#!/bin/bash

# kill all the children of the current process
trap "pkill -KILL -P $$; exit 255" SIGINT SIGTERM
trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

NBTEST="2"

for type in 'counter' 'list' 'set'
do
	#for i in 1 2 3 4 5 6 7 8 9 10 12 14 16 18 20 25 30 40 50 60 70 80 90;
	for i in 1 5 10;
	do
		echo " " > "Resultats/resultats_${type}_${i}_process.txt"
		for j in `seq 1 $NBTEST`
		do
			echo " Lancement du workload $type pour *$i* processus (test numero $j)"
			#python3 reset.py
			python3 workload_$type.py $i #>> "Resultats/resultats_${type}_${i}_process.txt"
		done
	done
done
echo " Fin du programme "
