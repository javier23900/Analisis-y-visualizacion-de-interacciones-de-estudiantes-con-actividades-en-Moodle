import csv
import random

import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import widgets

from Analizar_Datos_test import *
from Lectura_Ficheros import leer

'''
def Grafica_test_fecha(diccionario, temas, s_fechas, fechas, opcion, color): La función muestra para una serie de 
intervalos de tiempo una gráfica comparando un determinado valor (nota media, test finalizados, test aprobados o 
porcentaje de aprobados) para varios temas.

  - Argumentos:
      - diccionario: Diccionario que contiene los tests realizados por los estudiantes para cada uno de los temas 
      (la clave son los temas de los test y sus valores un array con los test realizados por los estudiantes).
      - temas: Temas seleccionados para los que se quiere obtener los resultados.
      - s_fechas: Intervalos de fechas seleccionados para los cuales se quiere obtener los resultados. 
      - fechas: Array con los intervalos de fechas.
      - opcion: Opción para el valor que se desea mostrar en las gráficas.
      - color: Color deseado para las barras de la gráfica.
      - diseno: opción para el diseño de la gráfica
'''


def Grafica_test_fecha(diccionario, temas, s_fechas, fechas, opcion, color, diseno):
    etiqueta = ""
    etiqueta2 = ""

    plt.rcParams.update({'figure.figsize': (10, 6), 'figure.dpi': 75})

    if s_fechas[0] != "Todos":
        fechas = []
        for f in s_fechas:
            fs = []
            fi = f.split('/')[0].lstrip().rstrip()
            ff = f.split('/')[1].lstrip().rstrip()

            fs.append(datetime.strptime(fi, '%Y-%m-%d'))
            fs.append(datetime.strptime(ff, '%Y-%m-%d'))
            fechas.append(fs)

    for f in fechas:
        print("-----------------------------------------------------------------------------")
        print(str(f[0]) + " - " + str(f[1]))

        x = []
        y = []
        y2 = []

        pruebas_temas = {}

        if temas[0] == "Todos":
            for t in diccionario.keys():
                pruebas = []

                for p in diccionario[t]:
                    if f[0] <= p.fecha <= f[1]:
                        pruebas.append(p)

                pruebas_temas[t] = pruebas
        else:
            for t in temas:
                pruebas = []

                for p in diccionario[t]:

                    if f[0] <= p.fecha <= f[1]:
                        pruebas.append(p)
                pruebas_temas[t] = pruebas

        if opcion == "Nota Media":
            etiqueta = "Nota Media"
            print("-----------------------------------------------------------------------------")
            print("NOTA MEDIA")

            for t in pruebas_temas:
                print("-----------------------------------------------------------------------------")
                print("Tema: " + str(t))
                print("-----------------------------------------------------------------------------")
                x.append(t)
                media = round(nota_media(pruebas_temas[t]), 2)
                y.append(media)
                print("La nota media del tema es: " + str(media))

        elif opcion == "Participacion":
            etiqueta = "Veces Finalizado"
            print("-----------------------------------------------------------------------------")
            print("NUMERO DE VECES QUE SE HA FINALIZADO EL TEST")

            for t in pruebas_temas:
                print("-----------------------------------------------------------------------------")
                print("Tema: " + str(t))
                print("-----------------------------------------------------------------------------")
                x.append(t)
                finalizado = participacion(pruebas_temas[t])
                y.append(finalizado)
                print("El numero de veces que se ha finalizado el test es: " + str(finalizado))

        elif opcion == "Aprobados":
            etiqueta = "Veces Aprobado"
            print("-----------------------------------------------------------------------------")
            print("NUMERO DE VECES QUE SE HA APROBADO EL TEST")

            for t in pruebas_temas:
                print("-----------------------------------------------------------------------------")
                print("Tema: " + str(t))
                print("-----------------------------------------------------------------------------")
                x.append(t)
                aprobado, porcentaje = aprobados(pruebas_temas[t])
                y.append(aprobado)
                print("El número de veces que se ha aprobado el test es: " + str(aprobado))

        elif opcion == "% Aprobados":
            etiqueta = "Veces Finalizado"
            etiqueta2 = "Veces Aprobado"
            print("-----------------------------------------------------------------------------")
            print("COMPARACION TEST REALIZADOS - TEST APROBADOS")

            for t in pruebas_temas:
                print("-----------------------------------------------------------------------------")
                print("Tema: " + str(t))
                print("-----------------------------------------------------------------------------")
                x.append(t)
                finalizado = participacion(pruebas_temas[t])
                aprobado, porcentaje = aprobados(pruebas_temas[t])

                y.append(finalizado)
                y2.append(aprobado)

                print("El número de veces que se ha finalizado el test es: " + str(finalizado))
                print("El número de veces que se ha aprobado el test es: " + str(aprobado))
                print("El porcentaje de aprobados es: " + str(porcentaje))

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

        plt.show()


