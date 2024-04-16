#!/usr/bin/python
#-*- coding: utf-8 -*-

from Alternativa import Alternativa

class Pregunta:
	def __init__(self, enunciado:str, ayuda: str, requerido: bool, alternativas: list):
		self.enunciado = enunciado
		self.ayuda = ayuda
		self.requerido = requerido
		#Considera que las alternativas son entregadas como una lista de diccionarios.
		self.__alternativas = [
			Alternativa(dicc["contenido"],dicc["ayuda"]) for dicc in alternativas
		]

	def mostrar_pregunta(self, ):
		print(self.enunciado)
		
		if self.ayuda:
			print("ayuda!!",self.ayuda)
			
		for obj_alter in self.__alternativas:
			print(obj_alter.mostrar_alternativa())


if __name__ == "__main__":

	alternativas = [
		{
		"contenido": "contenidos1",
		"ayuda": "ayudita1"
		},
		{
		"contenido": "contenidos2",
		"ayuda": "ayudita2"
		},
		{
		"contenido": "contenidos3",
		"ayuda": "ayudita3"
		}
	]

	pregunta= Pregunta("enunciado1", "ayuda1",True,alternativas)

	for dicc in alternativas:
		print(dicc)

