from cassandra.cluster import Cluster
import sys

def add(value):

	session.execute("""
	INSERT INTO test_where_contains.table_where (key)
	VALUES (%s)
	""", (value,))

cluster = Cluster()
session = cluster.connect()

numrow = int(sys.argv[1])

for i in range(numrow):
	add(i)
	

cluster.shutdown()
