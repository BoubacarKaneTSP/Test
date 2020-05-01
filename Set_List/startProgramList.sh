#!/bin/bash

# kill all the children of the current process
trap "pkill -KILL -P $$; exit 255" SIGINT SIGTERM

let "numprocess = $1-1"

#Lancement des process
for i in `seq 0 $numprocess`;
do
	echo "Lancement du process $i"
	python3 addList.py &
done

wait
