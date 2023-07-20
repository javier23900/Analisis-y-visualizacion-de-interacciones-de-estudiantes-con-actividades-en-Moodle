from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
from Analizar_Datos_test import *
import shutil

'''
def analisis_fechas_temario_pdf(diccionario, temas, s_fechas, fechas, documento): Función encargada de analizar los test de un tema para una serie de intervalos de fechas y descargar el documento pdf correspondiente con dicha información.
  - Argumentos:
      - diccionario: Diccionario que contiene los tests realizados por los estudiantes para cada uno de los temas (la clave son los temas de los test y su valor un array con los test realizados por los estudiantes).
      - temas: Temas seleccionados para los que se quiere obtener los resultados.
      - s_fechas: Intervalos de fechas seleccionados para los cuales se quiere obtener los resultados. 
      - fechas: Array con los intervalos de fechas.
      - documento: Objeto que representa el documento a descargar.
      - nombre_documento: Nombre del documento a descargar.
      - carpeta: Carpeta destino para el documento a descargar
'''


def analisis_fechas_temario_pdf(diccionario, temas, s_fechas, fechas, documento, nombre_documento, carpeta):
    w, h = A4
    cursor = 75
    documento.setFont("Times-Roman", 16)
    documento.drawString(50, h - int(cursor), "EVOLUCIÓN DE LOS TEMAS")
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

        documento.drawString(50, h - int(cursor),
                             "-----------------------------------------------------------------------------")
        cursor += 15
        documento.drawString(50, h - int(cursor), "TEMA " + str(t))
        cursor += 20

        for f in fechas:

            if h - cursor < 140:
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
            for p in diccionario[t]:
                if f[0] <= p.fecha <= f[1]:
                    pruebas.append(p)

            cursor = analisis_test_pdf(pruebas, documento, cursor)

        documento.showPage()
        documento.setFont("Times-Roman", 12)
        cursor = 75

    documento.save()
    if carpeta != "":
        shutil.move(nombre_documento, carpeta)

    '''
  def analisis_temario_fechas_pdf(diccionario, temas, s_fechas, fechas, documento): Función encargada de analizar los 
  test para una serie de intervalos de fechas para una serie de temas y descargar el documento pdf correspondiente con 
  dicha información.
  - Argumentos:
      - diccionario: Diccionario que contiene los tests realizados por los estudiantes para cada uno de los temas 
      (la clave son los temas de los test y su valor un array con los test realizados por los estudiantes).
      - temas: Temas seleccionados para los que se quiere obtener los resultados.
      - s_fechas: Intervalos de fechas seleccionados para los cuales se quiere obtener los resultados. 
      - fechas: Array con los intervalos de fechas.
      - documento: Objeto que representa el documento a descargar.
      - nombre_documento: Nombre del documento a descargar.
      - carpeta: Carpeta destino para el documento a descargar
  '''


def analisis_temario_fechas_pdf(diccionario, temas, s_fechas, fechas, documento, nombre_documento, carpeta):
    w, h = A4
    cursor = 75
    documento.setFont("Times-Roman", 16)
    documento.drawString(50, h - int(cursor), "COMPARACIÓN DE LOS TEMAS")
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

    for f in fechas:

        documento.drawString(50, h - int(cursor),
                             "-----------------------------------------------------------------------------")
        cursor += 15
        documento.drawString(50, h - int(cursor), str(f[0]).split(' ')[0] + " - " + str(f[1]).split(' ')[0])
        cursor += 15

        for t in temas:

            pruebas = []

            if h - cursor < 255:
                documento.showPage()
                documento.setFont("Times-Roman", 12)
                cursor = 75

            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 15
            documento.drawString(50, h - int(cursor), "TEMA " + str(t))
            cursor += 15
            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 15

            for p in diccionario[t]:
                if f[0] <= p.fecha <= f[1]:
                    pruebas.append(p)

            cursor = analisis_test_pdf(pruebas, documento, cursor)

        documento.showPage()
        documento.setFont("Times-Roman", 12)
        cursor = 75

    documento.save()
    if carpeta != "":
        shutil.move(nombre_documento, carpeta)


