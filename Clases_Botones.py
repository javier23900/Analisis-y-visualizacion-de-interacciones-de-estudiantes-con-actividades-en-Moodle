import ipywidgets as widgets
from IPython.display import display
import os

from ipyfilechooser import FileChooser

from Descargar_graficas_registros import Grafica_registros_pdf
from Graficas_registros import Grafica_registros
from Lectura_Ficheros import *
from Graficas_test import *
from Descargar_Datos_test import *
from Descargar_Graficas_test import *

'''
CLASE BOTON_FICHEROS

La clase representa el botón empleado para cargar los temas y su fichero correspondiente con la información de los test 
realizados por los alumnos.

  - diccionario_estudiantes: Diccionario con los estudiantes y sus test realizados. La clave del 
  diccionario es el identificador del estudiante y para cada clave su valor es un diccionario con los test. Este segundo 
  diccionario tiene como clave el tema al que pertenecen los test y para cada clave su valor es un array que contiene 
  los test realizados por los estudiantes.
  - diccionario_tema: Diccionario con los test realizados por los estudiantes. La clave del 
  diccionario es el tema al que pertenecen los test y para cada clave su valor es un array que contiene un conjunto de 
  arrays con los test realizados por los estudiantes.
  - diccionario_fecha: Diccionario con los test realizados por los estudiantes. La clave del 
  diccionario es la fecha en la que se realizó el test y para cada clave su valor es un array que contiene un conjunto 
  de arrays con los test de cada tema realizados por los estudiantes en dicha fecha.
  - tema: Tema del test cuyo fichero e información se quiere cargar.
  - carpeta: Ubicación del fichero que se quiere cargar.
  - uploader: Objeto de la librería ipywidgets que contiene el fichero seleccionado cuya información se quiere cargar.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.


Cuando se pulsa el botón se ejecuta la funcion encargada de leer el contenido del fichero y cargar la información 
(objetos de tipo Prueba) en los diccionarios con los que trabajamos.
Una vez se ha cargado la información correctamente se da al usuario la opción de repetir el proceso añadiendo un nuevo 
fichero.
'''


class Boton_ficheros:

    def __init__(self, tema, fichero, diccionario_tema, diccionario_fecha, diccionario_estudiantes,
                 documentos):
        self.diccionario_estudiantes = diccionario_estudiantes
        self.diccionario_tema = diccionario_tema
        self.diccionario_fecha = diccionario_fecha
        self.tema = tema
        self.fichero = fichero
        self.button = widgets.Button(description="Aceptar")
        self.button.on_click(self.on_button_clicked)
        self.documentos = documentos

    def on_button_clicked(self, b):

        if self.tema.value == '':
            text = 'Introduzca el tema del fichero'
            myLabel = widgets.HTML(value=f"<b><font color='red'>{text}</b>")
            box_layout = widgets.Layout(display='flex',
                                        flex_flow='column',
                                        align_items='center',
                                        border='solid',
                                        width='25%',
                                        margin='1%')
            items = [myLabel]
            box = widgets.Box(children=items, layout=box_layout)
            display(box)

        elif self.fichero.selected is None:
            text = 'Seleccione el fichero que desea leer'
            myLabel = widgets.HTML(value=f"<b><font color='red'>{text}</b>")
            box_layout = widgets.Layout(display='flex',
                                        flex_flow='column',
                                        align_items='center',
                                        border='solid',
                                        width='25%',
                                        margin='1%')
            items = [myLabel]
            box = widgets.Box(children=items, layout=box_layout)
            display(box)
        else:
            self.button.layout.visibility = 'hidden'

            '''if self.uploader_path is not None:
                print(self.uploader_path)
                print(self.uploader_filename)
                fichero = os.path.join(self.uploader_path, self.uploader_filename)
            else:
                fichero = self.uploader_filename'''
            fichero = self.fichero.selected

            self.diccionario_tema = lectura_tema(fichero, self.diccionario_tema, self.tema.value)
            self.diccionario_fecha = lectura_fecha(fichero, self.diccionario_fecha, self.tema.value)
            self.diccionario_estudiantes = test_por_alumno(fichero, self.diccionario_estudiantes, self.tema.value)

            if self.diccionario_tema is None or self.diccionario_tema is None or self.diccionario_tema is None:

                text = 'No se ha encontrado el fichero en la ruta indicada.'
                myLabel = widgets.HTML(value=f"<b><font color='red'>{text}</b>")
                box_layout = widgets.Layout(display='flex',
                                            flex_flow='column',
                                            align_items='center',
                                            border='solid',
                                            width='30%',
                                            margin='1%')
                items = [myLabel]
                box = widgets.Box(children=items, layout=box_layout)
                display(box)

            else:

                fichero = self.fichero.selected
                self.documentos.append((self.fichero.selected_filename, self.tema.value, fichero))

                p = widgets.Label(value="¿Desea añadir otro fichero?")
                display(p)

                b = widgets.HBox()

                botons = Boton_ficheros_s(self.tema, self.fichero, self.diccionario_tema,
                                          self.diccionario_fecha, b, self.diccionario_estudiantes, self.documentos)
                # display(botons.button)

                botonn = Boton_ficheros_n(b)
                # display(botonn.button)

                botones = [botons.button, botonn.button]

                b.children = [i for i in botones]
                display(b)


'''
CLASE BOTON_FICHEROS_S

La clase representa el botón empleado para repetir el proceso de cargar los temas y su fichero correspondiente con la 
información de los test realizados por los alumnos.

  - box: objeto de tipo HBox de la librería ipywidgets que contiene un objeto de tipo Boton_Ficheros_S y otro objeto de 
  tipo Boton_Ficheros_N.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.
  - diccionario_tema: Diccionario con los test realizados por los estudiantes. La clave del diccionario es el tema al 
  que pertenecen los test y para cada clave su valor es un array que contiene un conjunto de arrays con los test 
  realizados por los estudiantes.
  - diccionario_fecha: La función devuelve un diccionario con los test realizados por los estudiantes. La clave del 
  diccionario es la fecha en la que se realizó el test y para cada clave su valor es un array que contiene un conjunto 
  de arrays con los test de cada tema realizados por los estudiantes en dicha fecha.
  - diccionario_estudiantes: La función devuelve un diccionario con los estudiantes y sus test realizados. La clave del 
  diccionario es el identificador del estudiante y para cada clave su valor es un diccionario con los test. Este segundo 
  diccionario tiene como clave el tema al que pertenecen los test y para cada clave su valor es un array que contiene 
  los test realizados por los estudiantes.
  - tema: Tema del test cuyo fichero e información se quiere cargar.
  - uploader: Objeto de la librería ipywidgets que contiene el fichero seleccionado cuya información se quiere cargar.

Cuando se pulsa el botón se muestrá un objeto de tipo Boton_ficheros para continuar la ejecución.
'''


class Boton_ficheros_s:

    def __init__(self, tema, fichero, diccionario_tema, diccionario_fecha, b, diccionario_estudiantes, documentos):
        self.box = b
        self.button = widgets.Button(description="Si")
        self.button.on_click(self.on_button_clicked)
        self.diccionario_tema = diccionario_tema
        self.diccionario_fecha = diccionario_fecha
        self.diccionario_estudiantes = diccionario_estudiantes
        self.tema = tema
        self.fichero = fichero
        self.documentos = documentos

    def on_button_clicked(self, b):
        """p = widgets.Label(value="AVISO: Los ficheros se cargan desde la raíz de la carpeta.")
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
        display(carpeta)"""

        tema = widgets.Text(
            value='',
            placeholder='Tema: ',
            description='Tema:',
            disabled=False
        )

        # uploader = widgets.FileUpload()
        uploader = FileChooser()

        # elegir_tema(tema, uploader)
        p = widgets.Label(value="Introduce el tema al que se corresponde el fichero: ")
        display(p)
        display(tema)
        display(uploader)

        boton = Boton_ficheros(tema, uploader, self.diccionario_tema, self.diccionario_fecha,
                               self.diccionario_estudiantes, self.documentos)
        self.box.layout.visibility = 'hidden'
        display(boton.button)


