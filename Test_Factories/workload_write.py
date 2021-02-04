from cassandra.cluster import Cluster
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.management import create_keyspace_simple
from cassandra.cqlengine.connection import register_connection
from cassandra.cqlengine.connection import set_default_connection
from cassandra.auth import PlainTextAuthProvider
from cassandra.cqlengine.query import LWTException
import time
import sys
import random
import os

class Registre(Model):
    __keyspace__ = 'cassandraset'
    id = columns.Text(primary_key=True)
    value = columns.Text()
    
    
if os.getenv('CQLENG_ALLOW_SCHEMA_MANAGEMENT') is None:
    os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = '1'
auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
cluster = Cluster(protocol_version=3,auth_provider=auth_provider)
session = cluster.connect()
session.execute("CREATE KEYSPACE IF NOT EXISTS registre WITH replication = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 } AND durable_writes = false");
session = cluster.connect("registre")
register_connection(str(session), session=session)
set_default_connection(str(session))

sync_table(Registre)

obj = Registre.if_not_exists().create(id=str(os.getpid()))

NBOPERATION = 50000
NBOPERATION_p = 0

ensemble = [10, 100, 1000, 10000, 20000, 30000, 40000, 50000]

START = time.time()

while NBOPERATION_p <= NBOPERATION:

    obj.update(value="test")
    
    if(NBOPERATION_p in ensemble):
        print(time.time() - START)

    NBOPERATION_p = NBOPERATION_p + 1

