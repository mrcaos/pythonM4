class Personaje():
    
    def __init__(self,nombre:str):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0
        
    @property    
    def estado(self):
        return f"""
    nivel:{self.nivel}, experiencia:{self.experiencia}")
    """
    
    @estado.setter
    def estado(self,experiencia:int):
        self.experiencia += experiencia
        a=int(experiencia /100)
        if experiencia >= 100:
            self.nivel += a
            self.experiencia = experiencia -a
            
            
    def __lt__(self,other):
        return self.nivel < other.nivel    
    
    def __gt__(self,other):
        return self.nivel > other.nivel
    
    def __eq__(self,other):
        return self.nivel == other.nivel
    
    def probabilidades(self,other):
        if self < other:
            return 0.33
        elif self > other:
            return 0.66
        else:
            return 0.50
        
    @staticmethod
    def  mostrar_dialogo_opcion(probabilidad_de_ganar):
        return int(input(f"""
                    Con tu nivel actual, tienes {probabilidad_de_ganar*100} de probabilidades de ganarle al Orco.
Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.
Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.

¿Qué deseas hacer?
1. Atacar
2. Huir
                    """))