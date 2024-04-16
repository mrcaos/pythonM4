#!/usr/bin/python
#-*- coding: utf-8 -*-

from Encuesta import Encuesta

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre, regiones, preguntas=[], respuestas=[]):
        super().__init__(nombre, preguntas, respuestas)
        self.__regiones = regiones
        
    @property
    def regiones(self):
        return self.__regiones
    
    @regiones.setter
    def regiones(self, regiones):
        self.__regiones = regiones
        
    def agregar_respuestas(self, respuestas: list, region_usuario: int):
        if region_usuario in self.regiones:
            self.respuestas.append(respuestas)
        else:
            print("La región del usuario no está permitida para esta encuesta.")

