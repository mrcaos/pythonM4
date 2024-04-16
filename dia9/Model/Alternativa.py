#!/usr/bin/python
#-*- coding: utf-8 -*-

class Alternativa:
	def __init__(self, contenido: str, ayuda: str):
		self.contenido = contenido
		self.ayuda = ayuda

	def mostrar_alternativa(self):
		print(self.contenido)
		if self.ayuda:
			print("ayuda!!",self.ayuda)	

if __name__ == "__main__":

	dicc = {
	"contenido": "contenidos1",
	"ayuda": "ayudita1"
	},
	
	alternativa = Alternativa(dicc["contenido"],dicc["ayuda"])