'''
def analisis_test_pdf(test, documento, cursor): Función encargada de analizar un conjunto de pruebas mostrando en el 
documento el numero de veces que se ha finalizado el test, el numero de veces que se ha aprobado, el porcentaje de 
aprobados que tiene y la nota media del conjunto.
- Argumentos:
    - test: Conjunto de pruebas realizadas para un determinado tema en un intervalo de fechas.
    - documento: Objeto que representa el documento a descargar.
    - cursor: Posición en el documento escribir la información.
'''


def analisis_test_pdf(test, documento, cursor):
    w, h = A4
    aprobado, porcentaje = aprobados(test)

    documento.drawString(50, h - int(cursor), "El test se ha finalizado " + str(participacion(test)) + " veces")
    cursor += 20
    documento.drawString(50, h - int(cursor), "El test se ha aprobado " + str(aprobado) + " veces")
    cursor += 20
    documento.drawString(50, h - int(cursor), "El porcentaje de aprobados es del " + str(round(porcentaje, 2)) + "%")
    cursor += 20
    documento.drawString(50, h - int(cursor), "La nota media del test es: " + str(round(nota_media(test), 2)))
    cursor += 20

    return cursor


'''
def ranking_test_pdf(diccionario, s_fechas, fechas, opcion, documento): Función encargada de ordenar los temas de 
mejores a peores para una serie de valores y descargar el documento pdf correspondiente con dicha información.
- Argumentos:
  - diccionario: Diccionario que contiene los tests realizados por los estudiantes para cada uno de los temas 
  (la clave son los temas de los test y su valor un array con los test realizados por los estudiantes).
  - s_fechas: Intervalos de fechas seleccionados para los cuales se quiere obtener los resultados. 
  - fechas: Array con los intervalos de fechas.
  - opcion: Opción para el valor para el cual se quiere realizar el ranking (Nota media de los test, número de veces que 
  se ha completado el test, número de veces que se a aprobado el test y porcentaje de aprobados).
  - documento: Objeto que representa el documento a descargar.
  - nombre_documento: Nombre del documento a descargar.
  - carpeta: Carpeta destino para el documento a descargar
'''


def ranking_test_pdf(diccionario, s_fechas, fechas, opcion, documento, nombre_documento, carpeta):
    w, h = A4
    cursor = 75
    documento.setFont("Times-Roman", 16)
    documento.drawString(50, h - int(cursor), "RANKING DE LOS TEMAS")
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

    for f in fechas:
        posicion = 1
        temas = []

        documento.drawString(50, h - int(cursor),
                             "-----------------------------------------------------------------------------")
        cursor += 15
        documento.drawString(50, h - int(cursor), str(f[0]).split(' ')[0] + " - " + str(f[0]).split(' ')[0])
        cursor += 15

        for t in diccionario.keys():
            pruebas = []
            for p in diccionario[t]:
                if f[0] <= p.fecha <= f[1]:
                    pruebas.append(p)
            temas.append(pruebas)

        if opcion == "Nota Media":
            # POR NOTA MEDIA
            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 15
            documento.drawString(50, h - int(cursor), "OPCIÓN: NOTA MEDIA")
            cursor += 15
            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 20

            temas.sort(key=lambda x: nota_media(x), reverse=True)
            for t in temas:
                if len(t) > 0:

                    if h - cursor < 140:
                        documento.showPage()
                        documento.setFont("Times-Roman", 12)
                        cursor = 75

                    documento.drawString(50, h - int(cursor), str(posicion) + "º: " + t[0].tema)
                    cursor += 15
                    documento.drawString(50, h - int(cursor), "Nota media: " + str(round(nota_media(t), 2)))
                    cursor += 30

                    posicion += 1

        elif opcion == "Participacion":

            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 15
            documento.drawString(50, h - int(cursor), "OPCIÓN: PARTICIPACIÓN DE LOS ALUMNOS")
            cursor += 15
            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 20

            temas.sort(key=lambda x: participacion(x), reverse=True)
            for t in temas:
                if len(t) > 0:

                    if h - cursor < 140:
                        documento.showPage()
                        documento.setFont("Times-Roman", 12)
                        cursor = 75

                    documento.drawString(50, h - int(cursor), str(posicion) + "º: " + t[0].tema)
                    cursor += 15
                    documento.drawString(50, h - int(cursor),
                                         "Veces que se ha realizado el test: " + str(participacion(t)))
                    cursor += 30

                    posicion += 1

        elif opcion == "Aprobados":

            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 15
            documento.drawString(50, h - int(cursor), "OPCIÓN: TEST APROBADOS")
            cursor += 15
            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 20

            temas.sort(key=lambda x: aprobados(x)[0], reverse=True)
            for t in temas:
                if len(t) > 0:
                    n_aprobados, porcentaje = aprobados(t)

                    if h - cursor < 140:
                        documento.showPage()
                        documento.setFont("Times-Roman", 12)
                        cursor = 75

                    documento.drawString(50, h - int(cursor), str(posicion) + "º: " + t[0].tema)
                    cursor += 15
                    documento.drawString(50, h - int(cursor),
                                         "Veces que se ha aprobado el test: " + str(round(n_aprobados, 2)))
                    cursor += 30

                    posicion += 1

        elif opcion == "% Aprobados":

            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 15
            documento.drawString(50, h - int(cursor), "OPCIÓN: PORCENTAJE DE APROBADOS")
            cursor += 15
            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 20

            temas.sort(key=lambda x: aprobados(x)[1], reverse=True)
            for t in temas:
                if len(t) > 0:
                    n_aprobados, porcentaje = aprobados(t)

                    if h - cursor < 180:
                        documento.showPage()
                        documento.setFont("Times-Roman", 12)
                        cursor = 75

                    documento.drawString(50, h - int(cursor), str(posicion) + "º: " + t[0].tema)
                    cursor += 15
                    documento.drawString(50, h - int(cursor),
                                         "Veces que se ha realizado el test: " + str(participacion(t)))
                    cursor += 15
                    documento.drawString(50, h - int(cursor),
                                         "Veces que se ha aprobado el test: " + str(round(n_aprobados, 2)))
                    cursor += 15
                    documento.drawString(50, h - int(cursor), "Porcentaje de aprobados: " + str(round(porcentaje, 2)))
                    cursor += 30

                    posicion += 1

        documento.showPage()
        documento.setFont("Times-Roman", 12)
        cursor = 75

    documento.save()
    if carpeta != "":
        shutil.move(nombre_documento, carpeta)


