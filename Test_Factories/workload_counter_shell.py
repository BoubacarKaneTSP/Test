import time
import sys
import Factories.CounterFactory as CFactory
import os

C = CFactory.CounterFactory()
obj = C.create_counter("CCF","test"+str(os.getpid()))

NBOPERATION = 1000
NBOPERATION_p = 0


START = time.time()

while NBOPERATION_p < NBOPERATION:
	
	obj.increment(1)
	#obj.read()
	
	NBOPERATION_p = NBOPERATION_p + 1

EXECTIME = time.time() - START

OPESECONDE = NBOPERATION / EXECTIME

print(str(OPESECONDE))

#print(">>>>>>>>>>>" + str(len(obj.read())) + "<<<<<<<<<<<<<<<")