'''
CLASE BOTON_FICHEROS_N

La clase representa el botón empleado para finalizar el proceso de cargar los temas y su fichero correspondiente con la 
información de los test realizados por los alumnos.

  - box: objeto de tipo HBox de la librería ipywidgets que contiene un objeto de tipo Boton_Ficheros_S y otro objeto de 
  tipo Boton_Ficheros_N.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.

Cuando se pulsa el botón se oculta el objeto de tipo Boton_ficheros_si para impedir que se continue la ejecución.
'''


class Boton_ficheros_n:

    def __init__(self, b):
        self.box = b
        self.button = widgets.Button(description="No")
        self.button.on_click(self.on_button_clicked)

    def on_button_clicked(self, b):
        self.box.layout.visibility = 'hidden'
        p = widgets.Label(value="Lectura Finalizada")
        display(p)


'''
CLASE BOTON_FECHAS

La clase representa el botón empleado para seleccionar los intervalos de fechas para los cuales se quiere obtener 
información.

  - fecha_inicio: Fecha inicial del intervalo.
  - fecha_final: Fecha final del intervalo.
  - fechas: Array donde se van a almacenar los intervalos de fechas seleccionados.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.

Cuando se pulsa el botón se ejecuta la funcion encargada de almacenar el intervalo de fechas en un array. Una vez se ha 
guardado correctamente se da al usuario la opción de repetir el proceso.
'''


class Boton_fechas:

    def __init__(self, fecha_inicio, fecha_final, fechas):
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.fechas = fechas
        self.button = widgets.Button(description="Aceptar")
        self.button.on_click(self.on_button_clicked)

    def on_button_clicked(self, b):

        if self.fecha_inicio.value is None:
            text = 'Introduzca la fecha inicial del intervalo'
            myLabel = widgets.HTML(value=f"<b><font color='red'>{text}</b>")
            box_layout = widgets.Layout(display='flex',
                                        flex_flow='column',
                                        align_items='center',
                                        border='solid',
                                        width='25%',
                                        margin='1%')
            items = [myLabel]
            box = widgets.Box(children=items, layout=box_layout)
            display(box)

        elif self.fecha_final.value is None:
            text = 'Introduzca la fecha final del intervalo'
            myLabel = widgets.HTML(value=f"<b><font color='red'>{text}</b>")
            box_layout = widgets.Layout(display='flex',
                                        flex_flow='column',
                                        align_items='center',
                                        border='solid',
                                        width='25%',
                                        margin='1%')
            items = [myLabel]
            box = widgets.Box(children=items, layout=box_layout)
            display(box)
        else:
            self.button.layout.visibility = 'hidden'

            f = [datetime.strptime(str(self.fecha_inicio.value), '%Y-%m-%d'),
                 datetime.strptime(str(self.fecha_final.value), '%Y-%m-%d')]

            self.fechas.append(f)

            p = widgets.Label(value="¿Desea añadir otro intervalo de fechas?")
            display(p)

            b = widgets.HBox()

            botons = Boton_fechas_s(self.fecha_inicio, self.fecha_final, self.fechas, b)
            # display(botons.button)

            botonn = Boton_fechas_n(b)
            # display(botonn.button)

            botones = [botons.button, botonn.button]

            b.children = [i for i in botones]
            display(b)


'''
CLASE BOTON_FECHAS_S

La clase representa el botón empleado para repetir el proceso de seleccionar los intervalos de fechas para los cuales 
se quiere obtener información.

  - box: objeto de tipo HBox de la librería ipywidgets que contiene un objeto de tipo Boton_fechas_S y otro objeto de 
  tipo Boton_fechas_N.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.
  - fecha_inicio: Fecha inicial del intervalo.
  - fecha_final: Fecha final del intervalo.
  - fechas: Array donde se van a almacenar los intervalos de fechas seleccionados.

Cuando se pulsa el botón se muestrá un objeto de tipo Boton_ficheros para continuar la ejecución.
'''


class Boton_fechas_s:

    def __init__(self, fecha_inicio, fecha_final, fechas, b):
        self.box = b
        self.button = widgets.Button(description="Si")
        self.button.on_click(self.on_button_clicked)
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.fechas = fechas

    def on_button_clicked(self, b):
        fecha_inicio = widgets.DatePicker(
            description='Fecha Inicio:',
            disabled=False
        )

        fecha_final = widgets.DatePicker(
            description='Fecha Final:',
            disabled=False
        )

        p = widgets.Label(value="Introduce el intervalo de fechas: ")
        display(p)

        display(fecha_inicio)
        display(fecha_final)

        boton = Boton_fechas(fecha_inicio, fecha_final, self.fechas)
        self.box.layout.visibility = 'hidden'
        display(boton.button)


'''
CLASE BOTON_FECHAS_N

La clase representa el botón empleado para finalizar el proceso seleccionar los intervalos de fechas para los cuales 
se quiere obtener información.

  - box: objeto de tipo HBox de la librería ipywidgets que contiene un objeto de tipo Boton_fechas_S y otro objeto de 
  tipo Boton_fechas_N.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.

Cuando se pulsa el botón se oculta el objeto de tipo Boton_fechas_si para impedir que se continue la ejecución.
'''


class Boton_fechas_n:

    def __init__(self, b):
        self.box = b
        self.button = widgets.Button(description="No")
        self.button.on_click(self.on_button_clicked)

    def on_button_clicked(self, b):
        self.box.layout.visibility = 'hidden'
        p = widgets.Label(value="Selección Finalizada")
        display(p)


'''
CLASE BOTON_PROCESO_TEMAFECHA

La clase representa el botón empleado para ejecutar una de las opciones de análisis de la información obtenida de los 
test realizados por los alumnos.

  - opcion: Objeto de tipo RadioButtons de la libreria ipywidgets con la opción de análisis deseada.
  - diccionario_tema: La función devuelve un diccionario con los test realizados por los estudiantes. La clave del 
  diccionario es el tema al que pertenecen los test y para cada clave su valor es un array que contiene un conjunto de 
  arrays con los test realizados por los estudiantes.
  - seleccion_temas: Objeto de tipo SelectMultiple de la libreria ipywidgets con los temas seleccionados para los cuales 
  se quiere ejecutar el análisis.
  - seleccion_fechas: bjeto de tipo SelectMultiple de la libreria ipywidgets con los intervalos de fechas seleccionados 
  para los cuales se quiere ejecutar el análisis.
  - fechas: Array donde se van a almacenar los intervalos de fechas seleccionados.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.

Cuando se pulsa el botón se ejecuta una de entre dos opciones de análisis:
  - analisis_fechas_temario: Analiza los test de un tema para una serie de intervalos de fechas.
  - analisis_temario_fechas: Analiza los test para una serie de intervalos de fechas para una serie de temas.
'''


class Boton_proceso_temafecha:

    def __init__(self, d_t, s_t, s_f, fs, opcion):
        self.opcion = opcion
        self.diccionario_tema = d_t
        self.seleccion_temas = s_t
        self.seleccion_fechas = s_f
        self.fechas = fs
        self.button = widgets.Button(description="Aceptar")
        self.button.on_click(self.on_button_clicked)

    def on_button_clicked(self, b):
        if self.opcion.value == "Temas x Fecha":
            analisis_temario_fechas(self.diccionario_tema, self.seleccion_temas.value, self.seleccion_fechas.value,
                                    self.fechas)
        elif self.opcion.value == "Fecha x Temas":
            analisis_fechas_temario(self.diccionario_tema, self.seleccion_temas.value, self.seleccion_fechas.value,
                                    self.fechas)


