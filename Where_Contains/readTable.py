from cassandra.cluster import Cluster
import sys

def select():
	
    reads = session.execute("""
        SELECT key
        FROM test_where_contains.table_where
        WHERE following CONTAINS %s
        ALLOW FILTERING
    """, ("0",))
    
    #print (reads[0])


cluster = Cluster()
session = cluster.connect()

select()

cluster.shutdown()