'''
  Resultados_estudiante_pdf(identificador, pruebas, temas, s_fechas, fechas, opcion, documento, nombre_documento, 
  carpeta): Función encargada de analizar los test realizados por un estudiante y descargar el documento pdf 
  correspondiente con dicha información.
  - Argumentos:
      - identificador: Identificador del estudiante.
      - pruebas: Diccionario con los estudiantes y sus test realizados. La clave del diccionario es el identificador del 
      estudiante y para cada clave su valor es un diccionario con los test. Este segundo diccionario tiene como clave el 
      tema al que pertenecen los test y para cada clave su valor es un array que contiene los test realizados por los 
      estudiantes.
      - temas: Temas seleccionados para los que se quiere obtener los resultados.
      - s_fechas: Intervalos de fechas seleccionados para los cuales se quiere obtener los resultados. 
      - fechas: Array con los intervalos de fechas.
      - opcion: Opción para el tipo de análisis que queremos realizar sobre los test realizados por el estudiante 
      (Evolución para cada uno de los temas para una serie de intervalos de fechas o comparativa de una serie de temas 
      para una serie de intervalos de fechas)
      - documento: Objeto que representa el documento a descargar.
      - nombre_documento: Nombre del documento a descargar.
      - carpeta: Carpeta destino para el documento a descargar
  '''


