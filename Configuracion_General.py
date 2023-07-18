from Clases_Botones import *
import ipywidgets as widgets

'''
def configuracion(diccionario_tema, diccionario_estudiantes, diccionario_registros, documentos, fechas): 
Función encargada de generar las opciones de configuración y ejecución del notebook.
  - Argumentos:
    - diccionario_tema: Diccionario que contiene los tests realizados por los estudiantes para cada uno de los temas 
    (la clave son los temas de los test y su valor un array con los test realizados por los estudiantes).
    - diccionario_estudiantes: Diccionario con los estudiantes y sus test realizados. La clave del diccionario es el 
    identificador del estudiante y para cada clave su valor es un diccionario con los test. Este segundo diccionario 
    tiene como clave el tema al que pertenecen los test y para cada clave su valor es un array que contiene los test 
    realizados por los estudiantes.
    - diccionario_registros: Diccionario con los estudiantes y sus registros de acceso a Moodle. La clave del diccionario 
  es el identificador del estudiante. Para cada clave su valor es un array con objetos de tipo 'Registro' que contienen 
  los accesos a Moodle del estudiante.
    - documentos: Array con los nombres de los documentos leídos con los test realizados por los alumnos.
    - fechas: Array con los intervalos de fechas.
'''


def configuracion(diccionario_tema, diccionario_estudiantes, documentos, fechas):

    if (diccionario_tema == {} and diccionario_estudiantes == {}) or (len(fechas) < 1):

        text = 'Es necesario, antes de usar la herramienta, la lectura de datos y de intervalos de fechas'
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

        titulo_fechas = widgets.HTML(value=f"<b>SELECCIÓN DE FECHAS:</b>")

        fechas_s = ["Todos"]
        for f in fechas:
            fechas_s.append(str(f[0]).split(' ')[0] + " / " + str(f[1]).split(' ')[0])

        seleccion_fechas = widgets.SelectMultiple(
            options=fechas_s,
            value=['Todos'],
            # rows=10,
            description='Fechas',
            disabled=False
        )

        titulo_temas = widgets.HTML(value=f"<b>SELECCIÓN DE TEMAS:</b>")

        temas = ["Todos"]
        for k in diccionario_tema.keys():
            temas.append(k)

        seleccion_temas = widgets.SelectMultiple(
            options=temas,
            value=['Todos'],
            # rows=10,
            description='Temas',
            disabled=False
        )

        titulo_ejecucion = widgets.HTML(value=f"<b>OPCIONES DE EJECUCIÓN:</b>")

        titulo_documento = widgets.HTML(value=f"<b>NOMBRE DOCUMENTO PDF:</b>")

        pdf = widgets.Text(
            value='',
            placeholder='Documento',
            description='Documento:',
            disabled=False
        )

        aviso = widgets.Label(value="AVISO: El fichero se guardará en la raíz de la carpeta.")

        titulo_carpeta = widgets.HTML(value=f"<b>CARPETA DESCARGA PDF:</b>")

        aviso_carpeta = widgets.Label(value="Ejemplo:C:\\Users\\user\\Documents\\Archivos")

        carpeta = widgets.Text(
            value='',
            placeholder='Carpeta',
            description='Carpeta:',
            disabled=False
        )

        titulo_ranking = widgets.HTML(value=f"<b>OPCIONES DE RANKING:</b>")

        titulo_grafica = widgets.HTML(value=f"<b>OPCIONES DE GRÁFICA:</b>")

        titulo_color_grafica = widgets.HTML(value=f"<b>COLOR DE GRÁFICA:</b>")

        color_grafica = widgets.Label(value="Escoge un color.")

        color = widgets.ColorPicker(
            concise=False,
            description='Color',
            value='blue',
            disabled=False
        )

        diseno_grafica = widgets.HTML(value=f"<b>DISEÑO DE GRÁFICA:</b>")

        opcion_grafica = widgets.Dropdown(
            options=[('Barras Verticales', 1), ('Diagrama de líneas', 2)],
            value=1,
            description='Tipo de Gráfica:',
        )

        '''titulo_carpeta_grafica = widgets.HTML(value=f"<b>CARPETA DESCARGA GRÁFICAS:</b>")
    
        aviso_carpeta_grafica = widgets.Label(value="Ejemplo:C:\\Users\\user\\Documents\\Archivos")
    
        carpeta2 = widgets.Text(
            value='',
            placeholder='Carpeta',
            description='Carpeta:',
            disabled=False
        )'''

        ids = ['Todos']

        for id in diccionario_estudiantes.keys():
            ids.append(id)

        estudiantes = widgets.SelectMultiple(
            options=ids,
            value=['Todos'],
            # rows=10,
            description='Estudiantes',
            disabled=False
        )

        titulo_estudiantes = widgets.HTML(value=f"<b>SELECCIÓN DE ESTUDIANTES:</b>")

        titulo_identificador = widgets.HTML(value=f"<b>IDENTIFICADOR DE REGISTRO:</b>")

        # -----------------------------------------------------------------------------

        b1 = widgets.VBox()
        box1 = []

        '''text = "SELECCIÓN DE FECHAS"
        titulo = widgets.HTML(value=f"<b>{text}</b>")
        box1.append(titulo)'''
        box1.append(titulo_fechas)

        box1.append(seleccion_fechas)

        '''text = "SELECCIÓN DE TEMAS"
        titulo = widgets.HTML(value=f"<b>{text}</b>")'''

        box1.append(titulo_temas)

        '''temas = ["Todos"]
        for k in diccionario_tema.keys():
            temas.append(k)
    
        seleccion_temas = widgets.SelectMultiple(
            options=temas,
            value=['Todos'],
            # rows=10,
            description='Temas',
            disabled=False
        )'''

        box1.append(seleccion_temas)

        '''text = "OPCIONES DE EJECUCIÓN"
        titulo_b = widgets.HTML(value=f"<b>{text}</b>")'''

        opciones = widgets.RadioButtons(
            options=['Temas x Fecha', 'Fecha x Temas'],
            layout={'width': 'max-content'},  # If the items' names are long
            disabled=False
        )

        box1.append(titulo_ejecucion)
        box1.append(opciones)

        boton = Boton_proceso_temafecha(diccionario_tema, seleccion_temas, seleccion_fechas, fechas, opciones)
        box1.append(boton.button)

        '''text = "NOMBRE DOCUMENTO PDF"
        titulo = widgets.HTML(value=f"<b>{text}</b>")'''

        '''pdf = widgets.Text(
            value='',
            placeholder='Documento',
            description='Documento:',
            disabled=False
        )'''

        box1.append(titulo_documento)
        box1.append(pdf)

        '''p = widgets.Label(value="AVISO: El fichero se guardará en la raíz de la carpeta.")'''

        '''text = "CARPETA DESCARGA"
        titulo = widgets.HTML(value=f"<b>{text}</b>")
    
        p = widgets.Label(value="Ejemplo:C:\\Users\\user\\Documents\\Archivos")'''

        '''carpeta = widgets.Text(
            value='',
            placeholder='Carpeta',
            description='Carpeta:',
            disabled=False
        )'''

        box1.append(titulo_carpeta)
        box1.append(aviso)
        box1.append(aviso_carpeta)
        box1.append(carpeta)

        boton2 = Boton_proceso_temafecha_pdf(diccionario_tema, seleccion_temas, seleccion_fechas, fechas, opciones, pdf,
                                             carpeta)
        box1.append(boton2.button)

        b1.children = [i for i in box1]

        # -------------------------------------------------------------------------------

        b2 = widgets.VBox()
        box2 = []

        '''text = "SELECCIÓN DE FECHAS"
        titulo = widgets.HTML(value=f"<b>{text}</b>")'''

        '''fechas_s = ["Todos"]
        for f in fechas:
            fechas_s.append(str(f[0]).split(' ')[0] + " / " + str(f[1]).split(' ')[0])
    
        seleccion_fechas = widgets.SelectMultiple(
            options=fechas_s,
            value=['Todos'],
            # rows=10,
            description='Fechas',
            disabled=False
        )'''

        box2.append(titulo_fechas)
        box2.append(seleccion_fechas)

        '''text = "OPCIONES DE RANKING"
        titulo_b = widgets.HTML(value=f"<b>{text}</b>")'''

        opciones = widgets.RadioButtons(
            options=['Nota Media', 'Participacion', 'Aprobados', '% Aprobados'],
            #    value='pineapple', # Defaults to 'pineapple'
            layout={'width': 'max-content'},  # If the items' names are long
            disabled=False
        )

        box2.append(titulo_ranking)
        box2.append(opciones)

        boton = Boton_proceso_ranking(diccionario_tema, seleccion_fechas, fechas, opciones)
        box2.append(boton.button)

        '''text = "NOMBRE DOCUMENTO PDF"
        titulo = widgets.HTML(value=f"<b>{text}</b>")'''

        '''pdf = widgets.Text(
            value='',
            placeholder='Documento',
            description='Documento:',
            disabled=False
        )'''

        box2.append(titulo_documento)
        box2.append(pdf)

        '''p = widgets.Label(value="AVISO: El fichero se guardará en la raíz de la carpeta.")'''
        box2.append(aviso)

        '''text = "CARPETA DESCARGA"
        titulo = widgets.HTML(value=f"<b>{text}</b>")
    
        p = widgets.Label(value="Ejemplo:C:\\Users\\user\\Documents\\Archivos")'''

        '''carpeta = widgets.Text(
            value='',
            placeholder='Carpeta',
            description='Carpeta:',
            disabled=False
        )'''

        box2.append(titulo_carpeta)
        box2.append(aviso_carpeta)
        box2.append(carpeta)

        boton2 = Boton_proceso_ranking_pdf(diccionario_tema, seleccion_fechas, fechas, opciones, pdf, carpeta)
        box2.append(boton2.button)

        b2.children = [i for i in box2]

        # -------------------------------------------------------------------------------

        b3 = widgets.VBox()
        box3 = []

        '''text = "SELECCIÓN DE FECHAS"
        titulo = widgets.HTML(value=f"<b>{text}</b>")'''

        '''fechas_s = ["Todos"]
        for f in fechas:
            fechas_s.append(str(f[0]).split(' ')[0] + " / " + str(f[1]).split(' ')[0])
    
        seleccion_fechas = widgets.SelectMultiple(
            options=fechas_s,
            value=['Todos'],
            # rows=10,
            description='Fechas',
            disabled=False
        )'''

        box3.append(titulo_fechas)
        box3.append(seleccion_fechas)

        '''text = "SELECCIÓN DE TEMAS"
        titulo = widgets.HTML(value=f"<b>{text}</b>")'''

        '''temas = ["Todos"]
        for k in diccionario_tema.keys():
            temas.append(k)
    
        seleccion_temas = widgets.SelectMultiple(
            options=temas,
            value=['Todos'],
            # rows=10,
            description='Temas',
            disabled=False
        )'''

        box3.append(titulo_temas)
        box3.append(seleccion_temas)

        '''text = "OPCIONES DE EJECUCIÓN"
        titulo_b = widgets.HTML(value=f"<b>{text}</b>")'''

        opciones = widgets.RadioButtons(
            options=['Fecha x Temas', 'Temas x Fecha'],
            #    value='pineapple', # Defaults to 'pineapple'
            layout={'width': 'max-content'},  # If the items' names are long
            disabled=False
        )

        box3.append(titulo_ejecucion)
        box3.append(opciones)

        '''text = "OPCIONES DE GRÁFICA"
        titulo_b = widgets.HTML(value=f"<b>{text}</b>")'''

        opciones2 = widgets.RadioButtons(
            options=['Nota Media', 'Participacion', 'Aprobados', '% Aprobados'],
            #    value='pineapple', # Defaults to 'pineapple'
            layout={'width': 'max-content'},  # If the items' names are long
            disabled=False
        )

        box3.append(titulo_grafica)
        box3.append(opciones2)

        box3.append(diseno_grafica)
        box3.append(opcion_grafica)

        '''text = "COLOR DE GRÁFICA"
        titulo_b = widgets.HTML(value=f"<b>{text}</b>")'''

        '''p = widgets.Label(value="Escoge un color.")
        color = widgets.ColorPicker(
            concise=False,
            description='Color',
            value='blue',
            disabled=False
        )'''

        box3.append(titulo_color_grafica)
        box3.append(color_grafica)
        box3.append(color)

        boton = Boton_graficas(diccionario_tema, seleccion_temas, seleccion_fechas, fechas, opciones, opciones2, color,
                               opcion_grafica)
        box3.append(boton.button)

        '''text = "NOMBRE DOCUMENTO PDF"
        titulo = widgets.HTML(value=f"<b>{text}</b>")'''

        '''pdf = widgets.Text(
            value='',
            placeholder='Documento',
            description='Documento:',
            disabled=False
        )'''

        box3.append(titulo_documento)
        box3.append(pdf)


        box3.append(aviso)

        '''text = "CARPETA DESCARGA PDF"
        titulo = widgets.HTML(value=f"<b>{text}</b>")
        p = widgets.Label(value="Ejemplo:C:\\Users\\user\\Documents\\Archivos")'''

        box3.append(titulo_carpeta)
        box3.append(aviso_carpeta)

        '''carpeta = widgets.Text(
            value='',
            placeholder='Carpeta',
            description='Carpeta:',
            disabled=False
        )'''

        box3.append(carpeta)

        '''text = "CARPETA DESCARGA GRÁFICAS"
        titulo = widgets.HTML(value=f"<b>{text}</b>")
        p = widgets.Label(value="Ejemplo:C:\\Users\\user\\Documents\\Archivos")'''

        '''box3.append(titulo_carpeta_grafica)
        box3.append(aviso_carpeta_grafica)'''

        '''carpeta2 = widgets.Text(
            value='',
            placeholder='Carpeta',
            description='Carpeta:',
            disabled=False
        )'''

        # box3.append(carpeta2)

        boton2 = Boton_graficas_pdf(diccionario_tema, seleccion_temas, seleccion_fechas, fechas, opciones, opciones2,
                                    color, pdf, carpeta, opcion_grafica)
        box3.append(boton2.button)

        b3.children = [i for i in box3]

        # -------------------------------------------------------------------------------

        b4 = widgets.VBox()
        box4 = []

        '''text = "SELECCIÓN DE FECHAS"
        titulo = widgets.HTML(value=f"<b>{text}</b>")'''

        '''fechas_s = ["Todos"]
        for f in fechas:
            fechas_s.append(str(f[0]).split(' ')[0] + " / " + str(f[1]).split(' ')[0])
    
        seleccion_fechas = widgets.SelectMultiple(
            options=fechas_s,
            value=['Todos'],
            # rows=10,
            description='Fechas',
            disabled=False
        )'''

        box4.append(titulo_fechas)
        box4.append(seleccion_fechas)

        '''text = "SELECCIÓN DE TEMAS"
        titulo = widgets.HTML(value=f"<b>{text}</b>")'''

        '''temas = ["Todos"]
        for k in diccionario_tema.keys():
            temas.append(k)
    
        seleccion_temas = widgets.SelectMultiple(
            options=temas,
            value=['Todos'],
            # rows=10,
            description='Temas',
            disabled=False
        )'''

        box4.append(titulo_temas)
        box4.append(seleccion_temas)

        '''text = "SELECCIÓN DE ESTUDIANTES:"
        titulo_b = widgets.HTML(value=f"<b>{text}</b>")'''

        '''ids = ["Todos"]
        for id in diccionario_estudiantes.keys():
            ids.append(id)'''

        '''estudiantes = widgets.SelectMultiple(
            options=ids,
            value=['Todos'],
            # rows=10,
            description='Estudiantes',
            disabled=False
        )'''

        box4.append(titulo_estudiantes)
        box4.append(estudiantes)

        '''text = "OPCIONES DE EJECUCIÓN"
        titulo_b = widgets.HTML(value=f"<b>{text}</b>")'''

        opciones = widgets.RadioButtons(
            options=['Temas x Fechas', 'Fechas x Temas'],
            #    value='pineapple', # Defaults to 'pineapple'
            layout={'width': 'max-content'},  # If the items' names are long
            disabled=False
        )

        box4.append(titulo_ejecucion)
        box4.append(opciones)

        boton = Boton_estudiantes(diccionario_estudiantes, seleccion_temas, seleccion_fechas, fechas, opciones, estudiantes)
        box4.append(boton.button)

        '''text = "NOMBRE DOCUMENTO PDF"
        titulo = widgets.HTML(value=f"<b>{text}</b>")'''

        '''pdf = widgets.Text(
            value='',
            placeholder='Documento',
            description='Documento:',
            disabled=False
        )'''

        box4.append(titulo_documento)
        box4.append(pdf)

        '''p = widgets.Label(value="AVISO: El fichero se guardará en la raíz de la carpeta.")'''
        box4.append(aviso)

        '''text = "CARPETA DESCARGA"
        titulo = widgets.HTML(value=f"<b>{text}</b>")
    
        p = widgets.Label(value="Ejemplo:C:\\Users\\user\\Documents\\Archivos")'''

        '''carpeta = widgets.Text(
            value='',
            placeholder='Carpeta',
            description='Carpeta:',
            disabled=False
        )'''

        box4.append(titulo_carpeta)
        box4.append(aviso_carpeta)
        box4.append(carpeta)

        boton2 = Boton_estudiantes_pdf(diccionario_estudiantes, seleccion_temas, seleccion_fechas, fechas, opciones,
                                       estudiantes, pdf, carpeta)
        box4.append(boton2.button)

        b4.children = [i for i in box4]

        # -------------------------------------------------------------------------------
        b5 = widgets.VBox()
        box5 = []

        '''text = "SELECCIÓN DE FECHAS"
        titulo = widgets.HTML(value=f"<b>{text}</b>")'''

        '''fechas_s = ["Todos"]
        for f in fechas:
            fechas_s.append(str(f[0]).split(' ')[0] + " / " + str(f[1]).split(' ')[0])
    
        seleccion_fechas = widgets.SelectMultiple(
            options=fechas_s,
            value=['Todos'],
            # rows=10,
            description='Fechas',
            disabled=False
        )'''

        box5.append(titulo_fechas)
        box5.append(seleccion_fechas)

        '''text = "SELECCIÓN DE ESTUDIANTES:"
        titulo_b = widgets.HTML(value=f"<b>{text}</b>")'''

        '''ids = ["Todos"]
    
        for id in diccionario_estudiantes.keys():
            ids.append(id)'''

        '''estudiantes = widgets.SelectMultiple(
            options=ids,
            value=['Todos'],
            # rows=10,
            description='Estudiantes',
            disabled=False
        )'''

        box5.append(titulo_estudiantes)
        box5.append(estudiantes)

        '''text = "OPCIONES DE RANKING"
        titulo_b = widgets.HTML(value=f"<b>{text}</b>")'''

        opciones = widgets.RadioButtons(
            options=['Nota Media', 'Participacion', 'Aprobados', '% Aprobados'],
            #    value='pineapple', # Defaults to 'pineapple'
            layout={'width': 'max-content'},  # If the items' names are long
            disabled=False
        )

        box5.append(titulo_ranking)
        box5.append(opciones)

        boton = Boton_ranking_estudiante(diccionario_estudiantes, seleccion_fechas, fechas, opciones, estudiantes)
        box5.append(boton.button)

        '''text = "NOMBRE DOCUMENTO PDF"
        titulo = widgets.HTML(value=f"<b>{text}</b>")'''

        '''pdf = widgets.Text(
            value='',
            placeholder='Documento',
            description='Documento:',
            disabled=False
        )'''

        box5.append(titulo_documento)
        box5.append(pdf)

        '''p = widgets.Label(value="AVISO: El fichero se guardará en la raíz de la carpeta.")'''
        box5.append(aviso)

        '''text = "CARPETA DESCARGA"
        titulo = widgets.HTML(value=f"<b>{text}</b>")
    
        p = widgets.Label(value="Ejemplo:C:\\Users\\user\\Documents\\Archivos")'''

        '''carpeta = widgets.Text(
            value='',
            placeholder='Carpeta',
            description='Carpeta:',
            disabled=False
        )'''

        box5.append(titulo_carpeta)
        box5.append(aviso_carpeta)
        box5.append(carpeta)

        boton2 = Boton_ranking_estudiante_pdf(diccionario_estudiantes, seleccion_fechas, fechas, opciones, estudiantes, pdf,
                                              carpeta)
        box5.append(boton2.button)

        b5.children = [i for i in box5]
        # -------------------------------------------------------------------------------
        b6 = widgets.VBox()
        box6 = []

        '''text = "SELECCIÓN DE TEMAS"
        titulo = widgets.HTML(value=f"<b>{text}</b>")'''

        tms = []

        for k in diccionario_tema.keys():
            temas.append(k)
            tms.append(k)

        '''
        seleccion_temas = widgets.SelectMultiple(
            options=temas,
            value=['Todos'],
            # rows=10,
            description='Temas',
            disabled=False
        )'''

        '''text = "SELECCIÓN DE FECHAS"
        titulo = widgets.HTML(value=f"<b>{text}</b>")'''

        '''fechas_s = ["Todos"]
        for f in fechas:
            fechas_s.append(str(f[0]).split(' ')[0] + " / " + str(f[1]).split(' ')[0])
    
        seleccion_fechas = widgets.SelectMultiple(
            options=fechas_s,
            value=['Todos'],
            # rows=10,
            description='Fechas',
            disabled=False
        )'''

        box6.append(titulo_fechas)
        box6.append(seleccion_fechas)

        box6.append(titulo_temas)
        box6.append(seleccion_temas)

        '''text = "OPCIONES DE RANKING"
        titulo_b = widgets.HTML(value=f"<b>{text}</b>")'''

        opciones = widgets.RadioButtons(
            options=['Nota Media', 'Participacion', 'Aprobados', '% Aprobados'],
            #    value='pineapple', # Defaults to 'pineapple'
            layout={'width': 'max-content'},  # If the items' names are long
            disabled=False
        )

        box6.append(titulo_ranking)
        box6.append(opciones)

        '''ids = []
    
        for id in diccionario_estudiantes.keys():
            ids.append(id)'''

        boton = Boton_ranking_estudiantes(diccionario_estudiantes, seleccion_temas, tms, seleccion_fechas, fechas, opciones)
        box6.append(boton.button)

        '''text = "NOMBRE DOCUMENTO PDF"
        titulo = widgets.HTML(value=f"<b>{text}</b>")'''

        '''pdf = widgets.Text(
            value='',
            placeholder='Documento',
            description='Documento:',
            disabled=False
        )'''

        box6.append(titulo_documento)
        box6.append(pdf)

        '''p = widgets.Label(value="AVISO: El fichero se guardará en la raíz de la carpeta.")'''
        box6.append(aviso)

        '''text = "CARPETA DESCARGA"
        titulo = widgets.HTML(value=f"<b>{text}</b>")
    
        p = widgets.Label(value="Ejemplo:C:\\Users\\user\\Documents\\Archivos")'''

        '''carpeta = widgets.Text(
            value='',
            placeholder='Carpeta',
            description='Carpeta:',
            disabled=False
        )'''

        box6.append(titulo_carpeta)
        box6.append(aviso_carpeta)
        box6.append(carpeta)

        boton2 = Boton_ranking_estudiantes_pdf(diccionario_estudiantes, seleccion_temas, tms, seleccion_fechas, fechas,
                                               opciones, pdf, carpeta)
        box6.append(boton2.button)

        b6.children = [i for i in box6]
        # -------------------------------------------------------------------------------

        b7 = widgets.VBox()
        box7 = []

        '''text = "SELECCIÓN DE FECHAS"
        titulo = widgets.HTML(value=f"<b>{text}</b>")'''

        '''fechas_s = ["Todos"]
        for f in fechas:
            fechas_s.append(str(f[0]).split(' ')[0] + " / " + str(f[1]).split(' ')[0])
    
        seleccion_fechas = widgets.SelectMultiple(
            options=fechas_s,
            value=['Todos'],
            # rows=10,
            description='Fechas',
            disabled=False
        )'''

        box7.append(titulo_fechas)
        box7.append(seleccion_fechas)

        '''text = "SELECCIÓN DE TEMAS"
        titulo = widgets.HTML(value=f"<b>{text}</b>")'''

        '''temas = ["Todos"]
        for k in diccionario_tema.keys():
            temas.append(k)
    
        seleccion_temas = widgets.SelectMultiple(
            options=temas,
            value=['Todos'],
            # rows=10,
            description='Temas',
            disabled=False
        )'''

        box7.append(titulo_temas)
        box7.append(seleccion_temas)

        '''text = "SELECCIÓN DE ESTUDIANTES:"
        titulo_b = widgets.HTML(value=f"<b>{text}</b>")'''

        '''ids = ["Todos"]
    
        for id in diccionario_estudiantes.keys():
            ids.append(id)'''

        '''estudiantes = widgets.SelectMultiple(
            options=ids,
            value=['Todos'],
            # rows=10,
            description='Estudiantes',
            disabled=False
        )'''

        box7.append(titulo_estudiantes)
        box7.append(estudiantes)

        '''text = "OPCIONES DE EJECUCIÓN"
        titulo_b = widgets.HTML(value=f"<b>{text}</b>")'''

        opciones = widgets.RadioButtons(
            options=['Fecha x Temas', 'Temas x Fecha'],
            #    value='pineapple', # Defaults to 'pineapple'
            layout={'width': 'max-content'},  # If the items' names are long
            disabled=False
        )

        box7.append(titulo_ejecucion)
        box7.append(opciones)

        '''text = "OPCIONES DE GRÁFICA"
        titulo_b = widgets.HTML(value=f"<b>{text}</b>")'''

        opciones2 = widgets.RadioButtons(
            options=['Nota Media', 'Participacion', 'Aprobados', '% Aprobados'],
            #    value='pineapple', # Defaults to 'pineapple'
            layout={'width': 'max-content'},  # If the items' names are long
            disabled=False
        )

        box7.append(titulo_grafica)
        box7.append(opciones2)

        box7.append(diseno_grafica)
        box7.append(opcion_grafica)

        '''text = "COLOR DE GRÁFICA"
        titulo_b = widgets.HTML(value=f"<b>{text}</b>")
        p = widgets.Label(value="Escoge un color.")
        color = widgets.ColorPicker(
            concise=False,
            description='Color',
            value='blue',
            disabled=False
        )'''

        box7.append(titulo_color_grafica)
        box7.append(color_grafica)
        box7.append(color)

        boton = Boton_grafica_estudiante(diccionario_estudiantes, seleccion_temas, seleccion_fechas, fechas, opciones,
                                         estudiantes, opciones2, color, opcion_grafica)
        box7.append(boton.button)

        '''text = "NOMBRE DOCUMENTO PDF"
        titulo = widgets.HTML(value=f"<b>{text}</b>")'''

        '''pdf = widgets.Text(
            value='',
            placeholder='Documento',
            description='Documento:',
            disabled=False
        )'''

        box7.append(titulo_documento)
        box7.append(pdf)

        box7.append(aviso)

        '''text = "CARPETA DESCARGA"
        titulo = widgets.HTML(value=f"<b>{text}</b>")
        p = widgets.Label(value="Ejemplo:C:\\Users\\user\\Documents\\Archivos")'''

        box7.append(titulo_carpeta)
        box7.append(aviso_carpeta)

        '''carpeta = widgets.Text(
            value='',
            placeholder='Carpeta',
            description='Carpeta:',
            disabled=False
        )'''

        box7.append(carpeta)

        '''text = "CARPETA DESCARGA GRÁFICAS"
        titulo = widgets.HTML(value=f"<b>{text}</b>")
        p = widgets.Label(value="Ejemplo:C:\\Users\\user\\Documents\\Archivos")'''

        '''box7.append(titulo_carpeta_grafica)
        box7.append(aviso_carpeta_grafica)'''

        '''carpeta2 = widgets.Text(
            value='',
            placeholder='Carpeta',
            description='Carpeta:',
            disabled=False
        )'''

        # box7.append(carpeta2)

        boton2 = Boton_grafica_estudiante_pdf(diccionario_estudiantes, seleccion_temas, seleccion_fechas, fechas, opciones,
                                              estudiantes, opciones2, color, pdf, carpeta, opcion_grafica)
        box7.append(boton2.button)

        b7.children = [i for i in box7]

        # -------------------------------------------------------------------------------

        b8 = widgets.VBox()
        box8 = [titulo_identificador]

        identificador = widgets.Text(
            value='',
            placeholder='Id',
            description='Id:',
            disabled=False
        )

        box8.append(widgets.Label(value="Indique el identificador del recurso de Moodle: "))

        box8.append(identificador)

        box8.append(widgets.Label(value="Indique una dirección IP: "))

        IP = widgets.Text(
            value='',
            placeholder='IP',
            description='IP:',
            disabled=False
        )
        box8.append(IP)

        box8.append(titulo_fechas)
        box8.append(seleccion_fechas)

        estd = ['Grupo', 'Todos']

        for id in diccionario_estudiantes.keys():
            estd.append(id)

        estds = widgets.SelectMultiple(
            options=estd,
            value=['Grupo'],
            # rows=10,
            description='Estudiantes',
            disabled=False
        )

        box8.append(titulo_estudiantes)
        box8.append(estds)

        box8.append(diseno_grafica)
        box8.append(opcion_grafica)

        box8.append(titulo_color_grafica)
        box8.append(color_grafica)
        box8.append(color)

        boton = Boton_grafica_registros(identificador, seleccion_fechas, fechas,
                                        estds, color, IP, opcion_grafica, diccionario_estudiantes)
        box8.append(boton.button)

        box8.append(titulo_documento)
        box8.append(pdf)

        box8.append(aviso)

        box8.append(titulo_carpeta)
        box8.append(aviso_carpeta)

        box8.append(carpeta)

        '''box8.append(titulo_carpeta_grafica)
        box8.append(aviso_carpeta_grafica)
    
        box8.append(carpeta2)'''

        boton2 = Boton_grafica_registros_pdf(identificador, seleccion_fechas, fechas, estudiantes, color, pdf, carpeta,
                                             IP, opcion_grafica, diccionario_estudiantes)

        box8.append(boton2.button)

        b8.children = [i for i in box8]

        # -------------------------------------------------------------------------------

        b9 = widgets.VBox()
        box9 = [titulo_fechas, seleccion_fechas]

        titulo_comparacion = widgets.HTML(value=f"<b>SELECCIÓN DE DOCUMENTOS:</b>")

        dcmts = []

        for d in documentos:
            dcmts.append(d[0])

        if len(dcmts) == 0:
            dcmts.append(" ")
            valor = " "
        else:
            valor = dcmts[0]

        seleccion_comparacion = widgets.SelectMultiple(
            options=dcmts,
            value=[valor],
            # rows=10,
            description='Documentos',
            disabled=False
        )

        box9.append(titulo_comparacion)
        box9.append(seleccion_comparacion)

        opciones2 = widgets.RadioButtons(
            options=['Nota Media', 'Participacion', 'Aprobados', '% Aprobados'],
            #    value='pineapple', # Defaults to 'pineapple'
            layout={'width': 'max-content'},  # If the items' names are long
            disabled=False
        )

        box9.append(titulo_grafica)
        box9.append(opciones2)

        box9.append(diseno_grafica)
        box9.append(opcion_grafica)

        boton = Boton_graficas_comparacion(seleccion_fechas, fechas, opciones2, opcion_grafica,
                                           seleccion_comparacion, documentos)
        box9.append(boton.button)

        box9.append(titulo_documento)
        box9.append(pdf)

        box9.append(aviso)

        box9.append(titulo_carpeta)
        box9.append(aviso_carpeta)

        box9.append(carpeta)

        '''box9.append(titulo_carpeta_grafica)
        box9.append(aviso_carpeta_grafica)
    
        box9.append(carpeta2)'''

        boton2 = Boton_graficas_comparacion_PDF(seleccion_fechas, fechas, opciones2, opcion_grafica,
                                                seleccion_comparacion, documentos, pdf, carpeta)
        box9.append(boton2.button)

        b9.children = [i for i in box9]

        # -------------------------------------------------------------------------------

        box_layout = widgets.Layout(display='flex',
                                    flex_flow='column',
                                    width='50%', )

        accordion = widgets.Accordion(children=[b1, b2, b3, b4, b5, b6, b7, b8, b9], titles='', layout=box_layout)
        accordion.set_title(0, 'INFORMACIÓN DEL GRUPO')
        accordion.set_title(1, 'RANKING DE TEMAS')
        accordion.set_title(2, 'GRÁFICAS DE GRUPO')
        accordion.set_title(3, 'INFORMACIÓN DEL ESTUDIANTE')
        accordion.set_title(4, 'RANKING PARA ESTUDIANTES')
        accordion.set_title(5, 'RANKING DE ESTUDIANTES')
        accordion.set_title(6, 'GRÁFICAS DE ESTUDIANTE')
        accordion.set_title(7, 'REGISTROS DE ACCESO')
        accordion.set_title(8, 'COMPARAR FICHEROS')

        display(accordion)
