from .DegradedListFactory import DegradedListFactory
from .NormalListFactory import NormalListFactory
from .CassandraListFactory import CassandraListFactory

class ListFactory(object):
	
	@classmethod
	def create_list(self, targetclass, id_list):

		if targetclass == "DLF":
			return eval("DegradedListFactory(id_list)")
			
		if targetclass == "NLF":
			return eval("NormalListFactory(id_list)")
			
		if targetclass == "CLF":
			return eval("CassandraListFactory(id_list)")

