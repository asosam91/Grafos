#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np 
class Dijkstra:

	def __init__(self,lAristas = [],Nodos = {}):
		self.__lAristas = lAristas
		self.__Nodos = Nodos

	def algoritmo(self):
		setGrafo()
		#while getNodosNoEvaluados() > 0:


	def getNodosNoEvaluados(self, NoEvaluados = 0):
		if self.__Nodos:
			for p in self.__Nodos:
				if not self._Nodos[p].getFueEvaluado():
					NoEvaluados += 1
		return NoEvaluados

	def getNodoSource(Nodo, source = None):
		if self.__Nodos:
			for p in self.__Nodos:
				if self.__Nodos.getEsSource():
					source = self.__Nodos[p]
		return source