'''
CLASE BOTON_PROCESO_TEMAFECHA_PDF

La clase representa el botón empleado para ejecutar una de las opciones de análisis de los datos obtenidos de los test 
realizados por los alumnos y descargar un documento pdf con dicha información.

  - opcion: Objeto de tipo RadioButtons de la libreria ipywidgets con la opción de análisis deseada.
  - diccionario_tema: La función devuelve un diccionario con los test realizados por los estudiantes. La clave del 
  diccionario es el tema al que pertenecen los test y para cada clave su valor es un array que contiene un conjunto de 
  arrays con los test realizados por los estudiantes.
  - seleccion_temas: Objeto de tipo SelectMultiple de la libreria ipywidgets con los temas seleccionados para los 
  cuales se quiere ejecutar el análisis.
  - seleccion_fechas: bjeto de tipo SelectMultiple de la libreria ipywidgets con los intervalos de fechas seleccionados 
  para los cuales se quiere ejecutar el análisis.
  - fechas: Array donde se van a almacenar los intervalos de fechas seleccionados.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.
  - nombre_documento = Nombre del documento.
  - carpeta: Carpeta destino para el documento a descargar


Cuando se pulsa el botón se ejecuta una de entre dos opciones de análisis:
  - analisis_fechas_temario: Analiza los test de un tema para una serie de intervalos de fechas.
  - analisis_temario_fechas: Analiza los test para una serie de intervalos de fechas para una serie de temas.
'''


class Boton_proceso_temafecha_pdf:

    def __init__(self, d_t, s_t, s_f, fs, opcion, nombre_documento, carpeta):
        self.opcion = opcion
        self.diccionario_tema = d_t
        self.seleccion_temas = s_t
        self.seleccion_fechas = s_f
        self.fechas = fs
        self.button = widgets.Button(description="Descargar")
        self.button.on_click(self.on_button_clicked)

        self.nombre_documento = nombre_documento
        self.carpeta = carpeta

    def on_button_clicked(self, b):

        documento = canvas.Canvas(self.nombre_documento.value + ".pdf")
        documento.setPageSize(A4)

        if self.opcion.value == "Temas x Fecha":
            analisis_temario_fechas_pdf(self.diccionario_tema, self.seleccion_temas.value, self.seleccion_fechas.value,
                                        self.fechas, documento, self.nombre_documento.value + ".pdf",
                                        self.carpeta.value)
        elif self.opcion.value == "Fecha x Temas":
            analisis_fechas_temario_pdf(self.diccionario_tema, self.seleccion_temas.value, self.seleccion_fechas.value,
                                        self.fechas, documento, self.nombre_documento.value + ".pdf",
                                        self.carpeta.value)


'''
CLASE BOTON_PROCESO_RANKING

La clase representa el botón empleado para ejecutar la opción de ranking de análisis de la información obtenida de los 
test realizados por los alumnos.

  - opcion: Objeto de tipo RadioButtons de la libreria ipywidgets con el valor para el cual se quiere realizar el 
  ranking (Nota media de los test, número de veces que se ha completado el test, número de veces que se ha aprobado el 
  test y porcentaje de aprobados)
  - diccionario_tema: Diccionario con los test realizados por los estudiantes. La clave del diccionario es el tema al 
  que pertenecen los test y para cada clave su valor es un array que contiene un conjunto de arrays con los test 
  realizados por los estudiantes.
  - seleccion_fechas: bjeto de tipo SelectMultiple de la libreria ipywidgets con los intervalos de fechas seleccionados 
  para los cuales se quiere ejecutar el análisis.
  - fechas: Array donde se van a almacenar los intervalos de fechas seleccionados.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.

Cuando se pulsa el botón se ejecuta la función encargada de ordenar los temas de mejores a peores para una serie de 
valores.
'''


class Boton_proceso_ranking:

    def __init__(self, d_t, s_f, fs, opcion):
        self.opcion = opcion
        self.diccionario_tema = d_t
        self.seleccion_fechas = s_f
        self.fechas = fs
        self.button = widgets.Button(description="Aceptar")
        self.button.on_click(self.on_button_clicked)

    def on_button_clicked(self, b):
        ranking_test(self.diccionario_tema, self.seleccion_fechas.value, self.fechas, self.opcion.value)


'''
CLASE BOTON_PROCESO_RANKING_PDF

La clase representa el botón empleado para descargar un documento pdf con el ranking de temas obtenido a partir del 
análisis de la información de los test realizados por los alumnos.

  - opcion: Objeto de tipo RadioButtons de la libreria ipywidgets con el valor para el cual se quiere realizar el 
  ranking (Nota media de los test, número de veces que se ha completado el test, número de veces que se ha aprobado el 
  test y porcentaje de aprobados)
  - diccionario_tema: Diccionario con los test realizados por los estudiantes. La clave del diccionario es el tema al 
  que pertenecen los test y para cada clave su valor es un array que contiene un conjunto de arrays con los test 
  realizados por los estudiantes.
  - seleccion_fechas: bjeto de tipo SelectMultiple de la libreria ipywidgets con los intervalos de fechas seleccionados 
  para los cuales se quiere ejecutar el análisis.
  - fechas: Array donde se van a almacenar los intervalos de fechas seleccionados.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.
  - nombre_documento = Nombre del documento.
  - carpeta: Carpeta destino para el documento a descargar

Cuando se pulsa el botón se ejecuta la función encargada de ordenar los temas de mejores a peores para una serie de 
valores y descargar un documento pdf con dicha información.
'''


class Boton_proceso_ranking_pdf:

    def __init__(self, d_t, s_f, fs, opcion, nombre_documento, carpeta):
        self.opcion = opcion
        self.diccionario_tema = d_t
        self.seleccion_fechas = s_f
        self.fechas = fs
        self.button = widgets.Button(description="Descargar")
        self.button.on_click(self.on_button_clicked)

        self.nombre_documento = nombre_documento
        self.carpeta = carpeta

    def on_button_clicked(self, b):
        documento = canvas.Canvas(self.nombre_documento.value + ".pdf")
        documento.setPageSize(A4)

        ranking_test_pdf(self.diccionario_tema, self.seleccion_fechas.value, self.fechas, self.opcion.value, documento,
                         self.nombre_documento.value + ".pdf", self.carpeta.value)


'''
CLASE BOTON_GRAFICAS

La clase representa el botón empleado para generar las gráicas correspondientes a una de las opciones de análisis de la 
información obtenida de los test realizados por los alumnos.
  
  - color: Color deseado para las barras de la gráfica.
  - opcion: Objeto de tipo RadioButtons de la libreria ipywidgets con la opción de análisis deseada.
  - opcion2: Opción para el valor que se desea mostrar en las gráficas (nota media, test finalizados, test aprobados o 
  porcentaje de aprobados).
  - diccionario_tema: La función devuelve un diccionario con los test realizados por los estudiantes. La clave del 
  diccionario es el tema al que pertenecen los test y para cada clave su valor es un array que contiene un conjunto de 
  arrays con los test realizados por los estudiantes.
  - seleccion_temas: Objeto de tipo SelectMultiple de la libreria ipywidgets con los temas seleccionados para los cuales 
  se quiere ejecutar el análisis.
  - seleccion_fechas: bjeto de tipo SelectMultiple de la libreria ipywidgets con los intervalos de fechas seleccionados 
  para los cuales se quiere ejecutar el análisis.
  - fechas: Array donde se van a almacenar los intervalos de fechas seleccionados.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.
  - diseno: opción para el diseño de la gráfica

Cuando se pulsa el botón se ejecuta una de entre dos opciones de gráficas para el análisis de datos obtenidos a partir 
de los test relizados por los alumnos:
  - Grafica_fecha_test: Para una serie de temas muestra una grafica comparando un determinado valor (nota media, test 
  finalizados, test aprobados o porcentaje de aprobados) para varios intervalos de tiempo.
  - Grafica_test_fecha: Muestra para una serie de intervalos de tiempo una gráfica comparando un determinado valor 
  (nota media, test finalizados, test aprobados o porcentaje de aprobados) para varios temas.
'''


