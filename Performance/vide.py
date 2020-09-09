import matplotlib
#matplotlib.use('Agg')

from scipy.stats import powerlaw
import matplotlib.pyplot as plt
import numpy as np
import powerlawmaster.powerlaw as powerlaw
from collections import Counter

a, xmin = 1.35, 1.0
N = 100000

# generates random variates of power law distribution
vrs = powerlaw.Power_Law(xmin=xmin, parameters=[a]).generate_random(N)


"""
# plotting the PDF estimated from variates
bin_min, bin_max = np.min(vrs), np.max(vrs)
bins = 10**(np.linspace(np.log10(bin_min), np.log10(bin_max), 100))
counts, edges = np.histogram(vrs, bins, density=True)
centers = (edges[1:] + edges[:-1])/2.


	
# plotting the expected PDF 
xs = np.linspace(bin_min, bin_max, 100000)
plt.plot(xs, [(a-1)*xmin**(a-1)*x**(-a) for x in xs], color='red')
plt.plot(centers, counts, '.')

#plt.xscale('log')
#plt.yscale('log')
c=[]
for x in centers:
	#c.append(round(int(x),0))
	c.append(int(x))
	
m = Counter(c).most_common(100)
"""
#plt.xscale('log')
#plt.yscale('log')
r=[]
for x in vrs:
	r.append(round(int(x),-1))

mr = Counter(r).most_common(100)
print(len(r))

s=[]
v=[]
for i in range(100):
	print(mr[i][1])
	print(mr[i][0])
	v.append(mr[i][0])
	s.append(mr[i][1])

table_list = plt.plot(v, s, marker = "o", label = "List")
#print(m)
#print(counts)
plt.show()
"""
a = 1.35

r = powerlaw.rvs(a, loc=0, scale=100, size=10000000)

c=[]
for x in r:
	c.append(round(int(x),-1))


m = Counter(c).most_common(100)
s=[]
v=[]
print(m)
for i in range(10):
	#print(m[i][1])
	#print(m[i][0])
	v.append(m[i][0])
	s.append(m[i][1])

table_list = plt.plot(v, s, marker = "o", label = "List")


plt.show()

"""
"""
mean, var, skew, kurt = powerlaw.stats(a, moments='mvsk')

print (mean, var, skew, kurt)
print (powerlaw.ppf(0.01, a))
print (powerlaw.ppf(0.99, a))
x = np.linspace(powerlaw.ppf(0.01, a), powerlaw.ppf(0.99, a), 100)
print (x)

table_list = plt.plot(x, powerlaw.pdf(x, a),'r-', lw=5, alpha=0.6, label='powerlaw pdf')
plt.show()
"""

"""
x = np.linspace(powerlaw.ppf(0.01, a), powerlaw.ppf(0.99, a), 100)
ax.plot(x, powerlaw.pdf(x, a), 'r-', lw=5, alpha=0.6, label='powerlaw pdf')


r = powerlaw.rvs(a, size=1000)

print (len(r))

table_list = plt.plot(r, marker = "o", label = "List")
plt.yscale("log")
plt.show()
"""

"""
debut = time.time()

fic = open("resultat_client_"+str(NUMCLIENT)+".txt","w")

nbope = 0
while time.time() - debut <= 60:
	nbope = nbope + 1
	fic.write(str(nbope)
	
print (nbope)
	
fic.close()
"""

