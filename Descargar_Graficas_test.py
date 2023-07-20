import csv
import os

import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import widgets
import random
from reportlab.lib.pagesizes import A4
from Analizar_Datos_test import *
import shutil

from Lectura_Ficheros import leer

'''
def Grafica_test_fecha_pdf(diccionario, temas, s_fechas, fechas, opcion, color, documento, diseno): La función genera un 
documento PDF con las gráficas que para una serie de interalos de tiempo compara un determinado valor (nota media, test 
finalizados, test aprobados o porcentaje de aprobados) para varios temas.

  - Argumentos:
      - diccionario: Diccionario que contiene los tests realizados por los estudiantes para cada uno de los temas 
      (la clave son los temas de los test y sus valores un array con los test realizados por los estudiantes).
      - temas: Temas seleccionados para los que se quiere obtener los resultados.
      - s_fechas: Intervalos de fechas seleccionados para los cuales se quiere obtener los resultados. 
      - fechas: Array con los intervalos de fechas.
      - opcion: Opción para el valor que se desea mostrar en las gráficas.
      - color: Color deseado para las barras de la gráfica.
      - documento: Objeto que representa el documento a descargar.
      - nombre_documento: Nombre del documento a descargar.
      - carpeta: Carpeta destino para el documento a descargar
      - carpeta2: Carpeta destino para la gráfica a descargar
      - diseno: opción para el diseño de la gráfica
'''


