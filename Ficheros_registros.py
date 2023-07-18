from Clases_Botones import *

'''
def cargar_registros(diccionario_estudiantes): Función encargada de generar la opción de selección de los ficheros con la 
información de los registros de acceso.

    - Argumentos:

        - diccionario_registros: Diccionario con los estudiantes y sus registros de acceso. La clave del diccionario es 
        el identificador del estudiante y para cada clave su valor es un array de objetos de tipo Registros.
        
'''


def cargar_registros(diccionario_estudiantes):
    text = "LECTURA DE DATOS"
    titulo = widgets.HTML(value=f"<b>{text}</b>")
    display(titulo)

    p = widgets.Label(value="AVISO: Los ficheros se cargan desde la raíz de la carpeta.")
    display(p)
    p = widgets.Label(value="AVISO: Si los ficheros se encuentran en una subcarpeta, indique la ruta:")
    display(p)
    p = widgets.Label(value="Ejemplo:C:\\Users\\user\\Documents\\Registros")
    display(p)

    carpeta = widgets.Text(
        value='',
        placeholder='Carpeta',
        description='Carpeta:',
        disabled=False
    )
    display(carpeta)

    uploader = widgets.FileUpload()

    display(uploader)

    boton = Boton_registros(uploader, diccionario_estudiantes)
    display(boton.button)
