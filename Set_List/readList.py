from cassandra.cluster import Cluster
import sys

def lecture():
	
    reads = session.execute("""
        SELECT ensemble FROM test_set_list.table_list
    """)
    
    print (len(reads[0][0]))


cluster = Cluster()
session = cluster.connect()

lecture()

cluster.shutdown()

