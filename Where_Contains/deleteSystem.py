from cassandra.cluster import Cluster

def delete():
	session.execute("""
		DROP TABLE test_where_contains.table_where
	""")

cluster = Cluster()
session = cluster.connect()

delete()

cluster.shutdown()
