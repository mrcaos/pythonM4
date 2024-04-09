class Celular():
    def __init__(self, tamanio = 0):
        self.tamanio = tamanio 
        
android = Celular(16)
iphone = Celular(16)

print(android) #<__main__.Celular object at 0x000002792709E610>
print(iphone) #<__main__.Celular object at 0x000001815859ED50>
print(android == iphone) #FALSE

windowp = android
print(windowp) #<__main__.Celular object at 0x000002792709E610>
