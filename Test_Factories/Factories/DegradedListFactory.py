from .AbstractList import AbstractList
from cassandra.cluster import Cluster
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.management import create_keyspace_simple
from cassandra.cqlengine.connection import register_connection
from cassandra.cqlengine.connection import set_default_connection
from cassandra.auth import PlainTextAuthProvider
import Factories.CounterFactory as CFactory
import Factories.MultipleRowCounterFactory as MRCFactory

import os

class DList(Model):
	__keyspace__ = 'degradedlist'
	id_list = columns.Text(primary_key=True)
	id_writer = columns.Text(partition_key=True)
	ensemble = columns.List(value_type=columns.Text)

class DegradedListFactory(AbstractList):

	all_list = {}
	last_read = list()
	
	def __init__(self, id_new_list): # Connect to cassandra

		self.id = id_new_list

		if not self.all_list: #Check if the dict is empty
			self.connect()

		if self.id not in self.all_list:
			C = CFactory.CounterFactory()
			self.Count = C.create_counter("CCF",self.id)
			self.all_list[self.id] = DList.create(id_list=self.id, id_writer=str(os.getpid()))

	def add(self, elem):
		
		tmp = self.Count.read()	
		self.Count.increment(1)
		self.all_list[self.id].ensemble.append(str(tmp)+":"+str(elem))
		self.all_list[self.id].save()

	def remove(self, elem):
		self.all_list[self.id].ensemble.remove(elem)
		self.all_list[self.id].save()

	def read(self):
		
		new_read = list()
		result = list()
		values = list()
		
		for q in DList.objects(DList.id_list == self.id).allow_filtering().all():
			for tmp in q.ensemble:
				tmp_tuple = tmp.split(":")
				new_read.append(list(tmp_tuple))
		
		result = self.last_read + sorted([ele for ele in new_read if ele not in self.last_read])
		self.last_read = result
		
		values = [ele[1] for ele in result]
		return (values)
		
	def connect(self):
		self.auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
		self.cluster = Cluster(protocol_version=3,auth_provider=self.auth_provider)
		self.session = self.cluster.connect()
		#self.session.execute("DROP KEYSPACE IF EXISTS degradedlist")
		self.session.execute("CREATE KEYSPACE IF NOT EXISTS degradedlist WITH replication = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 } AND durable_writes = false");
		self.session = self.cluster.connect("degradedlist")
		register_connection(str(self.session), session=self.session)
		set_default_connection(str(self.session))

		sync_table(DList)
