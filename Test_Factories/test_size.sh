#!/bin/bash

# kill all the children of the current process
trap "pkill -KILL -P $$; exit 255" SIGINT SIGTERM
trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

NBTEST="2"

for type in 'list' 'set'
do
	echo " " > "resultat_${type}.txt"

	#for i in 10 100 1000 10000 20000 30000 40000 50000 100000 1000000;
	for i in 1 10 100;
	do
		echo " " > "Resultats/resultats_${type}_${i}_size.txt"
		for j in `seq 1 $NBTEST`
		do
			echo "Lancement du workload $type pour size *$i* (test numero $j)"
			python3 reset.py
			python3 fill_collection.py $type $i
			python3 workload_${type}_shell.py >> "Resultats/resultats_${type}_${i}_size.txt" 
			echo "fin"

		done
		
		python3 read_results.py $i $NBTEST $type >> "resultat_${type}.txt"

	done
done
echo " Fin du programme "
