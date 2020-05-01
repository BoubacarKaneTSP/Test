#!/bin/bash

#kill all the children of the current process
trap "pkill -KILL -P $$; exit 255" SIGINT SIGTERM

#Nombre de process
#for i in 1 2 3 4 5 6 7 8 9 10 12 14 16 18 20 25 30 35 40 45 50 55 60 65 70 75 80;
for i in 1 2;
do
	./testList.sh $i
	
done

wait
