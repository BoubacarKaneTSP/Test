import time
import sys
import Factories.ListFactory as LFactory

L = LFactory.ListFactory()
obj = L.create_list("CLF","test")

NBOPERATION = 10000
NBOPERATION_p = 0

START = time.time()

while NBOPERATION_p < NBOPERATION:

	obj.add("1")

	NBOPERATION_p = NBOPERATION_p + 1

EXECTIME = time.time() - START

OPESECONDE = NBOPERATION / EXECTIME

print(str(OPESECONDE))

#print(">>>>>>>>>>>" + str(len(obj.read())) + "<<<<<<<<<<<<<<<")