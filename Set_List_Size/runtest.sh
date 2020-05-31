#!/bin/bash

#kill all the children of the current process
trap "pkill -KILL -P $$; exit 255" SIGINT SIGTERM

BORNEINF="0"


python3 createSystem.py
python3 deleteSet.py
python3 createSystem.py

#Nombre de process
#for i in 100 200 300 400 500 600 700 800 900 1000 2000 3000 4000 5000 10000 15000 20000 25000 30000 35000 40000 45000 50000 60000 70000 80000 90000 100000 110000 120000 130000 140000 150000 160000 170000 180000 190000 200000 210000 220000 230000 240000 250000 260000 270000 280000 290000 300000 310000 320000 330000 340000 350000 360000 370000 380000 390000 400000 410000 420000 430000 440000 450000 460000 470000 480000 490000 500000 600000 700000 800000 900000 1000000;
for i in `seq 0 1000`;
do
	
	BORNEINF=$(($i*1000))	
	BORNESUP=$((($i+1)*1000))

	
	echo "addSet.py $BORNEINF $BORNESUP"
	#python3 addSet.py $BORNEINF $BORNESUP
	{ time python3 addSet.py $BORNEINF $BORNESUP > "Resultat/resultat_$BORNESUP.txt" ; } 2> "Resultat/resultat_$BORNESUP.txt"
	#{ time python3 readTable.py > "Resultat/resultat_$BORNESUP.txt" ; } 2> "Resultat/resultat_$BORNESUP.txt"
	
	#BORNEINF=$i
done

wait
