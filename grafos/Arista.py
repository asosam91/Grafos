class Arista:
	def __init__(self, kn1, kn2, cost):
		self.__keyN1 = kn1
		self.__keyN2 = kn2
		self.__costo = cost

	def getKeyN1(self):
		return self.__keyN1

	def getKeyN2(self):
		return self.__keyN2

	def getCosto(self):
		return self.__costo

	def setKeyN1(self, keyN1):
		self.__keyN1 = keyN1

	def setKeyN2(self, keyN2):
		self.__keyN2 =  keyN2

	def setCosto(self, costo):
		self.__costo = costo