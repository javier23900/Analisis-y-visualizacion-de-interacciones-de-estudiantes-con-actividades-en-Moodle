from Clases_Botones import *

'''
def cargar_ficheros(diccionario_tema, diccionario_fecha, diccionario_estudiantes): Función encargada de generar la 
opción de selección de los ficheros con la información de los test realizados por los estudiantes.

    - Argumentos:
    
        - diccionario_tema: Diccionario con los test realizados por los estudiantes. La clave del 
        diccionario es el tema al que pertenecen los test y para cada clave su valor es un array que contiene un conjunto de 
        arrays con los test realizados por los estudiantes.
        
        - diccionario_fecha: Diccionario con los test realizados por los estudiantes. La clave del 
        diccionario es la fecha en la que se realizó el test y para cada clave su valor es un array que contiene un conjunto 
        de arrays con los test de cada tema realizados por los estudiantes en dicha fecha.
        
        - diccionario_estudiantes: Diccionario con los estudiantes y sus test realizados. La clave del 
        diccionario es el identificador del estudiante y para cada clave su valor es un diccionario con los test. Este segundo 
        diccionario tiene como clave el tema al que pertenecen los test y para cada clave su valor es un array que contiene 
        los test realizados por los estudiantes.
'''


def cargar_ficheros(diccionario_tema, diccionario_fecha, diccionario_estudiantes):
    text = "LECTURA DE DATOS"
    titulo = widgets.HTML(value=f"<b>{text}</b>")
    display(titulo)

    p = widgets.Label(value="AVISO: Los ficheros se cargan desde la raíz de la carpeta.")
    display(p)
    p = widgets.Label(value="AVISO: Si los ficheros se encuentran en una subcarpeta, indique la ruta:")
    display(p)
    p = widgets.Label(value="Ejemplo:C:\\Users\\user\\Documents\\Archivos")
    display(p)

    carpeta = widgets.Text(
        value='',
        placeholder='Carpeta',
        description='Carpeta:',
        disabled=False
    )
    display(carpeta)

    tema = widgets.Text(
        value='',
        placeholder='Tema',
        description='Tema:',
        disabled=False
    )

    uploader = widgets.FileUpload()

    # elegir_tema(tema, uploader)
    p = widgets.Label(value="Introduce el tema al que se corresponde el fichero: ")
    display(p)
    display(tema)
    display(uploader)

    boton = Boton_ficheros(tema, uploader, diccionario_tema, diccionario_fecha, diccionario_estudiantes, carpeta)
    display(boton.button)
