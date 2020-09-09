from .CassandraCounterFactory import CassandraCounterFactory
from .MultipleRowCounterFactory import MultipleRowCounterFactory

class CounterFactory(object):
	
	@classmethod
	def create_counter(self, targetclass, id_count):
		
		if targetclass == "CCF":
			return eval("CassandraCounterFactory(id_count)")
			
		if targetclass == "MRCF":
			return eval("MultipleRowCounterFactory(id_count)")
		
		else:
			raise TypeError("This type of counter do not exists")
