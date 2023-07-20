from Clases_Botones import *

'''
def seleccionar_fechas(fechas): Función encargada de generar la opcion de selección de intervalos de fechas para el 
notebook.
    - Argumentos:
        - fechas: Array donde se guardan los intervalos de fechas seleccionados.
'''


def seleccionar_fechas(fechas):
    text = "INTERVALOS DE FECHAS"
    titulo = widgets.HTML(value=f"<b>{text}</b>")
    display(titulo)

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

    boton = Boton_fechas(fecha_inicio, fecha_final, fechas)
    display(boton.button)
