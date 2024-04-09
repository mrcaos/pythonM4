class Coordenada():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        compara_x = self.x == other.x
        compara_y = self.y == other.y
        print(compara_x,compara_y)
        return compara_x and compara_y
                
c1 = Coordenada(-5, 10)
c2 = Coordenada(-5, 10)
# Salida: True
print(c1 == c2)
