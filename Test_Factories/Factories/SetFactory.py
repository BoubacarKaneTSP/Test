from .DegradedSetFactory import DegradedSetFactory
from .NormalSetFactory import NormalSetFactory
from .CassandraSetFactory import CassandraSetFactory

class SetFactory(object):
	
	@classmethod
	def create_set(self, targetclass, id_set):
		if targetclass == "NSF":
			return eval("NormalSetFactory(id_set)")
			
		if targetclass == "DSF":
			return eval("DegradedSetFactory(id_set)")
			
		if targetclass == "CSF":
			return eval("CassandraSetFactory(id_set)")
		
