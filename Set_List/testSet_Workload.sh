#!/bin/bash

# kill all the children of the current process
trap "pkill -KILL -P $$; exit 255" SIGINT SIGTERM

python3 createSystem.py


#Differents workload : % de read

for j in `seq 0 20 40 60 80 100`;
#for j in 0 60;
do
	echo " " > "ResultatSet_Workload/resultat_Workload_Read_$j.txt"
	echo "***** Workload read : $j *****"
	#Nombre de test
	for i in `seq 1 2`
	do
		echo "====================================== Lancement du test SET numero $i ======================================"
		python3 deleteSet.py
		python3 createSystem.py
		#On indique ici avec le premier argument le nombre de process
		./startProgramSet_Workload.sh 2 $j &
		sleep 1m
		kill $!
		python3 readSet.py >> "ResultatSet_Workload/resultat_Workload_Read_$j.txt"
	done
done