class Boton_graficas:

    def __init__(self, d_t, s_t, s_f, fs, opcion, opcion2, color, diseno):
        self.color = color
        self.opcion = opcion
        self.opcion2 = opcion2
        self.diccionario_tema = d_t
        self.seleccion_temas = s_t
        self.seleccion_fechas = s_f
        self.fechas = fs
        self.button = widgets.Button(description="Aceptar")
        self.button.on_click(self.on_button_clicked)
        self.diseno = diseno

    def on_button_clicked(self, b):

        if self.opcion.value == "Temas x Fecha":
            Grafica_test_fecha(self.diccionario_tema, self.seleccion_temas.value, self.seleccion_fechas.value,
                               self.fechas, self.opcion2.value, self.color.value, self.diseno.value)
        elif self.opcion.value == "Fecha x Temas":
            Grafica_fecha_test(self.diccionario_tema, self.seleccion_temas.value, self.seleccion_fechas.value,
                               self.fechas, self.opcion2.value, self.color.value, self.diseno.value)


'''
CLASE BOTON_GRAFICAS_PDF

La clase representa el botón empleado para generar y descargar en un documento pdf los datos y las gráficas 
correspondientes a una de las opciones de análisis de la información obtenida de los test realizados por los alumnos.
  
  - color: Color deseado para las barras de la gráfica.
  - opcion: Objeto de tipo RadioButtons de la libreria ipywidgets con la opción de análisis deseada.
  - opcion2: Opción para el valor que se desea mostrar en las gráficas (nota media, test finalizados, test aprobados o 
  porcentaje de aprobados).
  - diccionario_tema: La función devuelve un diccionario con los test realizados por los estudiantes. La clave del 
  diccionario es el tema al que pertenecen los test y para cada clave su valor es un array que contiene un conjunto de 
  arrays con los test realizados por los estudiantes.
  - seleccion_temas: Objeto de tipo SelectMultiple de la libreria ipywidgets con los temas seleccionados para los cuales 
  se quiere ejecutar el análisis.
  - seleccion_fechas: bjeto de tipo SelectMultiple de la libreria ipywidgets con los intervalos de fechas seleccionados 
  para los cuales se quiere ejecutar el análisis.
  - fechas: Array donde se van a almacenar los intervalos de fechas seleccionados.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.
  - nombre_documento = Nombre del documento.
  - carpeta: Carpeta destino para el documento a descargar
  - carpeta2: Carpeta destino para la gráfica a descargar
  - diseno: opción para el diseño de la gráfica

Cuando se pulsa el botón se ejecuta una de entre dos opciones de gráficas para el análisis de datos obtenidos a partir 
de los test relizados por los alumnos:
  - Grafica_fecha_test: Para una serie de temas muestra una grafica comparando un determinado valor (nota media, test 
  finalizados, test aprobados o porcentaje de aprobados) para varios intervalos de tiempo.
  - Grafica_test_fecha: Muestra para una serie de intervalos de tiempo una gráfica comparando un determinado valor 
  (nota media, test finalizados, test aprobados o porcentaje de aprobados) para varios temas.
'''


class Boton_graficas_pdf:

    def __init__(self, d_t, s_t, s_f, fs, opcion, opcion2, color, nombre_documento, carpeta, diseno):
        self.color = color
        self.opcion = opcion
        self.opcion2 = opcion2
        self.diccionario_tema = d_t
        self.seleccion_temas = s_t
        self.seleccion_fechas = s_f
        self.fechas = fs
        self.button = widgets.Button(description="Descargar")
        self.button.on_click(self.on_button_clicked)

        self.nombre_documento = nombre_documento
        self.carpeta = carpeta
        self.diseno = diseno

    def on_button_clicked(self, b):

        documento = canvas.Canvas(self.nombre_documento.value + ".pdf")
        documento.setPageSize(A4)

        if self.opcion.value == "Fecha x Temas":
            Grafica_fecha_test_pdf(self.diccionario_tema, self.seleccion_temas.value, self.seleccion_fechas.value,
                                   self.fechas, self.opcion2.value, self.color.value, documento,
                                   self.nombre_documento.value + ".pdf", self.carpeta.value,
                                   self.diseno.value)
        elif self.opcion.value == "Temas x Fecha":
            Grafica_test_fecha_pdf(self.diccionario_tema, self.seleccion_temas.value, self.seleccion_fechas.value,
                                   self.fechas, self.opcion2.value, self.color.value, documento,
                                   self.nombre_documento.value + ".pdf", self.carpeta.value,
                                   self.diseno.value)


'''
CLASE BOTON_ESTUDIANTES

La clase representa el botón empleado para ejecutar una de las opciones de análisis de la información obtenida de los 
test realizados por los alumnos, centrándonos en los datos individuales de cada alumno.

  - opcion: Objeto de tipo RadioButtons de la libreria ipywidgets con la opción de análisis deseada.
  - estudiante: Objeto de tipo Dropdown de la librería ipywidgets que indica el estudiante del cual se quiere obtener 
  los resultados.
  - diccionario_tema: La función devuelve un diccionario con los test realizados por los estudiantes. La clave del 
  diccionario es el tema al que pertenecen los test y para cada clave su valor es un array que contiene un conjunto de 
  arrays con los test realizados por los estudiantes.
  - seleccion_temas: Objeto de tipo SelectMultiple de la libreria ipywidgets con los temas seleccionados para los cuales 
  se quiere ejecutar el análisis.
  - seleccion_fechas: bjeto de tipo SelectMultiple de la libreria ipywidgets con los intervalos de fechas seleccionados 
  para los cuales se quiere ejecutar el análisis.
  - fechas: Array donde se van a almacenar los intervalos de fechas seleccionados.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.
'''


class Boton_estudiantes:

    def __init__(self, d_e, s_t, s_f, fs, opcion, estudiantes):
        self.opcion = opcion
        self.estudiantes = estudiantes
        self.diccionario_estudiantes = d_e
        self.seleccion_temas = s_t
        self.seleccion_fechas = s_f
        self.fechas = fs
        self.button = widgets.Button(description="Aceptar")
        self.button.on_click(self.on_button_clicked)

    def on_button_clicked(self, b):
        Resultados_estudiante(self.estudiantes.value, self.diccionario_estudiantes, self.seleccion_temas.value,
                              self.seleccion_fechas.value, self.fechas, self.opcion.value)


'''
CLASE BOTON_ESTUDIANTES_PDF

La clase representa el botón empleado para descargar la información de una de las opciones de análisis de los datos 
obtenidos de los test realizados por los alumnos, centrándonos en los datos individuales de cada alumno.

  - opcion: Objeto de tipo RadioButtons de la libreria ipywidgets con la opción de análisis deseada.
  - estudiante: Objeto de tipo Dropdown de la librería ipywidgets que indica el estudiante del cual se quiere obtener 
  los resultados.
  - diccionario_tema: La función devuelve un diccionario con los test realizados por los estudiantes. La clave del 
  diccionario es el tema al que pertenecen los test y para cada clave su valor es un array que contiene un conjunto de 
  arrays con los test realizados por los estudiantes.
  - seleccion_temas: Objeto de tipo SelectMultiple de la libreria ipywidgets con los temas seleccionados para los cuales 
  se quiere ejecutar el análisis.
  - seleccion_fechas: bjeto de tipo SelectMultiple de la libreria ipywidgets con los intervalos de fechas seleccionados 
  para los cuales se quiere ejecutar el análisis.
  - fechas: Array donde se van a almacenar los intervalos de fechas seleccionados.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.
  - nombre_documento: Nombre del documento.
  - nombre_documento = Nombre del documento.
  - carpeta: Carpeta destino para el documento a descargar
'''


