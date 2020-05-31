import os
import sys
import numpy as np


nb_client = int(sys.argv[1])
results = []

resultat = open("Resultats.txt","r")

contenu = resultat.read()

contenu = contenu.split("\n")

contenu = contenu[:len(contenu)-1]


print (contenu)