def Resultados_estudiante_pdf(identificador, estudiantes, temas, s_fechas, fechas, opcion, documento, nombre_documento,
                              carpeta):
    w, h = A4
    cursor = 75
    documento.setFont("Times-Roman", 16)
    documento.drawString(50, h - int(cursor), "INFORMACIÓN ESTUDIANTES")
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

    if identificador[0] == "Todos":
        identificador = []
        for e in estudiantes.keys():
            identificador.append(e)

    for e in identificador:

        pruebas = estudiantes[e].pruebas

        if temas[0] == "Todos":
            temas = []
            for t in pruebas:
                temas.append(t)

        if opcion == "Fechas x Temas":

            for t in temas:

                documento.drawString(50, h - int(cursor),
                                     "-----------------------------------------------------------------------------")
                cursor += 15
                documento.drawString(50, h - int(cursor), "ESTUDIANTE " + e)
                cursor += 15
                documento.drawString(50, h - int(cursor),
                                     "-----------------------------------------------------------------------------")
                cursor += 20

                documento.drawString(50, h - int(cursor), "Tema " + t)
                cursor += 15

                for f in fechas:

                    if h - cursor < 170:
                        documento.showPage()
                        documento.setFont("Times-Roman", 12)
                        cursor = 75

                    documento.drawString(50, h - int(cursor),
                                         "----------------------------------------------------------------------------")
                    cursor += 15
                    documento.drawString(50, h - int(cursor), str(f[0]).split(' ')[0] + " - " + str(f[0]).split(' ')[0])
                    cursor += 15
                    documento.drawString(50, h - int(cursor),
                                         "----------------------------------------------------------------------------")
                    cursor += 15

                    prs = []
                    if t in pruebas:
                        for p in pruebas[t]:
                            if f[0] <= p.fecha <= f[1]:
                                prs.append(p)

                        finalizado = participacion(prs)
                        aprobado, porcentaje = aprobados(prs)

                        documento.drawString(50, h - int(cursor),
                                             "El estudiante ha finalizado un total de " + str(finalizado) + " test")
                        cursor += 15
                        documento.drawString(50, h - int(cursor),
                                             "El estudiante ha aprobado un total de " + str(aprobado) + " test")
                        cursor += 15
                        documento.drawString(50, h - int(cursor),
                                             "La nota media del estudiante es de " + str(round(nota_media(prs), 2)))
                        cursor += 15
                        documento.drawString(50, h - int(cursor),
                                             "El el porcentaje de aprobados del estudiante es " + str(porcentaje) + "%")
                        cursor += 20

                documento.showPage()
                documento.setFont("Times-Roman", 12)
                cursor = 75

        elif opcion == "Temas x Fechas":

            for f in fechas:

                documento.drawString(50, h - int(cursor),
                                     "-----------------------------------------------------------------------------")
                cursor += 15
                documento.drawString(50, h - int(cursor), "ESTUDIANTE " + e)
                cursor += 15
                documento.drawString(50, h - int(cursor),
                                     "-----------------------------------------------------------------------------")
                cursor += 20

                documento.drawString(50, h - int(cursor), str(f[0]).split(' ')[0] + " - " + str(f[0]).split(' ')[0])
                cursor += 20

                for t in temas:

                    if h - cursor < 180:
                        documento.showPage()
                        documento.setFont("Times-Roman", 12)
                        cursor = 75

                    documento.drawString(50, h - int(cursor),
                                         "----------------------------------------------------------------------------")
                    cursor += 15
                    documento.drawString(50, h - int(cursor), "Tema " + t)
                    cursor += 15
                    documento.drawString(50, h - int(cursor),
                                         "----------------------------------------------------------------------------")
                    cursor += 15

                    prs = []
                    if t in pruebas:
                        for p in pruebas[t]:
                            if f[0] <= p.fecha <= f[1]:
                                prs.append(p)

                        finalizado = participacion(prs)
                        aprobado, porcentaje = aprobados(prs)

                        documento.drawString(50, h - int(cursor),
                                             "El estudiante ha finalizado un total de " + str(finalizado) + " test")
                        cursor += 15
                        documento.drawString(50, h - int(cursor),
                                             "El estudiante ha aprobado un total de " + str(aprobado) + " test")
                        cursor += 15
                        documento.drawString(50, h - int(cursor),
                                             "La nota media del estudiante es de " + str(round(nota_media(prs), 2)))
                        cursor += 15
                        documento.drawString(50, h - int(cursor),
                                             "El porcentaje de aprobados del estudiante es " + str(porcentaje))
                        cursor += 20

                documento.showPage()
                documento.setFont("Times-Roman", 12)
                cursor = 75

    documento.save()
    if carpeta != "":
        shutil.move(nombre_documento, carpeta)