def Grafica_test_fecha_pdf(diccionario, temas, s_fechas, fechas, opcion, color, documento, nombre_documento, carpeta,
                           diseno):
    etiqueta = ''
    etiqueta2 = ''
    nombre_fichero = ''

    w, h = A4
    cursor = 75
    documento.setFont("Times-Roman", 16)
    documento.drawString(50, h - int(cursor), "GRÁFICAS TEMAS X FECHA")
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

    if temas[0] == "Todos":
        temas = []
        for t in diccionario.keys():
            temas.append(t)

    for f in fechas:
        x = []
        y = []
        y2 = []

        documento.drawString(50, h - int(cursor),
                             "-----------------------------------------------------------------------------")
        cursor += 15
        documento.drawString(50, h - int(cursor), str(f[0]).split(' ')[0] + " - " + str(f[1]).split(' ')[0])
        cursor += 15

        pruebas_temas = {}

        for t in temas:
            pruebas = []
            for p in diccionario[t]:
                if f[0] <= p.fecha <= f[1]:
                    pruebas.append(p)

            pruebas_temas[t] = pruebas

        if opcion == "Nota Media":

            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 15
            documento.drawString(50, h - int(cursor), "OPCIÓN: NOTA MEDIA")
            cursor += 15
            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 20

            etiqueta = 'Nota Media'
            nombre_fichero = "Nota_Media_" + str(f[0]).split(' ')[0].replace('-', '_') + "_" + str(f[1]).split(' ')[
                0].replace('-', '_') + ".jpg"

            for t in pruebas_temas:
                if h - cursor < 120:
                    documento.showPage()
                    documento.setFont("Times-Roman", 12)
                    cursor = 75

                x.append(t)

                media = round(nota_media(pruebas_temas[t]), 2)
                y.append(media)
                documento.drawString(50, h - int(cursor), "TEMA: " + t)
                cursor += 15
                documento.drawString(50, h - int(cursor), "Nota media: " + str(media))
                cursor += 20

        elif opcion == "Participacion":

            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 15
            documento.drawString(50, h - int(cursor), "OPCIÓN: NUMERO DE VECES QUE SE HA FINALIZADO EL TEST")
            cursor += 15
            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 20

            etiqueta = 'Veces Finalizado'
            nombre_fichero = "Veces_Finalizado" + str(f[0]).split(' ')[0].replace('-', '_') + "_" + \
                             str(f[1]).split(' ')[
                                 0].replace('-', '_') + ".jpg"

            for t in pruebas_temas:
                x.append(t)
                finalizado = participacion(pruebas_temas[t])
                y.append(finalizado)
                documento.drawString(50, h - int(cursor), "TEMA: " + t)
                cursor += 15
                documento.drawString(50, h - int(cursor),
                                     "Numero de veces que se ha finalizado el test es: " + str(finalizado))
                cursor += 20

        elif opcion == "Aprobados":

            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 15
            documento.drawString(50, h - int(cursor), "OPCIÓN: NUMERO DE VECES QUE SE HA APROBADO EL TEST")
            cursor += 15
            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 20

            etiqueta = 'Veces Aprobado'
            nombre_fichero = "Veces_Aprobado" + str(f[0]).split(' ')[0].replace('-', '_') + "_" + str(f[1]).split(' ')[
                0].replace('-', '_') + ".jpg"

            for t in pruebas_temas:
                x.append(t)
                aprobado, porcentaje = aprobados(pruebas_temas[t])
                y.append(aprobado)

                if h - cursor < 120:
                    documento.showPage()
                    documento.setFont("Times-Roman", 12)
                    cursor = 75

                documento.drawString(50, h - int(cursor), "TEMA: " + t)
                cursor += 15
                documento.drawString(50, h - int(cursor),
                                     "Numero de veces que se ha aprobado el test es: " + str(aprobado))
                cursor += 20

        elif opcion == "% Aprobados":

            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 15
            documento.drawString(50, h - int(cursor), "OPCIÓN: TEST REALIZADOS - TEST APROBADOS")
            cursor += 15
            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 20

            etiqueta = 'Veces Aprobado'
            etiqueta2 = 'Veces Finalizado'
            nombre_fichero = "Porcentaje_Aprobados" + str(f[0]).split(' ')[0].replace('-', '_') + "_" + \
                             str(f[1]).split(' ')[
                                 0].replace('-', '_') + ".jpg"

            for t in pruebas_temas:
                x.append(t)
                finalizado = participacion(pruebas_temas[t])
                aprobado, porcentaje = aprobados(pruebas_temas[t])

                y.append(finalizado)
                y2.append(aprobado)

                if h - cursor < 140:
                    documento.showPage()
                    documento.setFont("Times-Roman", 12)
                    cursor = 75

                documento.drawString(50, h - int(cursor), "TEMA: " + t)
                cursor += 15
                documento.drawString(50, h - int(cursor),
                                     "Numero de veces que se ha finalizado el test: " + str(finalizado))
                cursor += 15
                documento.drawString(50, h - int(cursor),
                                     "Numero de veces que se ha aprobado el test: " + str(aprobado))
                cursor += 15
                documento.drawString(50, h - int(cursor), "Porcentaje de aprobados: " + str(porcentaje) + "%")
                cursor += 20

        if h - cursor < 300:
            documento.showPage()
            documento.setFont("Times-Roman", 12)
            cursor = 75

        fig, ax = plt.subplots()
        n = len(x)
        width = 0.25

        if diseno == 1:
            if opcion == "% Aprobados":
                ax.bar(np.arange(n), y2, width=width, label=etiqueta, color="#00ba38")
                ax.bar(np.arange(n) - width, y, width=width, label=etiqueta2, color=color)
            else:
                ax.bar(np.arange(n), y, width=width, label=etiqueta, color=color)
        else:
            if opcion == "% Aprobados":
                ax.plot(np.arange(n), y2, label=etiqueta, color="#00ba38", linestyle='solid', marker='o')
                ax.plot(np.arange(n), y, label=etiqueta2, color=color, linestyle='solid', marker='o')
            else:
                ax.plot(np.arange(n), y, label=etiqueta, color=color, linestyle='solid', marker='o')

        plt.xticks(np.arange(n), x)
        plt.legend(loc='best')

        plt.savefig(nombre_fichero, bbox_inches='tight')

        cursor += 250
        documento.drawImage(nombre_fichero, 50, h - int(cursor))

        '''if carpeta2 != "":
            shutil.move(nombre_fichero, carpeta2)'''
        os.remove(nombre_fichero)

        documento.showPage()
        documento.setFont("Times-Roman", 12)
        cursor = 75

    documento.save()
    if carpeta != "":
        shutil.move(nombre_documento, carpeta)


'''
Grafica_fecha_test_pdf(diccionario, temas, s_fechas, fechas, opcion, color, documento, diseno): La función genera un documento 
PDF con las gráficas comparando para una serie de temas determinados valores (nota media, test finalizados, 
test aprobados o porcentaje de aprobados) para varios intervalos de tiempo.

  - Argumentos:
      - diccionario: Diccionario que contiene los tests realizados por los estudiantes para cada uno de los temas 
      (la clave son los temas de los test y sus valores un array con los test realizados por los estudiantes).
      - temas: Temas seleccionados para los que se quiere obtener los resultados.
      - s_fechas: Intervalos de fechas seleccionados para los cuales se quiere obtener los resultados. 
      - fechas: Array con los intervalos de fechas.
      - opcion: Opción para el valor que se desea mostrar en las gráficas.
      - color: Color deseado para las barras de la gráfica.
      - documento: Objeto que representa el documento a descargar.
      - nombre_documento: Nombre del documento a descargar.
      - carpeta: Carpeta destino para el documento a descargar
      - carpeta2: Carpeta destino para la gráfica a descargar
      - diseno: opción para el diseño de la gráfica
'''


