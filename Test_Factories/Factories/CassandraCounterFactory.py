from .AbstractCounter import AbstractCounter
from cassandra.cluster import Cluster
from cassandra.cqlengine import columns, CQLEngineException
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.management import create_keyspace_simple
from cassandra.cqlengine.connection import register_connection
from cassandra.cqlengine.connection import set_default_connection
from cassandra.auth import PlainTextAuthProvider
from cassandra.cqlengine.query import LWTException
import os

class CCounter(Model):
	__keyspace__ = 'cassandracounter'
	id = columns.Text(primary_key=True)
	count = columns.Counter()

class CassandraCounterFactory(AbstractCounter):
	
	all_counter = {}
	
	def __init__(self, id_counter):
		
		self.id = id_counter
		
		if not self.all_counter: #Check if the dict is empty
			self.connect()
		

		try:
			self.all_counter[self.id] = CCounter.create(id=self.id)
		except LWTException as e:
			self.all_counter[self.id] = CCounter.objects.filter(id=self.id).get()


		
	def increment(self, value):
		self.all_counter[self.id].count+=int(value)
		self.all_counter[self.id].save()
		
	def read(self):
		return self.all_counter[self.id].count
		
	def connect(self):
		if os.getenv('CQLENG_ALLOW_SCHEMA_MANAGEMENT') is None:
			os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = '1'
		self.auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
		self.cluster = Cluster(protocol_version=3,auth_provider=self.auth_provider)
		self.session = self.cluster.connect()
		#self.session.execute("DROP KEYSPACE IF EXISTS cassandracounter")
		self.session.execute("CREATE KEYSPACE IF NOT EXISTS cassandracounter WITH replication = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 } AND durable_writes = false");
		self.session = self.cluster.connect("cassandracounter")
		register_connection(str(self.session), session=self.session)
		set_default_connection(str(self.session))
		
		sync_table(CCounter)
