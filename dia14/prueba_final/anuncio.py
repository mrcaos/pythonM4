from abc import ABC,abstractmethod
from error import SubTipoInvalidoError

class Anuncio(ABC):
    def __init__(self, ancho: int, alto: int, url_archivo: str,
                url_clic: str, sub_tipo: str ) -> None:
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo= url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo= sub_tipo

    #getters
    @property
    def ancho(self):
        return self.__ancho
    @property
    def alto(self):
        return self.__alto
    @property
    def url_archivo(self):
        return self.__url_archivo
    @property
    def url_clic(self):
        return self.__url_clic
    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
    #setter
    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = ancho if ancho > 0 else 1

    @alto.setter
    def alto(self, alto):
        self.__alto = alto if alto > 0 else 1

    @url_archivo.setter
    def url_archivo(self, url_archivo):
        self.__url_archivo = url_archivo

    @url_clic.setter
    def url_clic(self, url_clic):
        self.__url_clic = url_clic

    @sub_tipo.setter
    def sub_tipo(self, sub_tipo):
        try:
            if (isinstance(self,Video) and sub_tipo not in Video.SUB_TIPOS or
            isinstance(self,Display) and sub_tipo not in Display.SUB_TIPOS or
            isinstance(self,Social) and sub_tipo not in Social.SUB_TIPOS) :
                raise SubTipoInvalidoError("No es un subtipos permitidos para las instancias",sub_tipo)
            else:
                self.__sub_tipo = sub_tipo
        except SubTipoInvalidoError as stie:
            print(f"Error:: {stie.mensaje}",stie.subtipo)

    @staticmethod
    def mostrar_formatos():
        print("FORMATO VIDEO:")
        print("==========")
        for video in Video.SUB_TIPOS:
            print(f"-{video}")

        print("FORMATO DISPLAY:")
        print("==========")
        for display in Display.SUB_TIPOS:
            print(f"-{display}")

        print("FORMATO SOCIAL:")
        print("==========")
        for social in Social.SUB_TIPOS:
            print(f"-{social}")

    #METODOS ABSTRACTOS
    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass


class Video(Anuncio):
    FORMATO =  "Video"
    SUB_TIPOS = ("instream","outstream")

    def __init__(self, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int) -> None:
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.__duracion = duracion if duracion > 0 else 5 
    
    @property
    def ancho(self):
        return self.__ancho
    @property
    def alto(self):
        return self.__alto
    
    @ancho.setter
    def ancho(self, ancho):
        pass
    @alto.setter
    def alto(self, alto):
        pass

    @property
    def duracion(self):
        return self.__duracion
    
    @duracion.setter
    def duracion(self, duracion):
        self.__duracion = duracion if duracion > 0 else 5 

    #metodos implementados por herencia
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

video = Video("","","",4)
#video.ancho = 10 #esto no surge efecto, ya que setter no hace nada
video.sub_tipo = "in"

class Display(Anuncio):
    FORMATO =  "Display"
    SUB_TIPOS = ("tradicional","native")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

class Social(Anuncio):
    FORMATO =  "Social"
    SUB_TIPOS = ("facebook","linkedin")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")