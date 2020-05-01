from cassandra.cluster import Cluster

def add(value):

	session.execute("""
	UPDATE test_set_list.table_list
	SET ensemble = ensemble + [%s]
	WHERE key = 0;
	""", (str(value),))

cluster = Cluster()
session = cluster.connect()

i = 0

while 1:
	add(i)
	i += 1

cluster.shutdown()
