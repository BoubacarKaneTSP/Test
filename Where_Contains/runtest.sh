#!/bin/bash

#kill all the children of the current process
trap "pkill -KILL -P $$; exit 255" SIGINT SIGTERM

RANDOM=$$
BORNESUP="-1"
LAST="0"


python3 createSystem.py
python3 deleteSystem.py
python3 createSystem.py

#Nombre de process
#for i in 100 200 300 400 500 600 700 800 900 1000 2000 3000 4000 5000 10000 15000 20000 25000 30000 35000 40000 45000 50000 100000 200000 300000 400000 500000 600000 700000 800000 900000 1000000;
for i in 100 200;
do
	
	BORNEINF=$((BORNESUP+1))
	FIRST=$BORNEINF

	echo "===== Remplissage de la base de donnee ====="

	DIXIEME=$((($i-$LAST)/10))
	for p in `seq 1 10`;
	do
		echo "start process $p"
		BORNESUP=$(((p*DIXIEME)-1+LAST))
		echo "$BORNEINF $BORNESUP $i"
		python3 addRow.py $BORNEINF $BORNESUP &
		BORNEINF=$((BORNESUP+1))
	done
	
	wait

	
	echo "===== Phase de follow aleatoire pour chaque process pour $i lignes ====="

	BORNEINF=$FIRST

	for p in `seq 1 10`;
	do
		BORNESUP=$(((p*DIXIEME)-1+LAST))
		echo "$BORNEINF $BORNESUP $i"
		./script_follow.sh $BORNEINF $BORNESUP $i &
	
		BORNEINF=$((BORNESUP+1))
	done
	
	wait 

	{ time python3 readTable.py >> "Resultat/resultat_$i.txt" ; } 2> "Resultat/resultat_$i.txt"
	
	LAST=$i
done

wait
