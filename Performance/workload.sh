#!/bin/bash

# kill all the children of the current process
trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT
trap "pkill -KILL -P $$; exit 255" SIGINT SIGTERM

NUMCLIENT="$1"
NBOPERATION=$((0))

echo "0" > "Perf/resultat_client_$NUMCLIENT.txt"

while [ 1 ]
do
	python3 vide.py
	#echo "1"
	NBOPERATION=$(($NBOPERATION+1))
	
	echo "$NBOPERATION" >> "Perf/resultat_client_$NUMCLIENT.txt"
done