'''
def Grafica_fecha_test(diccionario, temas, s_fechas, fechas, opcion, color): La función muestra para una serie de temas 
una grafica comparando un determinado valor (nota media, test finalizados, test aprobados o porcentaje de aprobados) 
para varios intervalos de tiempo.

  - Argumentos:
      - diccionario: Diccionario que contiene los tests realizados por los estudiantes para cada uno de los temas 
      (la clave son los temas de los test y sus valores un array con los test realizados por los estudiantes).
      - temas: Temas seleccionados para los que se quiere obtener los resultados.
      - s_fechas: Intervalos de fechas seleccionados para los cuales se quiere obtener los resultados. 
      - fechas: Array con los intervalos de fechas.
      - opcion: Opción para el valor que se desea mostrar en las gráficas.
      - color: Color deseado para las barras de la gráfica.
      - diseno: opción para el diseño de la gráfica
'''


def Grafica_fecha_test(diccionario, temas, s_fechas, fechas, opcion, color, diseno):
    etiqueta = ""
    etiqueta2 = ""

    plt.rcParams.update({'figure.figsize': (10, 6), 'figure.dpi': 75})

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

        print("-----------------------------------------------------------------------------")
        print("TEMA " + str(t))

        if opcion == "Nota Media":

            etiqueta = "Nota Media"
            print("-----------------------------------------------------------------------------")
            print("NOTA MEDIA")

        elif opcion == "Participacion":

            etiqueta = "Veces Finalizado"
            print("-----------------------------------------------------------------------------")
            print("NUMERO DE VECES QUE SE HA FINALIZADO EL TEST")

        elif opcion == "Aprobados":

            etiqueta = "Veces Aprobado"
            print("-----------------------------------------------------------------------------")
            print("NUMERO DE VECES QUE SE HA APROBADO EL TEST")

        elif opcion == "% Aprobados":
            etiqueta = "Veces Finalizado"
            etiqueta2 = "Veces Aprobado"
            print("-----------------------------------------------------------------------------")
            print("COMPARACION TEST REALIZADOS - TEST APROBADOS")

        for f in fechas:
            print("-----------------------------------------------------------------------------")
            print(str(f[0]).split(' ')[0] + " -- " + str(f[1]).split(' ')[0])
            print("-----------------------------------------------------------------------------")
            x.append(str(f[0]).split(' ')[0] + " / " + str(f[1]).split(' ')[0])
            pruebas = []
            for p in diccionario[t]:
                if f[0] <= p.fecha <= f[1]:
                    pruebas.append(p)

            if opcion == "Nota Media":
                y.append(round(nota_media(pruebas), 2))
                print("La nota media del test es: " + str(round(nota_media(pruebas), 2)))
            elif opcion == "Participacion":
                finalizado = participacion(pruebas)
                y.append(finalizado)
                print("El numero de veces que se ha finalizado el test es: " + str(finalizado))
            elif opcion == "Aprobados":
                aprobado, porcentaje = aprobados(pruebas)
                y.append(aprobado)
                print("El número de veces que se ha aprobado el test es: " + str(aprobado))
            elif opcion == "% Aprobados":
                finalizado = participacion(pruebas)
                aprobado, porcentaje = aprobados(pruebas)
                y.append(finalizado)
                y2.append(aprobado)
                print("El número de veces que se ha finalizado el test es: " + str(finalizado))
                print("El número de veces que se ha aprobado el test es: " + str(aprobado))
                print("El porcentaje de aprobados del tema es: " + str(porcentaje))

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

        plt.show()


'''
def Grafica_estudiante(identificador, estudiantes, temas, s_fechas, fechas, opcion, opcion2, color): La función muestra 
para cada uno de los estudiantes una gráfica comparando un determinado valor (nota media, test finalizados, 
test aprobados o porcentaje de aprobados) para varios temas (el valor se puede comparar para un mismo tema para varios 
interalos de tiempo o para varios temas en un intervalo de tiempo)
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
      - opcion2: Opción para el valor que se desea mostrar en las gráficas (nota media, test finalizados, test aprobados 
      o porcentaje de aprobados)
      - color: Color para las barras de las gráficas
      - diseno: opción para el diseño de la gráfica
'''


