from .AbstractSet import AbstractSet
from cassandra.cluster import Cluster
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.management import create_keyspace_simple
from cassandra.cqlengine.connection import register_connection
from cassandra.cqlengine.connection import set_default_connection
import os

class DSet(Model):
	__keyspace__ = 'degradedset'
	id_set = columns.Text(primary_key=True)
	id_writer = columns.Text(partition_key=True)
	ensemble = columns.Set(value_type=columns.Integer)

class DegradedSetFactory(AbstractSet):

	all_set = {}

	def __init__(self, id_proc): # Connect to cassandra

		self.id = id_proc

		if not self.all_set: #Check if the dict is empty
			self.connect()

		if self.id not in self.all_set:
			self.all_set[self.id] = DSet.create(id_set=self.id, id_writer=str(os.getpid()))

	def add(self, elem):

		self.all_set[self.id].ensemble.add(elem)
		self.all_set[self.id].save()

	def remove(self, elem):
		self.all_set[self.id].ensemble.remove(elem)
		self.all_set[self.id].save()

	def read(self):
		
		total = set()
		for q in DSet.objects(DSet.id_set == self.id).allow_filtering().all():
			total = total.union(q.ensemble)
		
		return sorted(total)
		
	def connect(self):
		self.cluster = Cluster(protocol_version=3)
		self.session = self.cluster.connect()
		#self.session.execute("DROP KEYSPACE IF EXISTS degradedset")
		self.session.execute("CREATE KEYSPACE IF NOT EXISTS degradedset WITH replication = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 } AND durable_writes = false");
		self.session = self.cluster.connect("degradedset")
		register_connection(str(self.session), session=self.session)
		set_default_connection(str(self.session))

		sync_table(DSet)
