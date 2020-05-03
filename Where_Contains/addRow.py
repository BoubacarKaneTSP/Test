from cassandra.cluster import Cluster
import sys

def add(value):

	session.execute("""
	INSERT INTO test_where_contains.table_where (key)
	VALUES (%s)
	""", (value,))

cluster = Cluster()
session = cluster.connect()

borneinf = int(sys.argv[1])
bornesup = int(sys.argv[2])


for i in range(borneinf, bornesup):
	add(i)
	

cluster.shutdown()
