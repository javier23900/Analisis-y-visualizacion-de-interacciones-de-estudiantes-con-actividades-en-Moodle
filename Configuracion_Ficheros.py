from Clases_Botones import *
from ipyfilechooser import FileChooser

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
        
        - documentos: Array con los documentos incororados a la herramienta.
'''


def cargar_test(diccionario_tema, diccionario_fecha, diccionario_estudiantes, documentos):
    text = "LECTURA DE DATOS"
    titulo = widgets.HTML(value=f"<b>{text}</b>")
    display(titulo)

    tema = widgets.Text(
        value='',
        placeholder='Tema',
        description='Tema:',
        disabled=False
    )

    uploader = FileChooser()

    p = widgets.Label(value="Introduce el tema al que se corresponde el fichero: ")
    display(p)
    display(tema)
    display(uploader)

    boton = Boton_ficheros(tema, uploader, diccionario_tema, diccionario_fecha,
                           diccionario_estudiantes, documentos)
    display(boton.button)


'''
def cargar_registros(diccionario_registros): Función encargada de generar la opción de selección de los ficheros con la 
información de los registros de acceso.

    - Argumentos:

        - diccionario_registros: Diccionario con los estudiantes y sus registros de acceso. La clave del diccionario es 
        el identificador del estudiante y para cada clave su valor es un array de objetos de tipo Registros.

'''


def cargar_registros(diccionario_registros):
    text = "LECTURA DE DATOS"
    titulo = widgets.HTML(value=f"<b>{text}</b>")
    display(titulo)

    uploader = FileChooser()
    display(uploader)

    boton = Boton_registros(uploader, diccionario_registros)
    display(boton.button)
