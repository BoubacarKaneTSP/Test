from .AbstractSet import AbstractSet
from cassandra.cluster import Cluster
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.management import create_keyspace_simple
from cassandra.cqlengine.connection import register_connection
from cassandra.cqlengine.connection import set_default_connection
from cassandra.auth import PlainTextAuthProvider
from cassandra.cqlengine.query import LWTException
import os

class CSet(Model):
    __keyspace__ = 'cassandraset'
    id = columns.Text(primary_key=True)
    ensemble = columns.Set(value_type=columns.Text)

class CassandraSetFactory(AbstractSet):
    
    all_set = {}
    
    def __init__(self, id_test):
        
        self.id = id_test
        
        if not self.all_set: #Check if the dict is empty
            self.connect()
            
        #if self.id not in self.all_set:
        try:
            self.all_set[self.id] = CSet.if_not_exists().create(id=self.id)
        except LWTException as e:
            self.all_set[self.id] = CSet.objects.filter(id=self.id).get()
    
    def add(self, elem):
        #print("add " + str(elem) + " in:", self.all_set[self.id].ensemble)
        #print(CSet.objects(id=self.id), "|",self.all_set[self.id].ensemble, self.id)
        #self.all_set[self.id].update(ensemble__add={str(elem)})
        CSet.objects(id=self.id).update(ensemble__add={str(elem)})
        #self.all_set[self.id].ensemble = self.all_set[self.id].ensemble.union({str(elem)})
        self.all_set[self.id].save()

    def remove(self, elem):
        self.all_set[self.id].ensemble.remove(str(elem))
        self.all_set[self.id].save()

    def read(self):
        return self.all_set[self.id].ensemble

    def connect(self):
        if os.getenv('CQLENG_ALLOW_SCHEMA_MANAGEMENT') is None:
            os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = '1'
        self.auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
        self.cluster = Cluster(protocol_version=3,auth_provider=self.auth_provider)
        self.session = self.cluster.connect()
        #self.session.execute("DROP KEYSPACE IF EXISTS cassandraset")
        self.session.execute("CREATE KEYSPACE IF NOT EXISTS cassandraset WITH replication = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 } AND durable_writes = false");
        self.session = self.cluster.connect("cassandraset")
        register_connection(str(self.session), session=self.session)
        set_default_connection(str(self.session))
        
        sync_table(CSet)