def Grafica_fecha_test_pdf(diccionario, temas, s_fechas, fechas, opcion, color, documento, nombre_documento, carpeta,
                           diseno):
    etiqueta = ''
    etiqueta2 = ''
    nombre_fichero = ''

    plt.rcParams.update({'figure.figsize': (10, 6), 'figure.dpi': 50})

    w, h = A4
    cursor = 75
    documento.setFont("Times-Roman", 16)
    documento.drawString(50, h - int(cursor), "GRÁFICAS FECHAS X TEMA")
    cursor += 30
    documento.setFont("Times-Roman", 12)

    if s_fechas[0] != "Todos":
        fechas = []
        for f in s_fechas:
            fs = []
            fi = f.split('/')[0].lstrip().rstrip()
            ff = f.split('/')[1].lstrip().rstrip()

            fs.append(datetime.strptime(fi, '%Y-%m-%d'))
            fs.append(datetime.strptime(ff, '%Y-%m-%d'))
            fechas.append(fs)

    if temas[0] == "Todos":
        temas = []
        for t in diccionario.keys():
            temas.append(t)

    for t in temas:

        x = []
        y = []
        y2 = []

        documento.drawString(50, h - int(cursor),
                             "-----------------------------------------------------------------------------")
        cursor += 15
        documento.drawString(50, h - int(cursor), "TEMA " + str(t))
        cursor += 15

        if opcion == "Nota Media":

            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 15
            documento.drawString(50, h - int(cursor), "OPCIÓN: NOTA MEDIA")
            cursor += 15
            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 20

            etiqueta = "Nota Media"
            nombre_fichero = "Nota_Media_" + t + ".jpg"

        elif opcion == "Participacion":
            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 15
            documento.drawString(50, h - int(cursor), "OPCIÓN: NUMERO DE VECES QUE SE HA FINALIZADO EL TEST")
            cursor += 15
            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 20

            etiqueta = "Veces Finalizado"
            nombre_fichero = "Veces_Finalizado_" + t + ".jpg"

        elif opcion == "Aprobados":

            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 15
            documento.drawString(50, h - int(cursor), "OPCIÓN: NUMERO DE VECES QUE SE HA APROBADO EL TEST")
            cursor += 15
            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 20

            etiqueta = "Veces Aprobado"
            nombre_fichero = "Veces_Aprobado_" + t + ".jpg"

        elif opcion == "% Aprobados":

            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 15
            documento.drawString(50, h - int(cursor), "OPCIÓN: TEST REALIZADOS - TEST APROBADOS")
            cursor += 15
            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 20

            etiqueta = "Veces Finalizado"
            etiqueta2 = "Veces Aprobado"
            nombre_fichero = "Porcentaje_Aprobados" + t + ".jpg"

        for f in fechas:
            x.append(str(f[0]).split(' ')[0] + " / " + str(f[1]).split(' ')[0])

            documento.drawString(50, h - int(cursor),
                                 "FECHA: " + str(f[0]).split(' ')[0] + " / " + str(f[1]).split(' ')[0])
            cursor += 20

            pruebas = []
            for p in diccionario[t]:
                if f[0] <= p.fecha <= f[1]:
                    pruebas.append(p)

            if opcion == "Nota Media":

                media = round(nota_media(pruebas), 2)
                y.append(media)

                if h - cursor < 100:
                    documento.showPage()
                    documento.setFont("Times-Roman", 12)
                    cursor = 75

                documento.drawString(50, h - int(cursor), "Nota media: " + str(media))
                cursor += 20

            elif opcion == "Participacion":

                finalizado = participacion(pruebas)
                y.append(finalizado)

                if h - cursor < 100:
                    documento.showPage()
                    documento.setFont("Times-Roman", 12)
                    cursor = 75

                documento.drawString(50, h - int(cursor),
                                     "Numero de veces que se ha finalizado el test: " + str(finalizado))
                cursor += 20

            elif opcion == "Aprobados":

                aprobado, porcentaje = aprobados(pruebas)
                y.append(aprobado)

                if h - cursor < 100:
                    documento.showPage()
                    documento.setFont("Times-Roman", 12)
                    cursor = 75

                documento.drawString(50, h - int(cursor),
                                     "Numero de veces que se ha aprobado el test: " + str(aprobado))
                cursor += 20

            elif opcion == "% Aprobados":

                finalizado = participacion(pruebas)
                aprobado, porcentaje = aprobados(pruebas)
                y.append(finalizado)
                y2.append(aprobado)

                if h - cursor < 140:
                    documento.showPage()
                    documento.setFont("Times-Roman", 12)
                    cursor = 75

                documento.drawString(50, h - int(cursor),
                                     "Numero de veces que se ha finalizado el test: " + str(finalizado))
                cursor += 15
                documento.drawString(50, h - int(cursor),
                                     "Numero de veces que se ha aprobado el test: " + str(aprobado))
                cursor += 15
                documento.drawString(50, h - int(cursor), "Porcentaje de aprobados: " + str(porcentaje))
                cursor += 20

        fig, ax = plt.subplots()
        n = len(x)
        width = 0.25

        if diseno == 1:
            if opcion == "% Aprobados":
                ax.bar(np.arange(n), y2, width=width, label=etiqueta, color="#00ba38")
                ax.bar(np.arange(n) - width, y, width=width, label=etiqueta2, color=color)
            else:
                ax.bar(np.arange(n), y, width=width, label=etiqueta, color=color)
        else:
            if opcion == "% Aprobados":
                ax.plot(np.arange(n), y2, label=etiqueta, color="#00ba38", linestyle='solid', marker='o')
                ax.plot(np.arange(n), y, label=etiqueta2, color=color, linestyle='solid', marker='o')
            else:
                ax.plot(np.arange(n), y, label=etiqueta, color=color, linestyle='solid', marker='o')

        plt.xticks(np.arange(n), x)
        plt.legend(loc='best')

        plt.savefig(nombre_fichero, bbox_inches='tight')

        if h - cursor < 300:
            documento.showPage()
            documento.setFont("Times-Roman", 12)
            cursor = 75

        cursor += 250
        documento.drawImage(nombre_fichero, 50, h - int(cursor))

        # shutil.move(nombre_fichero, carpeta2)
        os.remove(nombre_fichero)

        documento.showPage()
        documento.setFont("Times-Roman", 12)
        cursor = 75

    documento.save()
    shutil.move(nombre_documento, carpeta)

    '''
  def Grafica_estudiante_pdf(identificador, estudiantes, temas, s_fechas, fechas, opcion, opcion2, color, documento,
  diseno): 
  La función genera un documento PDF que recoge para cada uno de los estudiantes una gráfica comparando un determinado 
  valor (nota media, test finalizados, test aprobados o porcentaje de aprobados) para varios temas (el valor se puede 
  comparar para un mismo tema para varios interalos de tiempo o para varios temas en un intervalo de tiempo)
  - Argumentos:
      - identificador: Estudiantes seleccionados para los cuales se quiere obtener la información.
      - estudiantes. Diccionario con los estudiantes y sus test realizados. La clave del diccionario es el identificador 
      del estudiante y para cada clave su valor es un diccionario con los test. Este segundo diccionario tiene como 
      clave el tema al que pertenecen los test y para cada clave su valor es un array que contiene los test realizados 
      por los estudiantes.
      - temas: Temas seleccionados para los que se quiere obtener los resultados.
      - s_fechas: Intervalos de fechas seleccionados para los cuales se quiere obtener los resultados. 
      - fechas: Array con los intervalos de fechas.
      - opcion: Opción para el tipo de análisis que queremos realizar sobre los test realizados por el estudiante 
      (Evolución para cada uno de los temas para una serie de intervalos de fechas o comparativa de una serie de temas 
      para una serie de intervalos de fechas)
      - opcion2: Opción para el valor que se desea mostrar en las gráficas (nota media, test finalizados, test 
      aprobados o porcentaje de aprobados)
      - color: Color para las barras de las gráficas
      - documento: Objeto que representa el documento a descargar.
      - nombre_documento: Nombre del documento a descargar.
      - carpeta: Carpeta destino para el documento a descargar
      - carpeta2: Carpeta destino para la gráfica a descargar
      - diseno: opción para el diseño de la gráfica
  '''


