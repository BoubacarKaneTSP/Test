from .AbstractList import AbstractList
from cassandra.cluster import Cluster
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.management import create_keyspace_simple
from cassandra.cqlengine.connection import register_connection
from cassandra.cqlengine.connection import set_default_connection

class CList(Model):
    __keyspace__ = 'cassandralist'
    id = columns.Text(primary_key=True)
    ensemble = columns.List(value_type=columns.Text)

class CassandraListFactory(AbstractList):
	
	all_list = {}
	
	def __init__(self, id_list):
		
		self.id = id_list
		
		if not self.all_list: #Check if the dict is empty
			self.connect()
		
		if self.id not in self.all_list:
			self.all_list[self.id] = CList.create(id=self.id)
		
	def add(self, elem):
		self.all_list[self.id].ensemble.append(elem)
		self.all_list[self.id].save()

		
	def remove(self, elem):
		self.all_list[self.id].ensemble.remove(elem)
		self.all_list[self.id].save()
		
	def read(self):
		return self.all_list[self.id].ensemble
		
	def connect(self):
		self.cluster = Cluster(protocol_version=3)
		self.session = self.cluster.connect()
		#self.session.execute("DROP KEYSPACE IF EXISTS cassandralist")
		self.session.execute("CREATE KEYSPACE IF NOT EXISTS cassandralist WITH replication = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 } AND durable_writes = false");
		self.session = self.cluster.connect("cassandralist")
		register_connection(str(self.session), session=self.session)
		set_default_connection(str(self.session))
		
		sync_table(CList)