'''
def ranking_test_estudiante_pdf(identificador, estudiantes, s_fechas, fechas, opcion, documento, carpeta): Función 
encargada de ordenar los temas para una serie de valores en ciertos intervalos de tiempo para los estudiantes y 
descargar el documento pdf correspondiente con dicha información.

- Argumentos:
  - identificador: Estudiantes seleccionados para los cuales se quiere obtener los resultados.
  - estudiantes: Diccionario con los estudiantes y sus test realizados. La clave del diccionario es el identificador del 
  estudiante y para cada clave su valor es un diccionario con los test. Este segundo diccionario tiene como clave el 
  tema al que pertenecen los test y para cada clave su valor es un array que contiene los test realizados por los 
  estudiantes.
  - s_fechas: Intervalos de fechas seleccionados para los cuales se quiere obtener los resultados. 
  - fechas: Array con los intervalos de fechas.
  - opcion: Opción para el valor para el cual se quiere realizar el ranking (Nota media de los test, número de veces que 
  se ha completado el test, número de veces que se a aprobado el test y porcentaje de aprobados).
  - documento: Objeto que representa el documento a descargar.
  - nombre_documento: Nombre del documento a descargar.
  - carpeta: Carpeta destino para el documento a descargar
'''


def ranking_test_estudiante_pdf(identificador, estudiantes, s_fechas, fechas, opcion, documento, nombre_documento,
                                carpeta):
    w, h = A4
    cursor = 75
    documento.setFont("Times-Roman", 16)
    documento.drawString(50, h - int(cursor), "RANKING TEMAS X ESTUDIANTES")
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

    if identificador[0] == "Todos":
        identificador = []
        for e in estudiantes.keys():
            identificador.append(e)

    if opcion == "Nota Media":
        documento.drawString(50, h - int(cursor),
                             "-----------------------------------------------------------------------------")
        cursor += 15
        documento.drawString(50, h - int(cursor), "OPCIÓN: NOTA MEDIA")
        cursor += 15

    elif opcion == "Participacion":
        documento.drawString(50, h - int(cursor),
                             "-----------------------------------------------------------------------------")
        cursor += 15
        documento.drawString(50, h - int(cursor), "OPCIÓN: PARTICIPACIÓN DE LOS ALUMNOS")
        cursor += 15

    elif opcion == "Aprobados":
        documento.drawString(50, h - int(cursor),
                             "-----------------------------------------------------------------------------")
        cursor += 15
        documento.drawString(50, h - int(cursor), "OPCIÓN: TEST APROBADOS")
        cursor += 15

    elif opcion == "% Aprobados":
        documento.drawString(50, h - int(cursor),
                             "-----------------------------------------------------------------------------")
        cursor += 15
        documento.drawString(50, h - int(cursor), "OPCIÓN: PORCENTAJE DE APROBADOS")
        cursor += 15

    for e in identificador:

        documento.drawString(50, h - int(cursor),
                             "-----------------------------------------------------------------------------")
        cursor += 15
        documento.drawString(50, h - int(cursor), "ESTUDIANTE " + e)
        cursor += 15

        for f in fechas:
            temas = []

            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 15
            documento.drawString(50, h - int(cursor), str(f[0]).split(' ')[0] + " - " + str(f[0]).split(' ')[0])
            cursor += 15
            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 20

            for t in estudiantes[e].pruebas:
                prs = []
                for p in estudiantes[e].pruebas[t]:
                    if f[0] <= p.fecha <= f[1]:
                        prs.append(p)
                temas.append(prs)

            if opcion == "Nota Media":

                temas.sort(key=lambda x: nota_media(x), reverse=True)
                posicion = 0
                for t in temas:
                    if len(t) > 0:
                        posicion += 1

                        if h - cursor < 100:
                            documento.showPage()
                            documento.setFont("Times-Roman", 12)
                            cursor = 75

                        documento.drawString(50, h - int(cursor), str(posicion) + "º: " + t[0].tema)
                        cursor += 15
                        documento.drawString(50, h - int(cursor), "Nota media: " + str(round(nota_media(t), 2)))
                        cursor += 20

            elif opcion == "Participacion":

                temas.sort(key=lambda x: participacion(x), reverse=True)
                posicion = 0
                for t in temas:
                    if len(t) > 0:
                        posicion += 1

                        if h - cursor < 100:
                            documento.showPage()
                            documento.setFont("Times-Roman", 12)
                            cursor = 75

                        documento.drawString(50, h - int(cursor), str(posicion) + "º: " + t[0].tema)
                        cursor += 15
                        documento.drawString(50, h - int(cursor),
                                             "Veces que se ha realizado el test: " + str(participacion(t)))
                        cursor += 20

            elif opcion == "Aprobados":

                temas.sort(key=lambda x: aprobados(x)[0], reverse=True)
                posicion = 0
                for t in temas:
                    if len(t) > 0:
                        n_aprobados, porcentaje = aprobados(t)
                        posicion += 1

                        if h - cursor < 100:
                            documento.showPage()
                            documento.setFont("Times-Roman", 12)
                            cursor = 75

                        documento.drawString(50, h - int(cursor), str(posicion) + "º: " + t[0].tema)
                        cursor += 15
                        documento.drawString(50, h - int(cursor),
                                             "Veces que se ha aprobado el test: " + str(round(n_aprobados, 2)))
                        cursor += 20

            elif opcion == "% Aprobados":

                temas.sort(key=lambda x: aprobados(x)[1], reverse=True)
                posicion = 0
                for t in temas:
                    if len(t) > 0:
                        n_aprobados, porcentaje = aprobados(t)
                        posicion += 1

                        if h - cursor < 130:
                            documento.showPage()
                            documento.setFont("Times-Roman", 12)
                            cursor = 75

                        documento.drawString(50, h - int(cursor), str(posicion) + "º: " + t[0].tema)
                        cursor += 15
                        documento.drawString(50, h - int(cursor),
                                             "Veces que se ha realizado el test: " + str(participacion(t)))
                        cursor += 15
                        documento.drawString(50, h - int(cursor),
                                             "Veces que se ha aprobado el test: " + str(round(n_aprobados, 2)))
                        cursor += 15
                        documento.drawString(50, h - int(cursor),
                                             "Porcentaje de aprobados: " + str(round(porcentaje, 2)) + "%")
                        cursor += 20

            documento.showPage()
            documento.setFont("Times-Roman", 12)
            cursor = 75

        documento.showPage()
        documento.setFont("Times-Roman", 12)
        cursor = 75

    documento.save()
    if carpeta != "":
        shutil.move(nombre_documento, carpeta)

    '''
  def ranking_estudiantes_pdf(identificador, estudiantes, s_temas, temas, s_fechas, fechas, opcion, documento): Función 
  encargada de ordenar a los estudiantes de mejores a peores para una serie de valores en ciertos intervalos de tiempo 
  y descargar el documento pdf correspondiente con dicha información.

  - Argumentos:
    - identificador: Estudiantes seleccionados para los cuales se quiere obtener los resultados.
    - estudiantes: Diccionario con los estudiantes y sus test realizados. La clave del diccionario es el identificador 
    del estudiante y para cada clave su valor es un diccionario con los test. Este segundo diccionario tiene como clave 
    el tema al que pertenecen los test y para cada clave su valor es un array que contiene los test realizados por los 
    estudiantes.
    - s_temas: Temas seleccionados para los cuales se quiere obtener los resultados.
    - temas: Temas seleccionados para los que se quiere obtener los resultados.
    - s_fechas: Intervalos de fechas seleccionados para los cuales se quiere obtener los resultados. 
    - fechas: Array con los intervalos de fechas.
    - opcion: Opción para el valor para el cual se quiere realizar el ranking (Nota media de los test, número de veces 
    que se ha completado el test, número de veces que se a aprobado el test y porcentaje de aprobados).
    - documento: Objeto que representa el documento a descargar.
    - nombre_documento: Nombre del documento a descargar.
    - carpeta: Carpeta destino para el documento a descargar
  '''


