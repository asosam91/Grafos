import math
import numpy as np 

class Nodo:
	## este es el constructor donde se definen las variables privadas
	def __init__(self, key,esSource = False, fueEvaluado=False, keyNodoPadre="",acum= math.inf ):
		self.__key = key
		self.__esSource = esSource
		self.__fueEvaluado = fueEvaluado
		self.__keyNodoPadre = keyNodoPadre
		self.__acum = acum

	## getters y setters
	def getKey(self):
		return self.__key

	def setKey(self, key):
		self.__key = key

	def getEsSource(self):
		return self.__esSource

	def setEsSource(self, esSource):
		self.__esSource = esSource

	def getFueEvaluado(self):
		return self.__fueEvaluado

	def setFueEvaluado(self, fueEvaluado):
		self.__fueEvaluado = fueEvaluado

	def getKeyNodoPadre(self):
		return self.__keyNodoPadre

	def setKeyNodoPadre(self, keyNodoPadre):
		self.__keyNodoPadre = keyNodoPadre

	def getAcum(self):
		return self.__acum

	def setAcum(self, acum):
		self.__acum = acum

class Grafo:
	def __init__(self, nodos):
		self.__adyacencia = np.zeros((nodos,nodos))
		self.__n = nodos

	def addArco(self, nodo1, nodo2):
		self.__adyacencia[nodo1][nodo2] = 1
		self.__adyacencia[nodo2][nodo1] = 1

	def removeArco(self, nodo1, nodo2):
		self.__adyacencia[nodo1][nodo2] = 0
		self.__adyacencia[nodo2][nodo1] = 0

	def __str__(self):
		return self.__adyacencia