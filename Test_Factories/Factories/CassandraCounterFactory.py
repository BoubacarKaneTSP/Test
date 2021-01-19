from .AbstractCounter import AbstractCounter
from cassandra.cluster import Cluster
from cassandra.cqlengine import columns, CQLEngineException
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.management import create_keyspace_simple
from cassandra.cqlengine.connection import register_connection
from cassandra.cqlengine.connection import set_default_connection
import os

class LWTException(CQLEngineException):
	"""Lightweight conditional exception.

	This exception will be raised when a write using an `IF` clause could not be
	applied due to existing data violating the condition. The existing data is
	available through the ``existing`` attribute.

	:param existing: The current state of the data which prevented the write.
	"""
	def __init__(self, existing):
		super(LWTException, self).__init__("LWT Query was not applied")
		self.existing = existing

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
		
		if self.id not in self.all_counter:
			try:
				self.all_counter[self.id] = CCounter.create(id=self.id)
			except LWTException as e:
				#print("The counter already exists", e.existing)
				pass

		
	def increment(self, value):
		self.all_counter[self.id].count+=int(value)
		self.all_counter[self.id].save()
		
	def read(self):
		return self.all_counter[self.id].count
		
	def connect(self):
		self.auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
		self.cluster = Cluster(protocol_version=3,auth_provider=self.auth_provider)
		self.session = self.cluster.connect()
		#self.session.execute("DROP KEYSPACE IF EXISTS cassandracounter")
		self.session.execute("CREATE KEYSPACE IF NOT EXISTS cassandracounter WITH replication = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 } AND durable_writes = false");
		self.session = self.cluster.connect("cassandracounter")
		register_connection(str(self.session), session=self.session)
		set_default_connection(str(self.session))
		
		sync_table(CCounter)
