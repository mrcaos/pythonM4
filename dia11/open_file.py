import os

#MANIPULAR UN ARCHIVO
log_file = open(os.path.abspath("dia11/logs/error.log"))
#FileNotFoundError: [Errno 2] No such file or 
# directory: 'C:\\python\\M4\\logs\\error.log'

#LECTURA DE UN ARCHIVO EXISTENTE
log_file2 = open(os.path.abspath("dia11/index.html"),"r")
#VER EL CONTENIDO DEL ARCHIVO
print(log_file2.read())
log_file2.close()
print("************************")
#print(log_file2.readline())

print("************************")
with open(os.path.abspath("dia11/index.html"),"r") as archivo:
    print(archivo)
    for linea in archivo:
        print(linea.strip())


#SOLO ESCRITURA
#la ruta donde se creara el archivo debe existir 
log_file4 = open(os.path.abspath("dia11/assets/css/style.css"),"w")