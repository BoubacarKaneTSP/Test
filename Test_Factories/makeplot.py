import os
import matplotlib.pyplot as plt
import numpy as np

numprocess = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 25, 30, 40, 50, 60, 70, 80, 90]
#numprocess = [1, 2]

file_set = open("resultat_set.txt","r")
file_list = open("resultat_list.txt","r")
file_counter = open("resultat_counter.txt","r")

resultats_set = file_set.read().split()
resultats_list = file_list.read().split()
resultats_counter = file_counter.read().split()

tmp_set = resultats_set[:len(numprocess)]
tmp_list = resultats_list[:len(numprocess)]
tmp_counter = resultats_counter[:len(numprocess)]



r_set = [int(float(i)/j) for i,j in zip(tmp_set, numprocess)]
r_list = [int(float(i)/j) for i,j in zip(tmp_list, numprocess)]
r_counter = [int(float(i)/j) for i,j in zip(tmp_counter,numprocess)]

for a,b in zip(r_set, numprocess):
    print (a,b)
    
print("r_set: ",r_set)
print("r_list: ",r_list)
print("r_set: ",r_set)

plt.plot(numprocess, r_set, marker = "o", label="Set")
plt.plot(numprocess, r_list, marker = "o", label="List")
plt.plot(numprocess, r_counter, marker = "o", label="Counter")




plt.ylabel("opé/s")
plt.xlabel("# processes")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
#plt.legend(bbox_to_anchor=(1.01, 0.5), loc='upper left', borderaxespad=0.)
#plt.yscale("log")
plt.show()
#plt.savefig("all_results.png"