class Boton_estudiantes_pdf:

    def __init__(self, d_e, s_t, s_f, fs, opcion, estudiantes, nombre_documento, carpeta):
        self.opcion = opcion
        self.estudiantes = estudiantes
        self.diccionario_estudiantes = d_e
        self.seleccion_temas = s_t
        self.seleccion_fechas = s_f
        self.fechas = fs
        self.button = widgets.Button(description="Descargar")
        self.button.on_click(self.on_button_clicked)

        self.nombre_documento = nombre_documento
        self.carpeta = carpeta

    def on_button_clicked(self, b):
        documento = canvas.Canvas(self.nombre_documento.value + ".pdf")
        documento.setPageSize(A4)

        Resultados_estudiante_pdf(self.estudiantes.value, self.diccionario_estudiantes, self.seleccion_temas.value,
                                  self.seleccion_fechas.value, self.fechas, self.opcion.value, documento,
                                  self.nombre_documento.value + ".pdf", self.carpeta.value)


'''
CLASE BOTON_RANKING_ESTUDIANTE

La clase representa el botón empleado para ejecutar la opción de ranking de análisis de la información obtenida de los 
test realizados por los alumnos.

  - opcion: Objeto de tipo RadioButtons de la libreria ipywidgets con el valor para el cual se quiere realizar el 
  ranking (Nota media de los test, número de veces que se ha completado el test, número de veces que se ha aprobado el 
  test y porcentaje de aprobados)
  - diccionario_estudiantes: Diccionario con los estudiantes y sus test realizados. La clave del diccionario es el 
  identificador del estudiante y para cada clave su valor es un diccionario con los test. Este segundo diccionario tiene 
  como clave el tema al que pertenecen los test y para cada clave su valor es un array que contiene los test realizados 
  por los estudiantes.
  - seleccion_fechas: objeto de tipo SelectMultiple de la libreria ipywidgets con los intervalos de fechas seleccionados 
  para los cuales se quiere ejecutar el análisis.
  - fechas: Array donde se van a almacenar los intervalos de fechas seleccionados.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.
  - estudiante: objeto de tipo SelectMultiple de la libreria ipywidgets con los estudiantes seleccionados para los 
  cuales se quiere ejecutar el análisis.

Cuando se pulsa el botón se ejecuta la función encargada de ordenar los temas para una serie de valores en ciertos 
intervalos de tiempo para los estudiantes.
'''


class Boton_ranking_estudiante:

    def __init__(self, d_e, s_f, fs, opcion, estudiante):
        self.opcion = opcion
        self.diccionario_estudiantes = d_e
        self.seleccion_fechas = s_f
        self.fechas = fs
        self.button = widgets.Button(description="Aceptar")
        self.button.on_click(self.on_button_clicked)
        self.estudiante = estudiante

    def on_button_clicked(self, b):
        ranking_test_estudiante(self.estudiante.value, self.diccionario_estudiantes, self.seleccion_fechas.value,
                                self.fechas, self.opcion.value)


'''
CLASE BOTON_RANKING_ESTUDIANTE_PDF

La clase representa el botón empleado para ejecutar la opción de ranking de análisis de la información obtenida de los 
test realizados por los alumnos.

  - opcion: Objeto de tipo RadioButtons de la libreria ipywidgets con el valor para el cual se quiere realizar el 
  ranking (Nota media de los test, número de veces que se ha completado el test, número de veces que se ha aprobado el 
  test y porcentaje de aprobados)
  - diccionario_estudiantes: Diccionario con los estudiantes y sus test realizados. La clave del diccionario es el 
  identificador del estudiante y para cada clave su valor es un diccionario con los test. Este segundo diccionario tiene 
  como clave el tema al que pertenecen los test y para cada clave su valor es un array que contiene los test realizados 
  por los estudiantes.
  - seleccion_fechas: objeto de tipo SelectMultiple de la libreria ipywidgets con los intervalos de fechas seleccionados 
  para los cuales se quiere ejecutar el análisis.
  - fechas: Array donde se van a almacenar los intervalos de fechas seleccionados.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.
  - estudiante: objeto de tipo SelectMultiple de la libreria ipywidgets con los estudiantes seleccionados para los 
  cuales se quiere ejecutar el análisis.
  - nombre_documento: Nombre del documento.
  - carpeta: Carpeta destino para el documento a descargar

Cuando se pulsa el botón se ejecuta la función encargada de generar un documento PDF con los temas ordenados para una 
serie de valores en ciertos intervalos de tiempo para los estudiantes.
'''


class Boton_ranking_estudiante_pdf:

    def __init__(self, d_e, s_f, fs, opcion, estudiante, nombre_documento, carpeta):
        self.opcion = opcion
        self.diccionario_estudiantes = d_e
        self.seleccion_fechas = s_f
        self.fechas = fs
        self.button = widgets.Button(description="Descargar")
        self.button.on_click(self.on_button_clicked)
        self.estudiante = estudiante

        self.nombre_documento = nombre_documento
        self.carpeta = carpeta

    def on_button_clicked(self, b):
        documento = canvas.Canvas(self.nombre_documento.value + ".pdf")
        documento.setPageSize(A4)

        ranking_test_estudiante_pdf(self.estudiante.value, self.diccionario_estudiantes, self.seleccion_fechas.value,
                                    self.fechas, self.opcion.value, documento, self.nombre_documento.value + ".pdf",
                                    self.carpeta.value)


'''
**CLASE BOTON_RANKING_ESTUDIANTES**

La clase representa el botón empleado para ejecutar la opción de ranking de análisis de la información obtenida de los 
test realizados por los alumnos.

  - estudiante: objeto de tipo SelectMultiple de la libreria ipywidgets con los estudiantes seleccionados para los 
  cuales se quiere ejecutar el análisis.
  - diccionario_estudiantes: Diccionario con los estudiantes y sus test realizados. La clave del diccionario es el 
  identificador del estudiante y para cada clave su valor es un diccionario con los test. Este segundo diccionario tiene 
  como clave el tema al que pertenecen los test y para cada clave su valor es un array que contiene los test realizados 
  por los estudiantes.
  - seleccion_temas: objeto de tipo SelectMultiple de la libreria ipywidgets con los temas seleccionados para los 
  cuales se quiere ejecutar el análisis.
  - temas: Array donde se van a almacenar los temas seleccionados.
  - opcion: Objeto de tipo RadioButtons de la libreria ipywidgets con el valor para el cual se quiere realizar el 
  ranking (Nota media de los test, número de veces que se ha completado el test, número de veces que se ha aprobado el 
  test y porcentaje de aprobados)
  - seleccion_fechas: objeto de tipo SelectMultiple de la libreria ipywidgets con los intervalos de fechas seleccionados 
  para los cuales se quiere ejecutar el análisis.
  - fechas: Array donde se van a almacenar los intervalos de fechas seleccionados.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.

Cuando se pulsa el botón se ejecuta la función encargada de ordenar a los estudiantes de mejores a peores para una 
serie de valores en ciertos intervalos de tiempo.
'''


class Boton_ranking_estudiantes:

    def __init__(self, d_e, s_t, temas, s_f, fs, opcion):
        self.diccionario_estudiantes = d_e
        self.seleccion_temas = s_t
        self.temas = temas
        self.opcion = opcion
        self.seleccion_fechas = s_f
        self.fechas = fs
        self.button = widgets.Button(description="Aceptar")
        self.button.on_click(self.on_button_clicked)

    def on_button_clicked(self, b):
        ranking_estudiantes(self.diccionario_estudiantes, self.seleccion_temas.value, self.temas,
                            self.seleccion_fechas.value, self.fechas, self.opcion.value)


