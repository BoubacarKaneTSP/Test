import os
import matplotlib.pyplot as plt
import numpy as np

#numprocess = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
numprocess = [1, 2]

def resultat_set_avg(i):
	
	resultat = open("ResultatSet/resultat_"+str(i)+"_process.txt","r")

	contenu = resultat.read()

	contenu = contenu.split("\n")
	del contenu[0]
	del contenu[len(contenu)-1]

	array = np.array(contenu, dtype="int")
	
	val = ((np.average(array)) / i )/60
	
	return val
	resultat.close()

def resultat_list_avg(i):
	
	resultat = open("ResultatList/resultat_"+str(i)+"_process.txt","r")

	contenu = resultat.read()

	contenu = contenu.split("\n")
	del contenu[0]
	del contenu[len(contenu)-1]

	array = np.array(contenu, dtype="int")

	val = ((np.average(array)) / i )/60
	
	return val
	resultat.close()



resultats_set = []

for i in numprocess:
	resultats_set.append(resultat_set_avg(i))

resultats_set = np.array(resultats_set, dtype="int")

table_set = plt.plot(numprocess, resultats_set, marker = "o", label="Set")



resultats_list = []

for i in numprocess:
	resultats_list.append(resultat_list_avg(i))

resultats_list = np.array(resultats_list, dtype="int")

table_list = plt.plot(numprocess, resultats_list, marker = "o", label = "List")

all_results = np.array([resultats_set, resultats_list])

print(all_results)

plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
#plt.legend(bbox_to_anchor=(1.01, 0.5), loc='upper left', borderaxespad=0.)
#plt.yscale("log")
plt.show()
#plt.savefig("all_results.png"
