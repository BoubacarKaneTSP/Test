import time
import sys
import Factories.SetFactory as SFactory
import Factories.ListFactory as LFactory
import random
import os

c_type = sys.argv[1]
size = sys.argv[2]

if c_type == "list":
    L = LFactory.ListFactory()
    obj = L.create_list("CLF","test")
else:
    S = SFactory.SetFactory()
    obj = S.create_set("CSF","test")


NBOPERATION = int(size)
NBOPERATION_p = 0

START = time.time()

while NBOPERATION_p < NBOPERATION:

    obj.add(str(NBOPERATION_p+2000000))

    NBOPERATION_p = NBOPERATION_p + 1

EXECTIME = time.time() - START

print(str(EXECTIME))