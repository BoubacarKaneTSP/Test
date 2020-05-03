#!/bin/bash

# kill all the children of the current process
trap "pkill -KILL -P $$; exit 255" SIGINT SIGTERM

./testSet_Workload.sh
./testList_Workload.sh

wait
