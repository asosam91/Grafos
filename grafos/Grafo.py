#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

class Grafo:
	def __init__(self, nodos):
		self.__adyacencia = np.zeros((nodos,nodos))
		#self.__n = nodos

	def addArco(self, nodo1, nodo2):
		self.__adyacencia[nodo1][nodo2] = 1
		self.__adyacencia[nodo2][nodo1] = 1

	def removeArco(self, nodo1, nodo2):
		self.__adyacencia[nodo1][nodo2] = 0
		self.__adyacencia[nodo2][nodo1] = 0

	def getGrafo(self):
		return self.__adyacencia