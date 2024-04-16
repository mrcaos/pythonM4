#!/usr/bin/python
#-*- coding: utf-8 -*-

from Encuesta import Encuesta

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre: str, edad_minima: int, edad_maxima: int, preguntas=[], respuestas=[]):
        super().__init__(nombre, preguntas, respuestas)
        self.__edad_minima = edad_minima
        self.__edad_maxima = edad_maxima
        
    @property
    def edad_minima(self):
        return self.__edad_minima
    
    @edad_minima.setter
    def edad_minima(self, edad_minima):
        self.__edad_minima = edad_minima
        
    @property
    def edad_maxima(self):
        return self.__edad_maxima
    
    @edad_maxima.setter
    def edad_maxima(self, edad_maxima):
        self.__edad_maxima = edad_maxima
        
    def agregar_respuestas(self, respuestas: list, edad_usuario: int):
        if self.edad_minima <= edad_usuario <= self.edad_maxima:
            self.respuestas.append(respuestas)
        else:
            print("La edad del usuario no está dentro del rango permitido para esta encuesta.")