'''
CLASE BOTON_RANKING_ESTUDIANTES_PDF

La clase representa el botón empleado para ejecutar la opción de ranking de análisis de la información obtenida de los 
test realizados por los alumnos.

  - estudiante: objeto de tipo SelectMultiple de la libreria ipywidgets con los estudiantes seleccionados para los 
  cuales se quiere ejecutar el análisis.
  - diccionario_estudiantes: Diccionario con los estudiantes y sus test realizados. La clave del diccionario es el 
  identificador del estudiante y para cada clave su valor es un diccionario con los test. Este segundo diccionario tiene 
  como clave el tema al que pertenecen los test y para cada clave su valor es un array que contiene los test realizados 
  por los estudiantes.
  - seleccion_temas: objeto de tipo SelectMultiple de la libreria ipywidgets con los temas seleccionados para los cuales 
  se quiere ejecutar el análisis.
  - temas: Array donde se van a almacenar los temas seleccionados.
  - opcion: Objeto de tipo RadioButtons de la libreria ipywidgets con el valor para el cual se quiere realizar el 
  ranking (Nota media de los test, número de veces que se ha completado el test, número de veces que se ha aprobado el 
  test y porcentaje de aprobados)
  - seleccion_fechas: objeto de tipo SelectMultiple de la libreria ipywidgets con los intervalos de fechas seleccionados 
  para los cuales se quiere ejecutar el análisis.
  - fechas: Array donde se van a almacenar los intervalos de fechas seleccionados.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.
  - nombre_documento: Nombre del documento.
  - carpeta: Carpeta destino para el documento a descargar

Cuando se pulsa el botón se ejecuta la función encargada de generar un documento PDF con los estudiantes ordenados de 
mejores a peores para una serie de valores en ciertos intervalos de tiempo.
'''


class Boton_ranking_estudiantes_pdf:

    def __init__(self, d_e, s_t, temas, s_f, fs, opcion, nombre_documento, carpeta):
        self.diccionario_estudiantes = d_e
        self.seleccion_temas = s_t
        self.temas = temas
        self.opcion = opcion
        self.seleccion_fechas = s_f
        self.fechas = fs
        self.button = widgets.Button(description="Descargar")
        self.button.on_click(self.on_button_clicked)

        self.nombre_documento = nombre_documento
        self.carpeta = carpeta

    def on_button_clicked(self, b):
        documento = canvas.Canvas(self.nombre_documento.value + ".pdf")
        documento.setPageSize(A4)

        ranking_estudiantes_pdf(self.diccionario_estudiantes, self.seleccion_temas.value, self.temas,
                                self.seleccion_fechas.value, self.fechas, self.opcion.value, documento,
                                self.nombre_documento.value + ".pdf", self.carpeta.value)


'''
CLASE BOTON_GRAFICA_ESTUDIANTE

La clase representa el botón empleado para ejecutar la opción encargada de generar las gráficas correspondientes a una 
de las opciones de análisis de la información obtenida de los test realizados por los alumnos.

  - estudiante: objeto de tipo SelectMultiple de la libreria ipywidgets con los estudiantes seleccionados para los 
  cuales se quiere ejecutar el análisis.
  - diccionario_estudiantes: Diccionario con los estudiantes y sus test realizados. La clave del diccionario es el 
  identificador del estudiante y para cada clave su valor es un diccionario con los test. Este segundo diccionario tiene 
  como clave el tema al que pertenecen los test y para cada clave su valor es un array que contiene los test realizados 
  por los estudiantes.
  - seleccion_temas: objeto de tipo SelectMultiple de la libreria ipywidgets con los temas seleccionados para los cuales 
  se quiere ejecutar el análisis.
  - seleccion_fechas: objeto de tipo SelectMultiple de la libreria ipywidgets con los intervalos de fechas seleccionados 
  para los cuales se quiere ejecutar el análisis.
  - fechas: Array donde se van a almacenar los intervalos de fechas seleccionados.
  - opcion: Objeto de tipo RadioButtons de la libreria ipywidgets con la opción para el tipo de análisis que queremos 
  realizar sobre los test realizados por el estudiante (Evolución para cada uno de los temas para una serie de 
  intervalos de fechas o comparativa de una serie de temas para una serie de intervalos de fechas)
  - opcion2: Objeto de tipo RadioButtons de la libreria ipywidgets con el valor para el cual se quiere realizar el 
  ranking (Nota media de los test, número de veces que se ha completado el test, número de veces que se ha aprobado el 
  test y porcentaje de aprobados)
  - color: Color seleccionado para las barras de la gráfica.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.
  - diseno: Opción para el diseño de la gráfica

Cuando se pulsa el botón se ejecuta, para cada uno de los estudiantes seleccionados, una de entre dos opciones de 
gráficas para el analísis de datos obtenidos a partir de los test realizados or los alumnos:
  - fecha x tema: Se muestra para cada uno de los temas seleccionados una gráfica comparando el valor seleccionado para 
  los intervalos de fecha deseados.
  - tema x fecha: Se muestra para cara uno de los interalos de fecha deseados una gráfica comparando el valor 
  seleccionado para los temas.
'''


class Boton_grafica_estudiante:

    def __init__(self, d_e, s_t, s_f, fs, opcion, estudiante, opcion2, color, diseno):
        self.estudiante = estudiante
        self.diccionario_estudiantes = d_e
        self.seleccion_temas = s_t
        self.seleccion_fechas = s_f
        self.fechas = fs
        self.opcion = opcion
        self.opcion2 = opcion2
        self.color = color
        self.button = widgets.Button(description="Aceptar")
        self.button.on_click(self.on_button_clicked)
        self.diseno = diseno

    def on_button_clicked(self, b):
        Grafica_estudiante(self.estudiante.value, self.diccionario_estudiantes, self.seleccion_temas.value,
                           self.seleccion_fechas.value, self.fechas, self.opcion.value, self.opcion2.value,
                           self.color.value, self.diseno.value)


'''
CLASE BOTON_GRAFICA_ESTUDIANTE_PDF

La clase representa el botón empleado para ejecutar la opción encargada de
generar un documento PDF con las gráficas correspondientes a una de las opciones de análisis de la información obtenida 
de los test realizados por los alumnos.

  - estudiante: objeto de tipo SelectMultiple de la libreria ipywidgets con los estudiantes seleccionados para los 
  cuales se quiere ejecutar el análisis.
  - diccionario_estudiantes: Diccionario con los estudiantes y sus test realizados. La clave del diccionario es el 
  identificador del estudiante y para cada clave su valor es un diccionario con los test. Este segundo diccionario tiene 
  como clave el tema al que pertenecen los test y para cada clave su valor es un array que contiene los test realizados 
  por los estudiantes.
  - seleccion_temas: objeto de tipo SelectMultiple de la libreria ipywidgets con los temas seleccionados para los cuales 
  se quiere ejecutar el análisis.
  - seleccion_fechas: objeto de tipo SelectMultiple de la libreria ipywidgets con los intervalos de fechas seleccionados 
  para los cuales se quiere ejecutar el análisis.
  - fechas: Array donde se van a almacenar los intervalos de fechas seleccionados.
  - opcion: Objeto de tipo RadioButtons de la libreria ipywidgets con la opción para el tipo de análisis que queremos 
  realizar sobre los test realizados por el estudiante (Evolución para cada uno de los temas para una serie de 
  intervalos de fechas o comparativa de una serie de temas para una serie de intervalos de fechas)
  - opcion2: Objeto de tipo RadioButtons de la libreria ipywidgets con el valor para el cual se quiere realizar el 
  ranking (Nota media de los test, número de veces que se ha completado el test, número de veces que se ha aprobado el 
  test y porcentaje de aprobados)
  - color: Color seleccionado para las barras de la gráfica.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.
  - nombre_documento: Nombre del documento.
  - carpeta: Carpeta destino para el documento a descargar
  - carpeta2: Carpeta destino para la gráfica a descargar
  - diseno: Opción para el diseño de la gráfica

Cuando se pulsa el botón se genera un documento PDF con, para cada uno de los estudiantes seleccionados, las gráficas 
correspondientes a una de entre las dos opciones para el análisis de datos obtenidos a partir de los test realizados or 
los alumnos:
  - fecha x tema: Se muestra para cada uno de los temas seleccionados una gráfica comparando el valor seleccionado para 
  los intervalos de fecha deseados.
  - tema x fecha: Se muestra para cara uno de los interalos de fecha deseados una gráfica comparando el valor 
  seleccionado para los temas.
'''


