#!/bin/bash

# kill all the children of the current process
trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT
trap "pkill -KILL -P $$; exit 255" SIGINT SIGTERM

let "NBITERATION=3"

echo "" > "Resultats.txt" 

for i in `seq 0 $NBITERATION`
do
	echo "Lancement du test numero : $i"
	./test.sh $1
	python3 read_results.py $1 >> "Resultats.txt" 
done
