from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect()
session.set_keyspace("cc_counter")

def reset():
	
	session.execute(""" DROP TABLE IF EXISTS cc """)
	
	session.execute("""
				CREATE TABLE IF NOT EXISTS cc_counter.cc(
					key int,
					registre counter,
					PRIMARY KEY(key))
			""")
			
def add():
	
	session.execute("""
				UPDATE cc
				SET registre = registre + 1
				WHERE key = 0;
			""")


reset()

val = 0

while val < 10000:
	add()
	val = val + 1



cluster.shutdown()

