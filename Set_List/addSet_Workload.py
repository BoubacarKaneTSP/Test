from cassandra.cluster import Cluster
import sys
from random import seed
from random import randint


def add(value):

	session.execute("""
	UPDATE test_set_list.table_set
	SET ensemble = ensemble + {%s}
	WHERE key = 0;
	""", (str(value),))

def lecture():
	
    reads = session.execute("""
        SELECT ensemble FROM test_set_list.table_set
    """)
    
cluster = Cluster()
session = cluster.connect()

perc_read = int(sys.argv[1])

i = 0
task = 0

while 1:
	task = randint(0,100)
#	print (task)
	if task < perc_read:
		lecture()
#		print ("Lecture")
	else:
		add(i)
#		print ("Ecriture")
	
	i += 1
cluster.shutdown()