def ranking_estudiantes_pdf(estudiantes, s_temas, temas, s_fechas, fechas, opcion, documento,
                            nombre_documento, carpeta):
    w, h = A4
    cursor = 75
    documento.setFont("Times-Roman", 16)
    documento.drawString(50, h - int(cursor), "RANKING ESTUDIANTES")
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

    if s_temas[0] != "Todos":
        temas = []
        for t in s_temas:
            temas.append(t)

    for f in fechas:

        documento.drawString(50, h - int(cursor),
                             "-----------------------------------------------------------------------------")
        cursor += 15
        documento.drawString(50, h - int(cursor), str(f[0]).split(' ')[0] + " - " + str(f[0]).split(' ')[0])
        cursor += 20

        for t in temas:

            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 15
            documento.drawString(50, h - int(cursor), "Tema " + t)
            cursor += 15
            documento.drawString(50, h - int(cursor),
                                 "-----------------------------------------------------------------------------")
            cursor += 20

            estd = []

            for e in estudiantes:

                prs = []

                if t in estudiantes[e].pruebas:
                    for p in estudiantes[e].pruebas[t]:
                        if f[0] <= p.fecha <= f[1]:
                            prs.append(p)

                    estudiantes[e].paux = prs
                    if len(prs) > 0:
                        estd.append(e)

            if opcion == "Nota Media":
                posicion = 0
                # POR NOTA MEDIA
                documento.drawString(50, h - int(cursor), "OPCIÓN: NOTA MEDIA")
                cursor += 20

                estd.sort(key=lambda x: nota_media(estudiantes[x].paux), reverse=True)  # .reverse()

                for e in estd:
                    posicion += 1

                    if h - cursor < 110:
                        documento.showPage()
                        documento.setFont("Times-Roman", 12)
                        cursor = 75

                    documento.drawString(50, h - int(cursor), str(posicion) + "º: " + e)
                    cursor += 15
                    documento.drawString(50, h - int(cursor),
                                         "Nota media: " + str(round(nota_media(estudiantes[e].paux), 2)))
                    cursor += 20

            elif opcion == "Participacion":

                documento.drawString(50, h - int(cursor), "OPCIÓN: PARTICIPACIÓN")
                cursor += 20

                estd.sort(key=lambda x: participacion(estudiantes[x].paux), reverse=True)
                posicion = 0
                for e in estd:
                    posicion += 1

                    if h - cursor < 110:
                        documento.showPage()
                        documento.setFont("Times-Roman", 12)
                        cursor = 75

                    documento.drawString(50, h - int(cursor), str(posicion) + "º: " + e)
                    cursor += 15
                    documento.drawString(50, h - int(cursor), "Veces que se ha realizado el test: " + str(
                        participacion(estudiantes[e].paux)))
                    cursor += 20

            elif opcion == "Aprobados":

                documento.drawString(50, h - int(cursor), "OPCIÓN: TEST APROBADOS")
                cursor += 20

                estd.sort(key=lambda x: aprobados(estudiantes[x].paux)[0], reverse=True)
                posicion = 0
                for e in estd:
                    posicion += 1
                    n_aprobados, porcentaje = aprobados(estudiantes[e].paux)

                    if h - cursor < 110:
                        documento.showPage()
                        documento.setFont("Times-Roman", 12)
                        cursor = 75

                    documento.drawString(50, h - int(cursor), str(posicion) + "º: " + e)
                    cursor += 15
                    documento.drawString(50, h - int(cursor),
                                         "Veces que se ha aprobado el test: " + str(round(n_aprobados, 2)))
                    cursor += 20

            elif opcion == "% Aprobados":

                documento.drawString(50, h - int(cursor), "OPCIÓN: PORCENTAJE DE APROBADOS")
                cursor += 20

                estd.sort(key=lambda x: aprobados(estudiantes[x].paux)[1], reverse=True)
                posicion = 0
                for e in estd:
                    posicion += 1
                    n_aprobados, porcentaje = aprobados(estudiantes[e].paux)

                    if h - cursor < 140:
                        documento.showPage()
                        documento.setFont("Times-Roman", 12)
                        cursor = 75

                    documento.drawString(50, h - int(cursor), str(posicion) + "º: " + e)
                    cursor += 15
                    documento.drawString(50, h - int(cursor), "Veces que se ha realizado el test: " + str(
                        participacion(estudiantes[e].paux)))
                    cursor += 15
                    documento.drawString(50, h - int(cursor),
                                         "Veces que se ha aprobado el test: " + str(round(n_aprobados, 2)))
                    cursor += 15
                    documento.drawString(50, h - int(cursor),
                                         "Porcentaje de aprobados: " + str(round(porcentaje, 2)) + "%")
                    cursor += 20

            documento.showPage()
            documento.setFont("Times-Roman", 12)
            cursor = 75

    documento.save()

    if carpeta != "":
        shutil.move(nombre_documento, carpeta)
