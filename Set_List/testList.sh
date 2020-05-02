#!/bin/bash

# kill all the children of the current process
trap "pkill -KILL -P $$; exit 255" SIGINT SIGTERM

python3 createSystem.py

echo " " > "ResultatList/resultat_$1_process.txt"

#Nombre de test
for i in `seq 1 5`
do
	echo "====================================== Lancement du test LIST numero $i ======================================"
	python3 deleteList.py
	python3 createSystem.py
	./startProgramList.sh $1 &
	sleep 1m
	kill $!
	python3 readList.py >> "ResultatList/resultat_$1_process.txt"
done
