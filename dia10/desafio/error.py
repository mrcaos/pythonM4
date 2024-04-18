class DimensionError(Exception):
    
    def __init__(self, mensaje: str, dimension: str = None, maximo: int = None):
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo
    
    def __str__(self):
        if self.mensaje is None:
            return Exception.__str__(self)
        else:
            return f"""
            {self.mensaje}: 
            {self.dimension} debe ser entre 1 y {self.maximo}
            """