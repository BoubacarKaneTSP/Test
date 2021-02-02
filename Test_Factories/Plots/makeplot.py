import os
import matplotlib.pyplot as plt
import numpy as np
import sys

numprocess = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 25, 30, 40]
#numprocess = [1, 5, 10]

files = []
for arg in sys.argv[1:]:
    files.append(open(arg,"r"))

resultats = []

for file in files:
    resultats.append([int(float(i)) for i in file.read().split()[:len(numprocess)]])

print (resultats)

for resultat, name in zip(resultats,sys.argv[1:]):
    plt.plot(numprocess, resultat, marker = "o", label=name[9:len(name)-4].replace("_", " "))
    

"""
file_set = open("resultat_set.txt","r")
file_list = open("resultat_counter_ecriture_same_object.txt","r")
file_counter = open("resultat_counter_ecriture_different_objects.txt","r")

#resultats_set = file_set.read().split()
resultats_list = file_list.read().split()
resultats_counter = file_counter.read().split()

#tmp_set = resultats_set[:len(numprocess)]
tmp_list = resultats_list[:len(numprocess)]
tmp_counter = resultats_counter[:len(numprocess)]



#r_set = [int(float(i)) for i in tmp_set]
r_list = [int(float(i)) for i in tmp_list]
r_counter = [int(float(i)) for i in tmp_counter]
    
#print("r_set: ",r_set)
print("r_list: ",r_list)
print("r_counter: ",r_counter)

#plt.plot(numprocess, r_set, marker = "o", label="Set")
plt.plot(numprocess, r_list, marker = "o", label="List")
plt.plot(numprocess, r_counter, marker = "o", label="Counter")



"""
plt.ylabel("ope/s")
plt.xlabel("# processes")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
#plt.legend(bbox_to_anchor=(1.01, 0.5), loc='upper left', borderaxespad=0.)
#plt.yscale("log")
plt.show()

