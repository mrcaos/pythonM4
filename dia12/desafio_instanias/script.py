from usuario import Usuario
import json
from datetime import datetime

#paso 1 - > lectura del archivo usuarios.txt
with open('dia12/desafio_Instancias_usuario/usuarios.txt') as usuarios:
    #print("line: ",usuarios.readline())
    linea = usuarios.readline()#  linea = usuarios.readlines()
    #paso 7 -> variable de tipo lista para almacenar los objetos
    lista_objetos_usuarios = []

    #paso 9-> agregar en un ciclo
    while linea:
        #paso 3 -> controlar la excepcion
        try:
            #paso 2 -> transformar el texto en json
            usuario_dicc = json.loads(linea)
            #print("usuario_dicc",usuario_dicc)
            #usuario_dicc {'nombre': 'Page', 'apellido': 'Stappard', 'email': 'pstappard0@java.com', 'genero': 'Bigender'}
            #paso 6 -> Crear instancia de Usuario
            usuario = Usuario(
                            usuario_dicc['nombre'],
                            usuario_dicc['apellido'],
                            usuario_dicc['email'],
                            usuario_dicc['genero'],
                            )
            lista_objetos_usuarios.append(usuario)
        except Exception as error:
            #paso 4 -> imprimir el error
            print(f"el error es:",error)
            #paso 5 -> guardar el error en un log
            now = datetime.now()
            with open(f"{now.strftime('%Y-%m-%d')}_error.log",'a+') as log:
                print(log)
                
                log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {error}\n")
                #log.write(f"Error: {error}\n")
        finally:
            #paso 8 -> posicionar en la siguiente linea
            linea = usuarios.readline() 
    print("")
    print("contenido de la lista",lista_objetos_usuarios)