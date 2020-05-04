#!/bin/bash

#kill all the children of the current process
trap "pkill -KILL -P $$; exit 255" SIGINT SIGTERM

RANDOM=$$

python3 createSystem.py

for i in `seq $1 $2`;
do
	DIV=$((($3*1)/100))
	
	for j in `seq 1 $DIV`;
	do
		PROCESS=$(($RANDOM%$3))
		#echo "process --> $i <-- va follow le process --> $PROCESS <-- "
		python3 follow_user.py $i $PROCESS
	done
done
