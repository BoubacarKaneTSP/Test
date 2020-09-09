import time
import threading
import sys
import Factories.CounterFactory as CFactory

C = CFactory.CounterFactory()
obj = C.create_counter("CCF","test")
NBOPERATION = 10000

def work():
	NBOPERATION_p = 0

	while NBOPERATION_p < NBOPERATION:

		obj.increment(1)

		NBOPERATION_p = NBOPERATION_p + 1
	
nb_process = int(sys.argv[1])
processes = []

START = time.time()

for _ in range(nb_process):
	
	p = threading.Thread(target=work)
	p.start()
	processes.append(p)

for process in processes:
	process.join()
	

EXECTIME = time.time() - START

OPESECONDE = NBOPERATION*nb_process / EXECTIME

print(str(OPESECONDE))

print(">>>>>>>>>>>" + str(obj.read()) + "<<<<<<<<<<<<<<<")

