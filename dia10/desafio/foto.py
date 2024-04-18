from error import DimensionError

class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        self.ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, nuevo_ancho: int) -> None:
        if nuevo_ancho < 1 or nuevo_ancho > Foto.MAX:
            raise DimensionError("Valor de ancho inválido", "ancho", Foto.MAX)
        self.__ancho = nuevo_ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, nuevo_alto: int) -> None:
        if nuevo_alto < 1 or nuevo_alto > Foto.MAX:
            raise DimensionError("Valor de alto inválido", "alto", Foto.MAX)
        self.__alto = nuevo_alto

try:
    foto = Foto(1000, 1500, "imagen.jpg")
    foto.ancho = 50
    foto.alto = 3000
except DimensionError as error:
    print(f"Error: {error}")