def Grafica_estudiante(identificador, estudiantes, temas, s_fechas, fechas, opcion, opcion2, color, diseno):
    etiqueta = ""
    etiqueta2 = ""

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

    if opcion == "Nota Media":

        print("-----------------------------------------------------------------------------")
        print("NOTA MEDIA")

    elif opcion == "Participacion":

        print("-----------------------------------------------------------------------------")
        print("NUMERO DE VECES QUE SE HA FINALIZADO EL TEST")

    elif opcion == "Aprobados":

        print("-----------------------------------------------------------------------------")
        print("NUMERO DE VECES QUE SE HA APROBADO EL TEST")

    elif opcion == "% Aprobados":

        print("-----------------------------------------------------------------------------")
        print("COMPARACION TEST REALIZADOS - TEST APROBADOS")

    for e in identificador:

        print("-----------------------------------------------------------------------------")
        print("ESTUDIANTE: " + e)
        print("-----------------------------------------------------------------------------")

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

                    print("Tema: " + str(t))
                    print("-----------------------------------------------------------------------------")

                    for f in fechas:

                        print(str(f[0]).split(' ')[0] + " - " + str(f[1]).split(' ')[0])
                        print("-----------------------------------------------------------------------------")
                        prs = []

                        x.append(str(f[0]).split(' ')[0] + " - " + str(f[1]).split(' ')[0])

                        for p in pruebas[t]:
                            if f[0] <= p.fecha <= f[1]:
                                prs.append(p)

                        finalizado = participacion(prs)
                        aprobado, porcentaje = aprobados(prs)

                        print(opcion2)
                        if opcion2 == "Nota Media":
                            etiqueta = "Nota Media"
                            y.append(round(nota_media(prs), 2))
                            print("La nota media del estudiante es de " + str(round(nota_media(prs), 2)))
                        elif opcion2 == "Participacion":
                            etiqueta = "Finalizados"
                            y.append(finalizado)
                            print("El estudiante ha finalizado un total de " + str(finalizado) + " test")
                        elif opcion2 == "Aprobados":
                            etiqueta = "Aprobados"
                            y.append(aprobado)
                            print("El estudiante ha aprobado un total de " + str(aprobado) + " test")
                        elif opcion2 == "% Aprobados":
                            etiqueta = "Finalizados"
                            etiqueta2 = "Aprobados"
                            y.append(finalizado)
                            y2.append(aprobado)
                            print("El estudiante ha finalizado un total de " + str(finalizado) + " test")
                            print("El estudiante ha aprobado un total de " + str(aprobado) + " test")
                            print("El el porcentaje de aprobados del estudiante es " + str(porcentaje))

                    fig, ax = plt.subplots()
                    n = len(x)
                    width = 0.25

                    if diseno == 1:
                        if opcion2 == "% Aprobados":
                            ax.bar(np.arange(n), y2, width=width, label=etiqueta, color="#00ba38")
                            ax.bar(np.arange(n) - width, y, width=width, label=etiqueta2, color=color)
                        else:
                            ax.bar(np.arange(n), y, width=width, label=etiqueta, color=color)
                    else:
                        if opcion2 == "% Aprobados":
                            ax.plot(np.arange(n), y2, label=etiqueta, color="#00ba38", linestyle='solid', marker='o')
                            ax.plot(np.arange(n), y, label=etiqueta2, color=color, linestyle='solid', marker='o')
                        else:
                            ax.plot(np.arange(n), y, label=etiqueta, color=color, linestyle='solid', marker='o')

                    plt.xticks(np.arange(n), x)
                    plt.legend(loc='best')
                    plt.show()

        elif opcion == "Temas x Fecha":

            for f in fechas:

                x = []
                y = []
                y2 = []

                print("-----------------------------------------------------------------------------")
                print(str(f[0]).split(' ')[0] + " - " + str(f[1]).split(' ')[0])

                for t in temas:

                    if t in pruebas:
                        x.append(t)
                        print("-----------------------------------------------------------------------------")
                        print("Tema: " + str(t))
                        print("-----------------------------------------------------------------------------")
                        prs = []

                        for p in pruebas[t]:
                            if f[0] <= p.fecha <= f[1]:
                                prs.append(p)

                        finalizado = participacion(prs)
                        aprobado, porcentaje = aprobados(prs)

                        if opcion2 == "Nota Media":
                            etiqueta = "Nota Media"
                            y.append(round(nota_media(prs), 2))
                            print("La nota media del estudiante es de " + str(round(nota_media(prs), 2)))
                        elif opcion2 == "Participacion":
                            etiqueta = "Finalizados"
                            y.append(finalizado)
                            print("El estudiante ha finalizado un total de " + str(finalizado) + " test")
                        elif opcion2 == "Aprobados":
                            etiqueta = "Aprobados"
                            y.append(aprobado)
                            print("El estudiante ha aprobado un total de " + str(aprobado) + " test")
                        elif opcion2 == "% Aprobados":
                            etiqueta = "Finalizados"
                            etiqueta2 = "Aprobados"
                            y.append(finalizado)
                            y2.append(aprobado)
                            print("El estudiante ha finalizado un total de " + str(finalizado) + " test")
                            print("El estudiante ha aprobado un total de " + str(aprobado) + " test")
                            print("El el porcentaje de aprobados del estudiante es " + str(porcentaje))

                fig, ax = plt.subplots()
                n = len(x)
                width = 0.25

                if diseno == 1:
                    if opcion2 == "% Aprobados":
                        ax.bar(np.arange(n), y2, width=width, label=etiqueta, color="#00ba38")
                        ax.bar(np.arange(n) - width, y, width=width, label=etiqueta2, color=color)
                    else:
                        ax.bar(np.arange(n), y, width=width, label=etiqueta, color=color)
                else:
                    if opcion2 == "% Aprobados":
                        ax.plot(np.arange(n), y2, label=etiqueta, color="#00ba38", linestyle='solid', marker='o')
                        ax.plot(np.arange(n), y, label=etiqueta2, color=color, linestyle='solid', marker='o')
                    else:
                        ax.plot(np.arange(n), y, label=etiqueta, color=color, linestyle='solid', marker='o')

                plt.xticks(np.arange(n), x)
                plt.legend(loc='best')
                plt.show()


