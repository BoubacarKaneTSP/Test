import os
import matplotlib.pyplot as plt
import numpy as np

#tailleset = [1000, 2000, 3000, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
tailleset = []

for i in range(1000):
	if i != 0:
		
		tailleset.append(i*1000)

def resultat_set_avg(i):
	
	resultat = open("Resultat/resultat_"+str(i)+".txt","r")

	contenu = resultat.read()

	contenu = contenu.split("\n")
	#del contenu[0]
	#del contenu[len(contenu)-1]

	#array = np.array(contenu, dtype="int")
	
	#val = ((np.average(array)) / i )/60
	
	contenu[1] = contenu[1].replace(",",".")
	contenu[1] = contenu[1][7:len(contenu[1])-1]
	print (contenu[1])
	return float(contenu[1])
	resultat.close()

def resultat_list_avg(i):
	
	resultat = open("Resultat/resultat_"+str(i)+".txt","r")

	contenu = resultat.read()

	contenu = contenu.split("\n")
	del contenu[0]
	del contenu[len(contenu)-1]

	array = np.array(contenu, dtype="int")

	val = ((np.average(array)) / i )/60
	
	return val
	resultat.close()



resultats_set = []

for i in tailleset:
	resultats_set.append(resultat_set_avg(i))

resultats_set = np.array(resultats_set, dtype="float")

table_set = plt.plot(tailleset, resultats_set, marker = "o", label="Set")

"""
resultats_list = []

for i in tailleset:
	resultats_list.append(resultat_list_avg(i))

resultats_list = np.array(resultats_list, dtype="int")

table_list = plt.plot(tailleset, resultats_list, marker = "o", label = "List")

all_results = np.array([resultats_set, resultats_list])

print(all_results)
"""
plt.ylabel("runtime")
plt.xlabel("set's size")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
#plt.legend(bbox_to_anchor=(1.01, 0.5), loc='upper left', borderaxespad=0.)
#plt.yscale("log")
plt.xscale("log")
plt.show()
#plt.savefig("all_results.png"
