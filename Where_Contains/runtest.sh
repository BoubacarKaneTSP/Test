#!/bin/bash

#kill all the children of the current process
trap "pkill -KILL -P $$; exit 255" SIGINT SIGTERM

RANDOM=$$

#Nombre de process
#for i in 100 200 300 400 500 600 700 800 900 1000 2000 3000 4000 5000 10000 15000 20000 25000 30000 35000 40000 45000 50000 100000 200000 300000 400000 500000 600000 700000 800000 900000 1000000;
for i in 10 20;
do
	python3 addRow.py $i
	
	#Phase de follow aleatoire pour chaque process
	for j in `seq 0 $i`;
	do
		DIV=$(((i*10)/100))

		for n in `seq 0 $DIV`;
		do
			PROCESS=$(($RANDOM%$i))
			python3 follow_user.py $j $PROCESS
		done
	done
	
	{ time python3 readTable.py >> "Resultat/resultat_$i.txt" ; } 2> "Resultat/resultat_$i.txt"
	python3 deleteSystem.py
	python3 createSystem.py
done

wait
