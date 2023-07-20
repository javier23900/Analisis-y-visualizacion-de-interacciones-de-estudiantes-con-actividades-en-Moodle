import matplotlib.pyplot as plt
import numpy as np
from Analizar_Datos_test import *

'''
def Grafica_registros(identificador, diccionario, s_fechas, fechas, estudiantes, color, IP): La función muestra, para 
el grupo en general o para cada uno de los estdiantes una gráfica comparando el número de registros de acceso a Moodle 
a un recurso indicado para los intervalos de tiempo deseados.

    - Argumentos:
        - identificador: Identidicador del recurso de Moodle.
        - s_fechas: Intervalos de fechas seleccionados para los cuales se quiere obtener los resultados. 
        - fechas: Array con los intervalos de fechas.
        - estudiantes: Estudiantes seleccionados para los que se desea obtener la información.
        - color: Color para las barras de las gráficas.
        - IP: Dirección IP desde la cual se ha accedido a Moodle.
        - diseno: Opción para el diseño de la gráfica
        - diccionario_estudiantes: Diccionario con los estudiantes y sus registros de acceso. La clave del diccionario 
        es el identificador del estudiante y para cada clave su valor es un array de objetos de tipo Registros.
'''


def Grafica_registros(identificador, s_fechas, fechas, estudiantes, color, IP, diseno,
                      diccionario_estudiantes):
    etiqueta = "Accesos"
    contador = 0

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

    if estudiantes[0] == "Todos":
        estudiantes = []
        for e in diccionario_estudiantes.keys():
            estudiantes.append(e)

    if estudiantes[0] == "Grupo":
        x = []
        y = []

        print("-----------------------------------------------------------------------------")
        print("REGISTROS DEL GRUPO")

        for f in fechas:
            print("-----------------------------------------------------------------------------")
            print(str(f[0]).split(' ')[0] + " -- " + str(f[1]).split(' ')[0])
            print("-----------------------------------------------------------------------------")
            x.append(str(f[0]).split(' ')[0] + " / " + str(f[1]).split(' ')[0])

            contador = 0
            for e in diccionario_estudiantes:
                for r in diccionario_estudiantes[e].registros:
                    if f[0] <= r.fecha <= f[1]:
                        if IP != '':
                            print(IP)
                            print(r.IP)
                            if identificador in r.descripcion and r.IP == IP:
                                contador += 1
                        else:
                            if identificador in r.descripcion:
                                contador += 1

            y.append(contador)

            if IP != '':
                print("Número de veces que el grupo ha accedido al recurso con identificador " + identificador + " : " +
                      str(contador) + " a través de la dirección IP " + IP)
            else:
                print("Número de veces que el grupo ha accedido al recurso con identificador " + identificador + ": " +
                      str(contador))

        fig, ax = plt.subplots()
        n = len(x)
        width = 0.25

        if diseno == 1:
            ax.bar(np.arange(n), y, width=width, label=etiqueta, color=color)
        else:
            ax.plot(np.arange(n), y, width=width, label=etiqueta, color=color)

        plt.xticks(np.arange(n), x)
        plt.legend(loc='best')

        plt.show()

    else:

        for e in estudiantes:

            x = []
            y = []

            print("-----------------------------------------------------------------------------")
            print("ESTUDIANTE: " + e)

            for f in fechas:
                contador = 0

                print("-----------------------------------------------------------------------------")
                print(str(f[0]).split(' ')[0] + " -- " + str(f[1]).split(' ')[0])
                print("-----------------------------------------------------------------------------")
                x.append(str(f[0]).split(' ')[0] + " / " + str(f[1]).split(' ')[0])

                for r in diccionario_estudiantes[e].registros:
                    if f[0] <= r.fecha <= f[1]:
                        if IP != '':
                            if identificador in r.descripcion and r.IP == IP:
                                contador += 1
                        else:
                            if identificador in r.descripcion:
                                contador += 1

                if IP != '':
                    print(
                        "Número de veces que el estudiante ha accedido al recurso con identificador " + identificador +
                        " : " + str(contador) + " a través de la dirección IP " + IP)
                else:
                    print(
                        "Número de veces que el estudiante ha accedido al recurso con identificador " + identificador
                        + ": " + str(contador))

                y.append(contador)

            fig, ax = plt.subplots()
            n = len(x)
            width = 0.25

            if diseno == 1:
                ax.bar(np.arange(n), y, width=width, label=etiqueta, color=color)
            else:
                ax.plot(np.arange(n), y, label=etiqueta, color=color, linestyle='solid', marker='o')

            plt.xticks(np.arange(n), x)
            plt.legend(loc='best')

            plt.show()
