from cassandra.cluster import Cluster

def createKeyspace(name):
	session.execute("""
		CREATE KEYSPACE IF NOT EXISTS %s
		WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '1'}
		""" % name)

def createColumnfamily_set(name):
	session.execute("""
		CREATE TABLE IF NOT EXISTS %s(
			key int,
			following set<text>,
			PRIMARY KEY(key)
		)
	""" % name)
	

cluster = Cluster()
session = cluster.connect()

keyspace = "test_where_contains"

createKeyspace(keyspace)
session.set_keyspace(keyspace)

createColumnfamily_set("table_where")


cluster.shutdown()
