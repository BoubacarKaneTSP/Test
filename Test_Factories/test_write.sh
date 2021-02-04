#!/bin/bash

# kill all the children of the current process
trap "pkill -KILL -P $$; exit 255" SIGINT SIGTERM
trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

NBTEST="10"

for i in `seq 1 $NBTEST`
do
	echo "Lancement du test writing pour un registre (test numero $i)"
	python3 reset.py
	python3 workload_write.py >> "Resultats/resultats_registre_test_${i}_write.txt"
	echo "fin"
done

for type in 'list' 'set'
do
	#echo " " > "resultat_${type}.txt"

	echo " " > "Resultats/resultats_${type}_write.txt"
	for j in `seq 1 $NBTEST`
	do
		echo "Lancement du test writing $type (test numero $j)"
		python3 reset.py
		python3 fill_collection.py $type >> "Resultats/resultats_${type}_test_${j}_write.txt"
		echo "fin"
	done


done
echo " Fin du programme "
