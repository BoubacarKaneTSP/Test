from cassandra.cluster import Cluster
import sys

def add(value):

	session.execute("""
		UPDATE test_set_list_size.table_set
		SET ensemble = ensemble + {%s}
		WHERE key = 0;
	""", (str(value),))

cluster = Cluster()
session = cluster.connect()

borneinf = int(sys.argv[1])
bornesup = int(sys.argv[2])

query = """BEGIN BATCH"""

for i in range(borneinf, bornesup):
	
	query = query + " UPDATE test_set_list_size.table_set SET ensemble = ensemble + {'"+str(i)+"'} WHERE key = 0;"

query = query + " APPLY BATCH"

session.execute(query)


cluster.shutdown()
