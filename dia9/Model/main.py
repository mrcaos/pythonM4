from encuesta import Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion
from usuario import Usuario
from listaDeRespuesta import ListaDeRespuesta
from preguntas import preguntas_simple, respuestas_simple

# usuarios
usuario1 = Usuario("usuario1@example.com", 25, 1)
usuario2 = Usuario("usuario2@example.com", 35, 2)

# encuesta simple
encuesta_simple = Encuesta("Encuesta de satisfacción", preguntas_simple)
encuesta_simple.mostrar()

# encuesta limitada por edad
encuesta_edad = EncuestaLimitadaEdad("Encuesta de edad", 18, 60, preguntas_simple)
encuesta_edad.mostrar()

# encuesta limitada por región
encuesta_region = EncuestaLimitadaRegion("Encuesta de región", [1, 2], preguntas_simple)
encuesta_region.mostrar()

# listado de respuestas para la encuesta simple
listado_respuestas_simple = ListadoRespuestas(usuario1, respuestas_simple)
print("Respuestas de usuario 1:")
for respuesta in listado_respuestas_simple.respuestas:
    print(f"Pregunta {respuesta['pregunta'] + 1}: Alternativa {respuesta['alternativa'] + 1}")