from cassandra.cluster import Cluster

def deleteSet():
	session.execute("""
		DROP TABLE test_set_list.table_list
	""")

cluster = Cluster()
session = cluster.connect()

deleteSet()

cluster.shutdown()
