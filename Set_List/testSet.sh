#!/bin/bash

# kill all the children of the current process
trap "pkill -KILL -P $$; exit 255" SIGINT SIGTERM

python3 createSystem.py

echo " " > "ResultatSet/resultat_$1_process.txt"

#Nombre de test
for i in `seq 1 1`
do
	echo "====================================== Lancement du test SET numero $i ======================================"
	python3 deleteSet.py
	python3 createSystem.py
	./startProgramSet.sh $1 &
	sleep 3m
	kill $!
	python3 readSet.py >> "ResultatSet/resultat_$1_process.txt"
done