class Boton_grafica_estudiante_pdf:

    def __init__(self, d_e, s_t, s_f, fs, opcion, estudiante, opcion2, color, nombre_documento, carpeta,
                 diseno):
        self.estudiante = estudiante
        self.diccionario_estudiantes = d_e
        self.seleccion_temas = s_t
        self.seleccion_fechas = s_f
        self.fechas = fs
        self.opcion = opcion
        self.opcion2 = opcion2
        self.color = color

        self.button = widgets.Button(description="Descargar")
        self.button.on_click(self.on_button_clicked)

        self.nombre_documento = nombre_documento
        self.carpeta = carpeta
        self.diseno = diseno

    def on_button_clicked(self, b):
        documento = canvas.Canvas(self.nombre_documento.value + ".pdf")
        documento.setPageSize(A4)

        Grafica_estudiante_pdf(self.estudiante.value, self.diccionario_estudiantes, self.seleccion_temas.value,
                               self.seleccion_fechas.value, self.fechas, self.opcion.value, self.opcion2.value,
                               self.color.value, documento, self.nombre_documento.value + ".pdf", self.carpeta.value,
                               self.diseno.value)


'''
CLASE BOTON_REGISTROS

La clase representa el botón empleado para cargar los ficheros correspondientes con la información de los registros 
de acceso de los alumnos.

  - diccionario_registros: Diccionario con los estudiantes y sus registros de acceso. La clave del diccionario es el 
  identificador del estudiante y para cada clave su valor es un array de objetos de tipo Registros.
  - carpeta: Ubicación del fichero que se quiere cargar.
  - uploader: Objeto de la librería ipywidgets que contiene el fichero seleccionado cuya información se quiere cargar.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.


Cuando se pulsa el botón se ejecuta la funcion encargada de leer el contenido del fichero y cargar la información 
(objetos de tipo Registros) en los diccionarios con los que trabajamos.
Una vez se ha cargado la información correctamente se da al usuario la opción de repetir el proceso añadiendo un nuevo 
fichero.

'''


class Boton_registros:

    def __init__(self, uploader, diccionario_registros):
        self.diccionario_registros = diccionario_registros
        self.uploader = uploader
        self.button = widgets.Button(description="Aceptar")
        self.button.on_click(self.on_button_clicked)

    def on_button_clicked(self, b):

        if self.uploader.selected is None:
            text = 'Seleccione el fichero que desea leer'
            myLabel = widgets.HTML(value=f"<b><font color='red'>{text}</b>")
            box_layout = widgets.Layout(display='flex',
                                        flex_flow='column',
                                        align_items='center',
                                        border='solid',
                                        width='25%',
                                        margin='1%')
            items = [myLabel]
            box = widgets.Box(children=items, layout=box_layout)
            display(box)
        else:
            self.button.layout.visibility = 'hidden'

            '''if self.carpeta.value != '':
                fichero = os.path.join(self.carpeta.value, list(self.uploader.value.keys())[0])
            else:
                fichero = list(self.uploader.value.keys())[0]
            '''
            fichero = fichero = self.uploader.selected
            self.diccionario_registros = fichero_registros(fichero, self.diccionario_registros)

            if self.diccionario_registros is None:

                text = 'No se ha encontrado el fichero en la ruta indicada.'
                myLabel = widgets.HTML(value=f"<b><font color='red'>{text}</b>")
                box_layout = widgets.Layout(display='flex',
                                            flex_flow='column',
                                            align_items='center',
                                            border='solid',
                                            width='30%',
                                            margin='1%')
                items = [myLabel]
                box = widgets.Box(children=items, layout=box_layout)
                display(box)

            else:
                p = widgets.Label(value="¿Desea añadir otro fichero?")
                display(p)

                b = widgets.HBox()

                botons = Boton_registros_s(self.uploader, self.diccionario_registros, b)
                # display(botons.button)

                botonn = Boton_ficheros_n(b)
                # display(botonn.button)

                botones = [botons.button, botonn.button]

                b.children = [i for i in botones]
                display(b)


'''
CLASE BOTON_REGISTROS_S

La clase representa el botón empleado para repetir el proceso de cargar los ficheros con los registros de acceso de los 
alumnos.

  - box: objeto de tipo HBox de la librería ipywidgets que contiene un objeto de tipo Boton_registros_s y otro objeto de 
  tipo Boton_registros_n.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.
  - diccionario_registros: Diccionario con los estudiantes y sus registros de acceso. La clave del diccionario es el 
  identificador del estudiante y para cada clave su valor es un array de objetos de tipo Registros.
  - uploader: Objeto de la librería ipywidgets que contiene el fichero seleccionado cuya información se quiere cargar.

Cuando se pulsa el botón se muestrá un objeto de tipo Boton_registros para continuar la ejecución.
'''


class Boton_registros_s:

    def __init__(self, uploader, diccionario_registros, b):
        self.box = b
        self.button = widgets.Button(description="Si")
        self.button.on_click(self.on_button_clicked)
        self.diccionario_registros = diccionario_registros
        self.uploader = uploader

    def on_button_clicked(self, b):
        '''p = widgets.Label(value="AVISO: Los ficheros se cargan desde la raíz de la carpeta.")
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
        display(carpeta)'''

        uploader = FileChooser()
        # uploader = widgets.FileUpload()

        # elegir_tema(tema, uploader)
        p = widgets.Label(value="Introduce el tema al que se corresponde el fichero: ")
        display(p)
        display(uploader)

        boton = Boton_registros(uploader, self.diccionario_registros)
        self.box.layout.visibility = 'hidden'
        display(boton.button)


'''
CLASE BOTON_REGISTROS_N

La clase representa el botón empleado para finalizar el proceso de cargar los ficheros con los registros de acceso de 
los estudiantes.

  - box: objeto de tipo HBox de la librería ipywidgets que contiene un objeto de tipo Boton_registros_s y otro objeto de 
  tipo Boton_registros_n.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.

Cuando se pulsa el botón se oculta el objeto de tipo Boton_registros_s para impedir que se continue la ejecución.
'''


class Boton_registros_n:

    def __init__(self, b):
        self.box = b
        self.button = widgets.Button(description="No")
        self.button.on_click(self.on_button_clicked)

    def on_button_clicked(self, b):
        self.box.layout.visibility = 'hidden'
        p = widgets.Label(value="Lectura Finalizada")
        display(p)


