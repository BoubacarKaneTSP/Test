#!/bin/bash

# kill all the children of the current process
trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT
trap "pkill -KILL -P $$; exit 255" SIGINT SIGTERM

let "NBITERATION=$1-1"

for i in `seq 0 $NBITERATION`
do
	echo "Lancement du client numero : $i"
	./workload.sh $i &
done

sleep 1m
kill $!

echo "Fin du test"
