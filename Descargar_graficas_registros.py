import os

import matplotlib.pyplot as plt
import numpy as np
from reportlab.lib.pagesizes import A4
from Analizar_Datos_test import *
import shutil

'''
def Grafica_registros_pdf(identificador, diccionario, s_fechas, fechas, estudiantes, color, documento, nombre_documento,
carpeta, carpeta2, IP): La función genera un documento PDF, para el grupo en general o para cada uno de los estdiantes, 
con las gráficas del número de registros de acceso a Moodle a un recurso indicado para los intervalos de tiempo deseados

    - Argumentos:
        - identificador: Identidicador del recurso de Moodle.
        - diccionario: Diccionario con los estudiantes y sus registros de acceso a Moodle. La clave del diccionario 
        es el identificador del estudiante. Para cada clave su valor es un array con objetos de tipo 'Registro' que 
        contienen los accesos a Moodle del estudiante.
        - s_fechas: Intervalos de fechas seleccionados para los cuales se quiere obtener los resultados. 
        - fechas: Array con los intervalos de fechas.
        - estudiantes: Estudiantes seleccionados para los que se desea obtener la información.
        - color: Color para las barras de las gráficas.
        - documento: Objeto que representa el documento a descargar.
        - nombre_documento: Nombre del documento a descargar.
        - carpeta: Carpeta destino para el documento a descargar
        - carpeta2: Carpeta destino para la gráfica a descargar
        - IP: Dirección IP desde la cual se ha accedido a Moodle.
        - diseno: Opción para el diseño de la gráfica
'''


def Grafica_registros_pdf(identificador, diccionario, s_fechas, fechas, estudiantes, color, documento, nombre_documento,
                          carpeta, IP, diseno):
    etiqueta = 'Registros'

    w, h = A4
    cursor = 75
    documento.setFont("Times-Roman", 16)
    documento.drawString(50, h - int(cursor), "GRÁFICAS PARA LA EVOLUCIÓN DE LOS TEMAS")
    cursor += 30
    documento.setFont("Times-Roman", 12)

    plt.rcParams.update({'figure.figsize': (10, 6), 'figure.dpi': 50})

    if s_fechas[0] != "Todos":
        fechas = []
        for f in s_fechas:
            fs = []
            fi = f.split('/')[0].lstrip().rstrip()
            ff = f.split('/')[1].lstrip().rstrip()

            fs.append(datetime.strptime(fi, '%Y-%m-%d'))
            fs.append(datetime.strptime(ff, '%Y-%m-%d'))
            fechas.append(fs)

    if estudiantes[0] == "Todos":
        estudiantes = []
        for e in diccionario.keys():
            estudiantes.append(e)

    if estudiantes[0] == "Grupo":

        nombre_fichero = "registros_grupo.jpg"

        x = []
        y = []

        documento.drawString(50, h - int(cursor),
                             "-----------------------------------------------------------------------------")
        cursor += 15

        documento.drawString(50, h - int(cursor), "REGISTROS DEL GRUPO")
        cursor += 15

        for f in fechas:

            if h - cursor < 50:
                documento.showPage()
                documento.setFont("Times-Roman", 12)
                cursor = 75

            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 15

            documento.drawString(50, h - int(cursor), "FECHA: " + str(f[0]).split(' ')[0] +
                                 " -- " + str(f[1]).split(' ')[0])
            cursor += 15

            x.append(str(f[0]).split(' ')[0] + " / " + str(f[1]).split(' ')[0])

            contador = 0

            for e in diccionario:
                for r in diccionario[e]:
                    if f[0] <= r.fecha <= f[1]:
                        if IP != '':
                            if identificador in r.descripcion and r.IP == IP:
                                contador += 1
                        else:
                            if identificador in r.descripcion:
                                contador += 1

            y.append(contador)

            if IP != '':
                documento.drawString(50, h - int(cursor), "Número de veces que el grupo ha accedido al recurso " +
                                     "con identificador " + identificador + " : " + str(contador) +
                                     "a través de la dirección IP " + IP)

            else:
                documento.drawString(50, h - int(cursor),
                                     "Número de veces que el grupo ha accedido al recurso con identificador " +
                                     identificador + ": " + str(contador))
            cursor += 20

        fig, ax = plt.subplots()
        n = len(x)
        width = 0.25

        if diseno == 1:
            ax.bar(np.arange(n), y, width=width, label=etiqueta, color=color)
        else:
            ax.plot(np.arange(n), y, label=etiqueta, color=color, linestyle='solid', marker='o')

        plt.xticks(np.arange(n), x)
        plt.legend(loc='best')

        if h - cursor < 300:
            documento.showPage()
            documento.setFont("Times-Roman", 12)
            cursor = 75

        plt.savefig(nombre_fichero, bbox_inches='tight')

        cursor += 250
        documento.drawImage(nombre_fichero, 50, h - int(cursor))
        shutil.move(nombre_fichero, carpeta2)

        documento.showPage()
        documento.setFont("Times-Roman", 12)

    else:

        for e in estudiantes:

            nombre_fichero = "registros_estduainte_" + e + ".jpg"

            x = []
            y = []

            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 15

            documento.drawString(50, h - int(cursor), "ESTUDIANTE: " + e)
            cursor += 15

            for f in fechas:
                contador = 0

                documento.drawString(50, h - int(cursor),
                                     "-----------------------------------------------------------------------------")
                cursor += 15

                documento.drawString(50, h - int(cursor), "FECHA: " + str(f[0]).split(' ')[0] +
                                     " -- " + str(f[1]).split(' ')[0])
                cursor += 15

                x.append(str(f[0]).split(' ')[0] + " / " + str(f[1]).split(' ')[0])

                for r in diccionario[e]:
                    if f[0] <= r.fecha <= f[1]:
                        if IP != '':
                            if identificador in r.descripcion and r.IP == IP:
                                contador += 1
                        else:
                            if identificador in r.descripcion:
                                contador += 1

                y.append(contador)

                if IP != '':
                    documento.drawString(50, h - int(cursor), "Número de veces que el estudiante ha accedido al recurso"
                                         + " con identificador " + identificador + " : " + str(contador) +
                                         "a través de la dirección IP " + IP)

                else:
                    documento.drawString(50, h - int(cursor),
                                         "Número de veces que el estudiante  ha accedido al recurso con identificador "
                                         + identificador + ": " + str(contador))

                cursor += 20

            fig, ax = plt.subplots()
            n = len(x)
            width = 0.25

            if diseno == 1:
                ax.bar(np.arange(n), y, width=width, label=etiqueta, color=color)
            else:
                ax.plot(np.arange(n), y, label=etiqueta, color=color, linestyle='solid', marker='o')

            plt.xticks(np.arange(n), x)
            plt.legend(loc='best')

            if h - cursor < 300:
                documento.showPage()
                documento.setFont("Times-Roman", 12)
                cursor = 75

            plt.savefig(nombre_fichero, bbox_inches='tight')

            cursor += 250
            documento.drawImage(nombre_fichero, 50, h - int(cursor))
            # shutil.move(nombre_fichero, carpeta2)
            os.remove(nombre_fichero)

            documento.showPage()
            documento.setFont("Times-Roman", 12)

    documento.save()
    shutil.move(nombre_documento, carpeta)
