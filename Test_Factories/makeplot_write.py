import os
import matplotlib.pyplot as plt
import numpy as np
import sys

numwrites = [10, 100, 1000, 10000, 20000, 30000, 40000, 50000]

files = []
for arg in sys.argv[1:]:
    files.append(open(arg,"r"))

resultats = []

for file in files:
    resultats.append([int(float(i)) for i in file.read().split()[:len(numwrites)]])

print (resultats)

for resultat, name in zip(resultats,sys.argv[1:]):
    plt.plot(numwrites, resultat, marker = "o", label=name[9:len(name)-4].replace("_", " "))
    
plt.ylabel("ope/s")
plt.xlabel("# processes")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
plt.show()