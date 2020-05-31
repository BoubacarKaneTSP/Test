from cassandra.cluster import Cluster
import sys

def lecture():
	
	reads = session.execute("""
		SELECT ensemble FROM test_set_list.table_list
	""")

	new_list = []
	
	for item in reads[0][0]:
		new_list.append(int(item))

	#print (len(new_list))
	print (max(new_list))


cluster = Cluster()
session = cluster.connect()

lecture()

cluster.shutdown()

