from cassandra.cluster import Cluster

def createKeyspace(name):
	session.execute("""
		CREATE KEYSPACE IF NOT EXISTS %s
		WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2'}
		""" % name)

def createColumnfamily(name):
	session.execute("""
		CREATE TABLE IF NOT EXISTS %s(
			key int,
			colonne list<int>,
			PRIMARY KEY(key))
	""" % name)

cluster = Cluster()
session = cluster.connect()

keyspace = "test_keyspace"

createKeyspace(keyspace)
session.set_keyspace(keyspace)

createColumnfamily("test_list")


cluster.shutdown()
