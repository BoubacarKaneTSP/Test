import time
import sys
import Factories.SetFactory as SFactory
import random
#import os

S = SFactory.SetFactory()
obj = S.create_set("CSF","test")

NBOPERATION = 1000
NBOPERATION_p = 0

#obj.add("1")

START = time.time()

while NBOPERATION_p < NBOPERATION:

	obj.add(str(random.randint(0,100000)))
	#obj.read()
	NBOPERATION_p = NBOPERATION_p + 1

EXECTIME = time.time() - START

OPESECONDE = NBOPERATION / EXECTIME

print(str(OPESECONDE))

#print(">>>>>>>>>>>" + str(len(obj.read())) + "<<<<<<<<<<<<<<<")
