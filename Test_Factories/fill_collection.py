import time
import sys
import Factories.SetFactory as SFactory
import Factories.ListFactory as LFactory
import random
import os

c_type = sys.argv[1]
#size = sys.argv[2]

if c_type == "list":
    L = LFactory.ListFactory()
    obj = L.create_list("CLF","test")
else:
    S = SFactory.SetFactory()
    obj = S.create_set("CSF","test")


NBOPERATION = 50000#int(size)
NBOPERATION_p = 0

START = time.time()
ensemble = [10, 100, 1000, 10000, 20000, 30000, 40000, 50000]

while NBOPERATION_p <= NBOPERATION:

    if(NBOPERATION_p in ensemble):
        print(time.time() - START)
              
    obj.add(str(NBOPERATION_p))

    NBOPERATION_p = NBOPERATION_p + 1
