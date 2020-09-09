from abc import abstractmethod, ABCMeta

class AbstractList(metaclass=ABCMeta):
	
	def __init__(self):
		self.all_list = {}
		
	@abstractmethod	
	def add(self, *args):
		pass
		
	@abstractmethod
	def remove(self, elem):
		pass
	
	@abstractmethod
	def read():
		pass
