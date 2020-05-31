from cassandra.cluster import Cluster
import sys

def select():
	
	reads = session.execute("""
		SELECT key
		FROM test_set_list_size.table_set
		WHERE ensemble CONTAINS %s
		ALLOW FILTERING
	""", ("90",))
	
	#print (reads[0])
	
def lecture():
	
	reads = session.execute("""
		SELECT ensemble
		FROM test_set_list_size.table_set
	""")
	
	print (len(reads[0][0]))


cluster = Cluster()
session = cluster.connect()

#select()
lecture()

cluster.shutdown()

