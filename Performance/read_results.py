import os
import sys
import numpy as np

def read_result(i):
	resultat = open("Perf/resultat_client_"+str(i)+".txt","r")

	contenu = resultat.read()

	contenu = contenu.split("\n")
	
	return contenu[len(contenu)-2]
	

nb_client = int(sys.argv[1])
results = []

for i in range(nb_client):
	results.append(read_result(i))

array = np.array(results, dtype="int")

total = 0

for i in array:
	total += i
	
#print(total)
	
val = (total / nb_client )/60
print (val)
