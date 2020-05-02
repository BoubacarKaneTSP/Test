from cassandra.cluster import Cluster
import sys

def follow(id_user, id_to_follow):
	
	session.execute("""
		UPDATE test_where_contains.table_where SET following = following + {%s} WHERE key = %s
	""", (str(id_to_follow), id_user))
	
	

cluster = Cluster()
session = cluster.connect()

id_user = int(sys.argv[1])
id_to_follow = int(sys.argv[2])

follow(id_user, id_to_follow)

cluster.shutdown()
