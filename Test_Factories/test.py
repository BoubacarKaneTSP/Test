from cassandra.cluster import Cluster
import Factories.SetFactory as SFactory
import Factories.ListFactory as LFactory
import Factories.CounterFactory as CFactory
"""
L = LFactory.ListFactory()
DL = L.create_list("CLF","test")
DL.add("a")
DL.add("b")
DL.add("c")
print(DL.read())
DL.add("d")
DL.add("e")
DL.add("f")

L = LFactory.ListFactory()
NS = L.create_list("NLF",0)
NS.add("a")
NS.add("b")
NS.add("c")
NS.add("d")

NS.remove("c")
print(NS.read())

CS = L.create_list("CLF",1)
CS.add(94)
CS.add(93)
CS.add(92)
CS.add(78)

CS.remove(78)

print(CS.read())

CS = L.create_list("CLF",0)
print(CS.read())
print(type(CS))

S = SFactory.SetFactory()
DS = S.create_set("DSF",'0:follower')

DS.add(78)
DS.add(91)
DS.add(92)
DS.add(93)
DS.add(94)

DS.add(78530)
DS.add(91)
DS.add(92000)
DS.add(93270)
DS.add(94380)

DS.remove(91)

print(DS.read())

"""
C = CFactory.CounterFactory()

CC = C.create_counter("CCF","0:test")
CC2 = C.create_counter("CCF","1:test")

CC.increment(1)
CC.increment(2)
CC.increment(3)
CC2.increment(3)
CC2.increment(3)
CC2.increment(3)
CC2.increment(3)

print(CC.read())
print(CC2.read())