def Grafica_estudiante_pdf(identificador, estudiantes, temas, s_fechas, fechas, opcion, opcion2, color, documento,
                           nombre_documento, carpeta, diseno):
    etiqueta = ''
    etiqueta2 = ''
    nombre_fichero = ''

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

    if identificador[0] == "Todos":
        identificador = []
        for e in estudiantes.keys():
            identificador.append(e)

    documento.drawString(50, h - int(cursor),
                         "-----------------------------------------------------------------------------")
    cursor += 15
    if opcion2 == "Nota Media":

        documento.drawString(50, h - int(cursor), "OPCIÓN: NOTA MEDIA")
        cursor += 20

    elif opcion2 == "Participacion":

        documento.drawString(50, h - int(cursor),
                             "OPCIÓN: NUMERO DE VECES QUE SE HA FINALIZADO EL TEST")
        cursor += 20

    elif opcion2 == "Aprobados":

        documento.drawString(50, h - int(cursor), "OPCIÓN: NUMERO DE VECES QUE SE HA APROBADO EL TEST")
        cursor += 20

    elif opcion2 == "% Aprobados":

        documento.drawString(50, h - int(cursor), "OPCIÓN: TEST REALIZADOS - TEST APROBADOS")
        cursor += 20

    documento.drawString(50, h - int(cursor),
                         "-----------------------------------------------------------------------------")
    cursor += 20

    for e in identificador:

        documento.drawString(50, h - int(cursor),
                             "-----------------------------------------------------------------------------")
        cursor += 15
        documento.drawString(50, h - int(cursor), "ESTUDIANTE " + e)
        cursor += 15
        documento.drawString(50, h - int(cursor),
                             "-----------------------------------------------------------------------------")
        cursor += 20

        pruebas = estudiantes[e].pruebas

        if temas[0] == "Todos":
            temas = []
            for t in pruebas:
                temas.append(t)

        if opcion == "Fecha x Temas":
            for t in temas:

                x = []
                y = []
                y2 = []

                if t in pruebas:

                    documento.drawString(50, h - int(cursor), "TEMA " + str(t))
                    cursor += 25

                    if opcion2 == "Nota Media":

                        etiqueta = "Nota Media"
                        nombre_fichero = "Nota_Media_" + t + "_" + e + ".jpg"

                    elif opcion2 == "Participacion":

                        etiqueta = "Veces Aprobado"
                        nombre_fichero = "Veces_Aprobado_" + t + "_" + e + ".jpg"

                    elif opcion2 == "Aprobados":

                        etiqueta = "Veces Finalizado"
                        nombre_fichero = "Veces_Finalizado_" + t + "_" + e + ".jpg"

                    elif opcion2 == "% Aprobados":

                        etiqueta = "Veces Finalizado"
                        etiqueta2 = "Veces Aprobado"
                        nombre_fichero = "Porcentaje_Aprobados" + t + "_" + e + ".jpg"

                    for f in fechas:

                        if h - cursor < 150:
                            documento.showPage()
                            documento.setFont("Times-Roman", 12)
                            cursor = 75

                        documento.drawString(50, h - int(cursor),
                                             "-----------------------------------------------------------------------------")
                        cursor += 15
                        documento.drawString(50, h - int(cursor),
                                             str(f[0]).split(' ')[0] + " - " + str(f[1]).split(' ')[0])
                        cursor += 15
                        documento.drawString(50, h - int(cursor),
                                             "-----------------------------------------------------------------------------")
                        cursor += 20

                        x.append(str(f[0]).split(' ')[0] + " - " + str(f[1]).split(' ')[0])

                        prs = []

                        for p in pruebas[t]:
                            if f[0] <= p.fecha <= f[1]:
                                prs.append(p)

                        finalizado = participacion(prs)
                        aprobado, porcentaje = aprobados(prs)

                        if opcion2 == "Nota Media":

                            documento.drawString(50, h - int(cursor), "Nota media: " + str(round(nota_media(prs), 2)))
                            cursor += 20

                            y.append(round(nota_media(prs), 2))

                        elif opcion2 == "Participacion":

                            documento.drawString(50, h - int(cursor),
                                                 "Numero de veces que se ha finalizado el test: " + str(finalizado))
                            cursor += 20

                            y.append(finalizado)

                        elif opcion2 == "Aprobados":

                            documento.drawString(50, h - int(cursor),
                                                 "Numero de veces que se ha aprobado el test: " + str(aprobado))
                            cursor += 20

                            y.append(aprobado)

                        elif opcion2 == "% Aprobados":

                            y.append(finalizado)
                            y2.append(aprobado)

                            documento.drawString(50, h - int(cursor),
                                                 "Numero de veces que se ha finalizado el test: " + str(finalizado))
                            cursor += 15
                            documento.drawString(50, h - int(cursor),
                                                 "Numero de veces que se ha aprobado el test: " + str(aprobado))
                            cursor += 15
                            documento.drawString(50, h - int(cursor), "Porcentaje de aprobados: " + str(porcentaje))
                            cursor += 20

                    fig, ax = plt.subplots()
                    n = len(x)
                    width = 0.25

                    if diseno == 1:
                        if opcion == "% Aprobados":
                            ax.bar(np.arange(n), y2, width=width, label=etiqueta, color="#00ba38")
                            ax.bar(np.arange(n) - width, y, width=width, label=etiqueta2, color=color)
                        else:
                            ax.bar(np.arange(n), y, width=width, label=etiqueta, color=color)
                    else:
                        if opcion == "":
                            ax.plot(np.arange(n), y2, label=etiqueta, color="#00ba38", linestyle='solid', marker='o')
                            ax.plot(np.arange(n), y, label=etiqueta2, color=color, linestyle='solid', marker='o')
                        else:
                            ax.plot(np.arange(n), y, label=etiqueta, color=color, linestyle='solid', marker='o')

                    plt.xticks(np.arange(n), x)
                    plt.legend(loc='best')

                    if h - cursor < 330:
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
                    cursor = 75

        elif opcion == "Temas x Fecha":

            for f in fechas:

                x = []
                y = []
                y2 = []

                documento.drawString(50, h - int(cursor), str(f[0]).split(' ')[0] + " - " + str(f[1]).split(' ')[0])
                cursor += 20

                if opcion2 == "Nota Media":
                    documento.drawString(50, h - int(cursor), "OPCIÓN: NOTA MEDIA")
                    cursor += 20

                    etiqueta = "Nota Media"
                    nombre_fichero = "Nota_Media_" + str(f[0]).split(' ')[0].replace('-', '_') + "_" + \
                                     str(f[1]).split(' ')[
                                         0].replace('-', '_') + "_" + e + ".jpg"

                elif opcion2 == "Participacion":

                    documento.drawString(50, h - int(cursor), "OPCIÓN: NUMERO DE VECES QUE SE HA FINALIZADO EL TEST")
                    cursor += 20

                    etiqueta = "Veces Aprobado"
                    nombre_fichero = "Veces_Aprobado_" + str(f[0]).split(' ')[0].replace('-', '_') + "_" + \
                                     str(f[1]).split(' ')[
                                         0].replace('-', '_') + "_" + e + ".jpg"

                elif opcion2 == "Aprobados":

                    documento.drawString(50, h - int(cursor), "OPCIÓN: NUMERO DE VECES QUE SE HA APROBADO EL TEST")
                    cursor += 20

                    etiqueta = "Veces Finalizado"
                    nombre_fichero = "Veces_Finalizado_" + str(f[0]).split(' ')[0].replace('-', '_') + "_" + \
                                     str(f[1]).split(' ')[
                                         0].replace('-', '_') + "_" + e + ".jpg"

                elif opcion2 == "% Aprobados":

                    documento.drawString(50, h - int(cursor), "OPCIÓN: TEST REALIZADOS - TEST APROBADOS")
                    cursor += 20

                    etiqueta = "Veces Finalizado"
                    etiqueta2 = "Veces Aprobado"
                    nombre_fichero = "Porcentaje_Aprobados" + str(f[0]).split(' ')[0].replace('-', '_') + "_" + \
                                     str(f[1]).split(' ')[
                                         0].replace('-', '_') + "_" + e + ".jpg"

                for t in temas:

                    if t in pruebas:

                        x.append(t)

                        if h - cursor < 150:
                            documento.showPage()
                            documento.setFont("Times-Roman", 12)
                            cursor = 75

                        documento.drawString(50, h - int(cursor),
                                             "-----------------------------------------------------------------------------")
                        cursor += 15
                        documento.drawString(50, h - int(cursor), "Tema " + str(t))
                        cursor += 15
                        documento.drawString(50, h - int(cursor),
                                             "-----------------------------------------------------------------------------")
                        cursor += 20

                        prs = []

                        for p in pruebas[t]:
                            if f[0] <= p.fecha <= f[1]:
                                prs.append(p)

                        finalizado = participacion(prs)
                        aprobado, porcentaje = aprobados(prs)

                        if opcion2 == "Nota Media":

                            documento.drawString(50, h - int(cursor), "Nota media: " + str(round(nota_media(prs), 2)))
                            cursor += 15

                            y.append(round(nota_media(prs), 2))

                        elif opcion2 == "Participacion":

                            documento.drawString(50, h - int(cursor),
                                                 "Numero de veces que se ha finalizado el test: " + str(finalizado))
                            cursor += 15

                            y.append(finalizado)

                        elif opcion2 == "Aprobados":

                            documento.drawString(50, h - int(cursor),
                                                 "Numero de veces que se ha aprobado el test: " + str(aprobado))
                            cursor += 15

                            y.append(aprobado)

                        elif opcion2 == "% Aprobados":

                            y.append(finalizado)
                            y2.append(aprobado)

                            documento.drawString(50, h - int(cursor),
                                                 "Numero de veces que se ha finalizado el test: " + str(finalizado))
                            cursor += 15
                            documento.drawString(50, h - int(cursor),
                                                 "Numero de veces que se ha aprobado el test: " + str(aprobado))
                            cursor += 15
                            documento.drawString(50, h - int(cursor),
                                                 "Porcentaje de aprobados: " + str(porcentaje)) + '%'
                            cursor += 15

                fig, ax = plt.subplots()
                n = len(x)
                width = 0.25

                if diseno == 1:
                    if opcion == "% Aprobados":
                        ax.bar(np.arange(n), y2, width=width, label=etiqueta, color="#00ba38", alpha=0.25)
                        ax.bar(np.arange(n) - width, y, width=width, label=etiqueta2, color=color, alpha=0.25)
                    else:
                        ax.bar(np.arange(n), y, width=width, label=etiqueta, color=color, alpha=0.25)
                else:

                    if opcion == "":
                        ax.plot(np.arange(n), y2, label=etiqueta, color="#00ba38", linestyle='solid', marker='o')
                        ax.plot(np.arange(n), y, label=etiqueta2, color=color, linestyle='solid', marker='o')
                    else:
                        ax.plot(np.arange(n), y, label=etiqueta, color=color, linestyle='solid', marker='o')

                plt.xticks(np.arange(n), x)
                plt.legend(loc='best')

                if h - cursor < 300:
                    documento.showPage()
                    documento.setFont("Times-Roman", 12)
                    cursor = 75

                plt.savefig(nombre_fichero, bbox_inches='tight')

                cursor += 220
                documento.drawImage(nombre_fichero, 50, h - int(cursor))
                # shutil.move(nombre_fichero, carpeta2)
                os.remove(nombre_fichero)

                documento.showPage()
                documento.setFont("Times-Roman", 12)
                cursor = 75

    documento.save()
    shutil.move(nombre_documento, carpeta)


