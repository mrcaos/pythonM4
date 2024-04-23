from datetime import date

class Campania():
    def __init__(self,nombre: str, fecha_inicio: date, fecha_termino: date, anuncios: list) -> None:
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios =[self.__instancia_de_anuncios(dicc)  for dicc in anuncios  ]
        # self.__anuncios =[Video, Video, Display, Social]
    #[{},{},{}]

    def __instancia_de_anuncios(self,anuncio: dict):
        
        #return Video()
        #return Social()
        #return Display()
        pass
    
    def contar_anuncios(self):
        contador = {"Video": 0, "Display": 0, "Social": 0}
        for anuncio in self.__anuncios:
            if isinstance(anuncio, Video):
                contador["Video"] += 1
            elif isinstance(anuncio, Display):
                contador["Display"] += 1
            elif isinstance(anuncio, Social):
                contador["Social"] += 1
        return ", ".join([f"{value} {key}" for key, value in contador.items()])