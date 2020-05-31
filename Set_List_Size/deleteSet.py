from cassandra.cluster import Cluster

def deleteSet():
	session.execute("""
		DROP TABLE test_set_list_size.table_set
	""")

cluster = Cluster()
session = cluster.connect()

deleteSet()

cluster.shutdown()
