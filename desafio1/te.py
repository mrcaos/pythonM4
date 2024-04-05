class Te:
    
    #Precios de los productos y Datos de los tipos de producto entregados de forma estructurada en un diccionario.
    precios = {"300gr": 3000, "500gr":5000 }
    datosTe = {
        "té negro": {
            "tiempo_preparacion": 3,
            "recomendacion": "Se recomienda consumir al desayuno."
        },
        "té verde": {
            "tiempo_preparacion": 5,
            "recomendacion": "Se recomienda consumir al medio día."
        },
        "agua de hierbas": {
            "tiempo_preparacion": 6,
            "recomendacion": "Se recomienda consumir al atardecer."
        }
    }
    
    #Metodo Estatico que bueca segun el N°ingresado correspondite al sabor,el tipo de sabor, el tiempo de preparacion y la recomendacion de cada producto.
    @staticmethod
    def tiempo_prep(sabor):
        if  sabor == 1:
            nombre= "té negro"
            tiempo= Te.datosTe.get("té negro").get("tiempo_preparacion")
            recomendacion= Te.datosTe.get("té negro").get("recomendacion")
        elif sabor == 2:
            nombre= "té verde"
            tiempo= Te.datosTe.get("té verde").get("tiempo_preparacion")
            recomendacion= Te.datosTe.get("té verde").get("recomendacion")
        elif sabor == 3:
            nombre = "agua de hierbas"
            tiempo= Te.datosTe.get("agua de hierbas").get("tiempo_preparacion")
            recomendacion= Te.datosTe.get("agua de hierbas").get("recomendacion")    
        return tiempo,recomendacion,nombre
    
    #Metodo estatico que busca el precio dependiendo del formato que se busque
    @staticmethod
    def obtener_precio(valor):
        if valor == 300:
            formato="300gr"
            p_var=Te.precios.get("300gr")
        elif valor == 500:
            formato="500gr"
            p_var=Te.precios.get("500gr")
        return p_var,formato