'''
def Grafica_test_fecha_comparacion_PDF(diccionario, temas, s_fechas, fechas, opcion, color, diseno, ficheros): 
La función muestra para una serie de intervalos de tiempo una gráfica comparando un determinado valor 
(nota media, test finalizados, test aprobados o porcentaje de aprobados) para varios temas, para varios ficheros.

  - Argumentos:
      - s_fechas: Intervalos de fechas seleccionados para los cuales se quiere obtener los resultados. 
      - fechas: Array con los intervalos de fechas.
      - opcion: Opción para el valor que se desea mostrar en las gráficas.
      - diseno: opción para el diseño de la gráfica
      - ficheros: ficheros que se desea comparar
      - documentos: Array con los documentos incorporados a la herramienta.
      - documento: Objeto que representa el documento a descargar.
      - nombre_documento: Nombre del documento.
      - carpeta: Carpeta destino para el documento a descargar
'''


def Grafica_test_comparacion_PDF(s_fechas, fechas, opcion, diseno, ficheros, documentos,
                                 documento, nombre_documento, carpeta):
    dic_ficheros = {}

    etiqueta = ""
    etiqueta2 = ""
    nombre_fichero = ""

    w, h = A4
    cursor = 75
    documento.setFont("Times-Roman", 16)
    documento.drawString(50, h - int(cursor), "GRÁFICAS PARA LA EVOLUCIÓN DE LOS TEMAS")
    cursor += 30
    documento.setFont("Times-Roman", 12)

    plt.rcParams.update({'figure.figsize': (10, 6), 'figure.dpi': 50})
    fig, ax = plt.subplots()

    if s_fechas[0] != "Todos":
        fechas = []
        for f in s_fechas:
            fs = []
            fi = f.split('/')[0].lstrip().rstrip()
            ff = f.split('/')[1].lstrip().rstrip()

            fs.append(datetime.strptime(fi, '%Y-%m-%d'))
            fs.append(datetime.strptime(ff, '%Y-%m-%d'))
            fechas.append(fs)

    for fch in ficheros:
        ruta = ""
        tema = ""
        for doc in documentos:
            if fch == doc[0]:
                ruta = doc[2]
                tema = doc[1]
        try:
            with open(ruta, "r") as archv:
                tests = []

                lector = csv.reader(archv, delimiter=",")
                next(lector, None)
                for fila in lector:
                    tests.append(leer(fila, tema))

                dic_ficheros[fch] = tests
        except FileNotFoundError:
            text = 'No se ha encontrado el fichero ' + fch + ' en la ruta indicada.'
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

    x = []
    for f in fechas:
        x.append(str(f[0]).split(' ')[0] + " - " + str(f[1]).split(' ')[0])

    valores_grafica = {}

    if opcion == "Nota Media":

        etiqueta = "Nota Media "

        documento.drawString(50, h - int(cursor),
                             "-----------------------------------------------------------------------------")
        cursor += 15
        documento.drawString(50, h - int(cursor), "NOTA MEDIA")
        cursor += 15

    elif opcion == "Participacion":

        etiqueta = "Veces Finalizado "

        documento.drawString(50, h - int(cursor),
                             "-----------------------------------------------------------------------------")
        cursor += 15
        documento.drawString(50, h - int(cursor), "NUMERO DE VECES QUE SE HA FINALIZADO EL TEST")
        cursor += 15

    elif opcion == "Aprobados":

        etiqueta = "Veces Aprobado "

        documento.drawString(50, h - int(cursor),
                             "-----------------------------------------------------------------------------")
        cursor += 15
        documento.drawString(50, h - int(cursor), "NUMERO DE VECES QUE SE HA APROBADO EL TEST")
        cursor += 15

    elif opcion == "% Aprobados":

        etiqueta = "Veces Finalizado "
        etiqueta2 = "Veces Aprobado "

        documento.drawString(50, h - int(cursor),
                             "-----------------------------------------------------------------------------")
        cursor += 15
        documento.drawString(50, h - int(cursor), "COMPARACION TEST REALIZADOS - TEST APROBADOS")
        cursor += 20

    for fch in dic_ficheros.keys():

        documento.drawString(50, h - int(cursor),
                             "-----------------------------------------------------------------------------")
        cursor += 15

        documento.drawString(50, h - int(cursor), fch)
        cursor += 15

        y = []
        y2 = []

        for f in fechas:

            if h - cursor < 70:
                documento.showPage()
                documento.setFont("Times-Roman", 12)
                cursor = 75

            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 15

            documento.drawString(50, h - int(cursor), str(f[0]).split(' ')[0] + " - " + str(f[1]).split(' ')[0])
            cursor += 15

            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 20

            pruebas = []

            for t in dic_ficheros[fch]:
                if f[0] <= t.fecha <= f[1]:
                    pruebas.append(t)

            if opcion == "Nota Media":

                nombre_fichero = "Comparativa_Nota_Media" + ".jpg"

                media = round(nota_media(pruebas), 2)
                y.append(media)

                documento.drawString(50, h - int(cursor), "Nota media: " + str(media))
                cursor += 15

            elif opcion == "Participacion":

                nombre_fichero = "Comparativa_Veces_Finaliado" + ".jpg"

                finalizado = participacion(pruebas)
                y.append(finalizado)

                documento.drawString(50, h - int(cursor),
                                     "Numero de veces que se ha finalizado el test: " + str(finalizado))
                cursor += 15

            elif opcion == "Aprobados":

                nombre_fichero = "Comparativa_Veces_Aprobado" + ".jpg"

                aprobado, porcentaje = aprobados(pruebas)
                y.append(aprobado)

                documento.drawString(50, h - int(cursor),
                                     "Numero de veces que se ha aprobado el test: " + str(aprobado))
                cursor += 15

            elif opcion == "% Aprobados":

                nombre_fichero = "Comparativa_Porcentaje_Aprobados" + ".jpg"

                finalizado = participacion(pruebas)
                aprobado, porcentaje = aprobados(pruebas)

                y.append(finalizado)
                y2.append(aprobado)

                documento.drawString(50, h - int(cursor),
                                     "Numero de veces que se ha finalizado el test: " + str(finalizado))
                cursor += 15
                documento.drawString(50, h - int(cursor),
                                     "Numero de veces que se ha aprobado el test: " + str(aprobado))
                cursor += 15
                documento.drawString(50, h - int(cursor),
                                     "Porcentaje de aprobados: " + str(porcentaje) + '%')
                cursor += 15

        valores_grafica[fch] = [y, y2]

        documento.showPage()
        documento.setFont("Times-Roman", 12)
        cursor = 75

    n = len(x)
    width = 0.25

    for fch in dic_ficheros.keys():
        if diseno == 1:
            color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
            if opcion == "% Aprobados":
                ax.bar(np.arange(n), valores_grafica[fch][1], width=width, label=etiqueta + fch, color="#00ba38",
                       alpha=0.25)
                ax.bar(np.arange(n) - width, valores_grafica[fch][0], width=width, label=etiqueta2 + fch, color=color,
                       alpha=0.25)
            else:
                ax.bar(np.arange(n), valores_grafica[fch][0], width=width, label=etiqueta + fch, color=color,
                       alpha=0.25)
        else:
            color = (np.random.random(), np.random.random(), np.random.random())
            if opcion == "% Aprobados":
                ax.plot(np.arange(n), valores_grafica[fch][1], label=etiqueta + fch, color="#00ba38", linestyle='solid',
                        marker='o')
                ax.plot(np.arange(n), valores_grafica[fch][0], label=etiqueta2 + fch, color=color, linestyle='solid',
                        marker='o')
            else:
                ax.plot(np.arange(n), valores_grafica[fch][0], label=etiqueta + fch, color=color, linestyle='solid',
                        marker='o')

    plt.xticks(np.arange(n), x)
    plt.legend(loc='best')

    if h - cursor < 300:
        documento.showPage()
        documento.setFont("Times-Roman", 12)
        cursor = 75

    plt.savefig(nombre_fichero, bbox_inches='tight')

    cursor += 220
    documento.drawImage(nombre_fichero, 50, h - int(cursor))
    os.remove(nombre_fichero)

    documento.save()
    shutil.move(nombre_documento, carpeta)
