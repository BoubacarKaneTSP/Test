from cassandra.cluster import Cluster
import Factories.CounterFactory as CFactory
import Factories.SetFactory as SFactory
import Factories.ListFactory as LFactory
from cassandra.auth import PlainTextAuthProvider
import os

if os.getenv('CQLENG_ALLOW_SCHEMA_MANAGEMENT') is None:
    os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = '1'

auth = PlainTextAuthProvider(username='cassandra', password='cassandra')
cluster = Cluster(protocol_version=3,auth_provider=auth)
session = cluster.connect()

session.execute("""DROP KEYSPACE IF EXISTS multiplerowcounter""")
session.execute("""DROP KEYSPACE IF EXISTS degradedlist""")
session.execute("""DROP KEYSPACE IF EXISTS degradedset""")
session.execute("""DROP KEYSPACE IF EXISTS cassandracounter""")
session.execute("""DROP KEYSPACE IF EXISTS cassandralist""")
session.execute("""DROP KEYSPACE IF EXISTS cassandraset""")

C = CFactory.CounterFactory()
obj = C.create_counter("CCF","test")

S = SFactory.SetFactory()
obj = S.create_set("CSF","test")

L = LFactory.ListFactory()
obj = L.create_list("CLF","test")