'''
def Grafica_test_fecha_comparacion(diccionario, temas, s_fechas, fechas, opcion, color, diseno, ficheros): 
La función muestra para una serie de intervalos de tiempo una gráfica comparando un determinado valor 
(nota media, test finalizados, test aprobados o porcentaje de aprobados) para varios temas, para varios ficheros.

  - Argumentos:
      - diccionario: Diccionario que contiene los tests realizados por los estudiantes para cada uno de los temas 
      (la clave son los temas de los test y sus valores un array con los test realizados por los estudiantes).
      - s_fechas: Intervalos de fechas seleccionados para los cuales se quiere obtener los resultados. 
      - fechas: Array con los intervalos de fechas.
      - opcion: Opción para el valor que se desea mostrar en las gráficas.
      - color: Color deseado para las barras de la gráfica.
      - diseno: opción para el diseño de la gráfica
      - ficheros: ficheros que se desea comparar
'''


def Grafica_test_comparacion(s_fechas, fechas, opcion, diseno, ficheros, documentos):
    dic_ficheros = {}

    etiqueta = ""
    etiqueta2 = ""

    plt.rcParams.update({'figure.figsize': (10, 6), 'figure.dpi': 75})
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
        print("-----------------------------------------------------------------------------")
        print("NOTA MEDIA")

    elif opcion == "Participacion":
        etiqueta = "Veces Finalizado "
        print("-----------------------------------------------------------------------------")
        print("NUMERO DE VECES QUE SE HA FINALIZADO EL TEST")

    elif opcion == "Aprobados":
        etiqueta = "Veces Aprobado "
        print("-----------------------------------------------------------------------------")
        print("NUMERO DE VECES QUE SE HA APROBADO EL TEST")

    elif opcion == "% Aprobados":
        etiqueta = "Veces Finalizado "
        etiqueta2 = "Veces Aprobado "
        print("-----------------------------------------------------------------------------")
        print("TEST REALIZADOS - TEST APROBADOS")

    for fch in dic_ficheros.keys():

        print("-----------------------------------------------------------------------------")
        print(fch)
        y = []
        y2 = []

        for f in fechas:
            print("-----------------------------------------------------------------------------")
            print(str(f[0]).split(' ')[0] + " - " + str(f[1]).split(' ')[0])

            pruebas = []

            for t in dic_ficheros[fch]:
                if f[0] <= t.fecha <= f[1]:
                    pruebas.append(t)

            if opcion == "Nota Media":

                media = round(nota_media(pruebas), 2)
                y.append(media)
                print("La nota media es: " + str(media))

            elif opcion == "Participacion":

                finalizado = participacion(pruebas)
                y.append(finalizado)
                print("El numero de veces que se ha finalizado el test es: " + str(finalizado))

            elif opcion == "Aprobados":

                aprobado, porcentaje = aprobados(pruebas)
                y.append(aprobado)
                print("El número de veces que se ha aprobado el test es: " + str(aprobado))

            elif opcion == "% Aprobados":

                finalizado = participacion(pruebas)
                aprobado, porcentaje = aprobados(pruebas)

                y.append(finalizado)
                y2.append(aprobado)

                print("El número de veces que se ha finalizado el test es: " + str(finalizado))
                print("El número de veces que se ha aprobado el test es: " + str(aprobado))
                print("El porcentaje de aprobados es: " + str(porcentaje) + "%")

        valores_grafica[fch] = [y, y2]

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

    plt.show()