'''
CLASE BOTON_GRAFICA_REGISTROS

La clase representa el botón empleado para ejecutar la opción encargada de generar las gráficas correspondientes 
al análisis de la información obtenida de los registros de acceso de los estudiantes a Moodle.

    - identificador: Objeto de tipo Text de la libreria ipywidgets para indicar el identificador del recurso de Moodle 
    cuya información se desea obtener.
    - estudiante: objeto de tipo SelectMultiple de la libreria ipywidgets con los estudiantes seleccionados para los 
  cuales se quiere ejecutar el análisis.
  - diccionario_registros: Diccionario con los estudiantes y sus registros de acceso a Moodle. La clave del diccionario 
  es el identificador del estudiante. Para cada clave su valor es un array con objetos de tipo 'Registro' que contienen los accesos a Moodle del estudiante 
  para cada uno de los temas en una semana en concreto
  - seleccion_fechas: objeto de tipo SelectMultiple de la libreria ipywidgets con los intervalos de fechas seleccionados 
  para los cuales se quiere ejecutar el análisis.
  - fechas: Array donde se van a almacenar los intervalos de fechas seleccionados.
  - color: Color seleccionado para las barras de la gráfica.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.
  - diseno: Opción para el diseño de la gráfica

Cuando se pulsa el botón se realiza, para cada uno de los estudiantes seleccionados o para el grupo en general,
el análisis de sus registros de acceso a la plataforma Moodle.
'''


class Boton_grafica_registros:

    def __init__(self, identificador, d_r, s_f, fs, estudiante, color, IP, diseno):
        self.identificador = identificador
        self.estudiante = estudiante
        self.diccionario_registros = d_r
        self.seleccion_fechas = s_f
        self.fechas = fs
        self.color = color
        self.button = widgets.Button(description="Aceptar")
        self.button.on_click(self.on_button_clicked)
        self.IP = IP
        self.diseno = diseno

    def on_button_clicked(self, b):
        Grafica_registros(self.identificador.value, self.diccionario_registros, self.seleccion_fechas.value,
                          self.fechas, self.estudiante.value,
                          self.color.value, self.IP.value, self.diseno.value)


'''
CLASE BOTON_GRAFICA_REGISTROS_PDF

La clase representa el botón empleado para ejecutar la opción encargada de generar e imprimir en un documento PDF 
las gráficas correspondientes al análisis de la información obtenida de los registros de acceso de los estudiantes a 
Moodle.

    - identificador: Objeto de tipo Text de la libreria ipywidgets para indicar el identificador del recurso de Moodle 
    cuya información se desea obtener.
    - estudiante: objeto de tipo SelectMultiple de la libreria ipywidgets con los estudiantes seleccionados para los 
  cuales se quiere ejecutar el análisis.
  - diccionario_registros: Diccionario con los estudiantes y sus registros de acceso a Moodle. La clave del diccionario 
  es el identificador del estudiante. Para cada clave su valor es un array con objetos de tipo 'Registro' que contienen 
  los accesos a Moodle del estudiante.
  - seleccion_fechas: objeto de tipo SelectMultiple de la libreria ipywidgets con los intervalos de fechas seleccionados 
  para los cuales se quiere ejecutar el análisis.
  - fechas: Array donde se van a almacenar los intervalos de fechas seleccionados.
  - color: Color seleccionado para las barras de la gráfica.
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.
  - nombre_documento: Nombre del documento.
  - carpeta: Carpeta destino para el documento a descargar
  - carpeta2: Carpeta destino para la gráfica a descargar
  - diseno: Opción para el diseño de la gráfica

Cuando se pulsa el botón se realiza para cada uno de los estudiantes seleccionados o para el grupo en general,
el análisis de sus registros de acceso a la plataforma Moodle.
'''


class Boton_grafica_registros_pdf:

    def __init__(self, identificador, d_r, s_f, fs, estudiante, color, nombre_documento, carpeta, IP,
                 diseno):
        self.identificador = identificador
        self.estudiante = estudiante
        self.diccionario_registros = d_r
        self.seleccion_fechas = s_f
        self.fechas = fs
        self.color = color
        self.button = widgets.Button(description="Descargar")
        self.button.on_click(self.on_button_clicked)

        self.nombre_documento = nombre_documento
        self.carpeta = carpeta
        self.IP = IP
        self.diseno = diseno

    def on_button_clicked(self, b):
        documento = canvas.Canvas(self.nombre_documento.value + ".pdf")
        documento.setPageSize(A4)

        Grafica_registros_pdf(self.identificador.value, self.diccionario_registros, self.seleccion_fechas.value,
                              self.fechas, self.estudiante.value,
                              self.color.value, documento, self.nombre_documento.value + ".pdf", self.carpeta.value,
                              self.IP.value, self.diseno.value)


'''
CLASE BOTON_GRAFICAS_COMPARACION

La clase representa el botón empleado para generar las gráficas comparativas correspondientes a una de las opciones de 
análisis de la información obtenida de los test realizados por los alumnos.

  - seleccion_fechas: bjeto de tipo SelectMultiple de la libreria ipywidgets con los intervalos de fechas seleccionados 
  para los cuales se quiere ejecutar el análisis.
  - fechas: Array donde se van a almacenar los intervalos de fechas seleccionados.
  - color: Color deseado para las barras de la gráfica.
  - opcion2: Opción para el valor que se desea mostrar en las gráficas (nota media, test finalizados, test aprobados o 
    porcentaje de aprobados).
  - button: objeto de tipo Button de la librería ipywidgets que representa el botón.
  - diseno: opción para el diseño de la gráfica

'''


class Boton_graficas_comparacion:

    def __init__(self, s_f, fs, opcion2, diseno, ficheros, documentos):
        self.opcion2 = opcion2
        self.seleccion_fechas = s_f
        self.fechas = fs
        self.button = widgets.Button(description="Aceptar")
        self.button.on_click(self.on_button_clicked)
        self.diseno = diseno
        self.ficheros = ficheros
        self.documentos = documentos

    def on_button_clicked(self, b):
        Grafica_test_comparacion(self.seleccion_fechas.value, self.fechas, self.opcion2.value,
                                 self.diseno.value, self.ficheros.value, self.documentos)

    '''
    CLASE BOTON_GRAFICAS_COMPARACION_PDF

    La clase representa el botón empleado para generar las gráficas comparativas de los resultados obtenidos de los test
    realizados por los alumnos.

      - seleccion_fechas: bjeto de tipo SelectMultiple de la libreria ipywidgets con los intervalos de fechas seleccionados 
      para los cuales se quiere ejecutar el análisis.
      - fechas: Array donde se van a almacenar los intervalos de fechas seleccionados.
      - opcion2: Opción para el valor que se desea mostrar en las gráficas (nota media, test finalizados, test aprobados o 
        porcentaje de aprobados).
      - diseno: opción para el diseño de la gráfica
      - ficheros: ficheros seleccionados para los cuales se desea realizar la comparación.
      . documentos: Array con los documentos añadidos a la herramienta.
      - nombre_documento: Nombre del documento.
      - carpeta: Carpeta destino para el documento a descargar
      - carpeta2: Carpeta destino para la gráfica a descargar

    '''


class Boton_graficas_comparacion_PDF:

    def __init__(self, s_f, fs, opcion2, diseno, ficheros, documentos, nombre_documento, carpeta):
        self.opcion2 = opcion2
        self.seleccion_fechas = s_f
        self.fechas = fs
        self.button = widgets.Button(description="Descargar")
        self.button.on_click(self.on_button_clicked)
        self.diseno = diseno
        self.ficheros = ficheros
        self.documentos = documentos
        self.nombre_documento = nombre_documento
        self.carpeta = carpeta

    def on_button_clicked(self, b):
        documento = canvas.Canvas(self.nombre_documento.value + ".pdf")
        documento.setPageSize(A4)

        Grafica_test_comparacion_PDF(self.seleccion_fechas.value, self.fechas, self.opcion2.value,
                                     self.diseno.value, self.ficheros.value, self.documentos,
                                     documento, self.nombre_documento.value + ".pdf", self.carpeta.value)
