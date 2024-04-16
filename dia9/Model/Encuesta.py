#!/usr/bin/python
#-*- coding: utf-8 -*-

def __init__(self, nombre: str, preguntas = [], respuestas=[]):
        self.nombre = nombre
        self.__preguntas = [Pregunta(p["enunciado"], p["ayuda"], p["requerida"], p["alternativas"]) for p in preguntas]
        self.__respuestas = respuestas
        
@property
def preguntas(self):
        self.__preguntas
        
@preguntas.setter   
def preguntas(self, preguntas):
        pass
    
@property
def respuestas(self):
        self.__respuestas
        
@respuestas.setter   
def respuestas(self, respuestas):
        pass

def mostrar(self):
        print(f"Encuesta: {self.nombre}")
        print("***Preguntas***")
        for pregunta in self.__preguntas:
            pregunta.mostrar()

