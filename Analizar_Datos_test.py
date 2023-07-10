from datetime import datetime

'''def nota_media(pruebas): Función encargada de calcular la nota media para un conjunto de pruebas.
  - Argumentos:
      - pruebas: array con todas las pruebas realizadas para un determinado test.
  - Resultado: Devuelve la nota media para un conjunto de pruebas (nota media de los resultados obtenidos)
'''


def nota_media(pruebas):
    total = 0
    contador = 0
    for p in pruebas:
        if p.estado == 'Finalizado':
            contador += 1
            total += float(p.calificacion_total.replace(",", "."))

    if contador == 0:
        return total
    else:
        return total / contador


'''def analisis_fechas_temario(diccionario, temas, s_fechas, fechas): Función encargada de analizar los test de un 
tema para una serie de intervalos de fechas. 
- Argumentos: 
  - diccionario: Diccionario que contiene los tests realizados por los estudiantes para cada uno de los temas 
  (la clave son los temas de los test y su valor un array con los test realizados por los estudiantes). 
  - temas: Temas seleccionados para los que se quiere obtener los resultados. 
  - s_fechas: Intervalos de fechas seleccionados para los cuales se quiere obtener los resultados. 
  - fechas: Array con los intervalos de fechas. 
  
  (Muestra información del conjunto de test de forma que podemos observar 
  como los resultados del grupo cambian para una serie de intervalos de fechas para cada uno de los temas deseados)
'''


def analisis_fechas_temario(diccionario, temas, s_fechas, fechas):
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

        print("-----------------------------------------------------------------------------")
        print("TEMA " + str(t))

        for f in fechas:
            print("-----------------------------------------------------------------------------")
            print(str(f[0]).split(' ')[0] + " - " + str(f[1]).split(' ')[0])
            print("-----------------------------------------------------------------------------")
            pruebas = []
            for p in diccionario[t]:
                if f[0] <= p.fecha <= f[1]:  # p.fecha >= f[0] and p.fecha <= f[1]:
                    pruebas.append(p)

            analisis_test(pruebas)


'''
def analisis_temario_fechas(diccionario, temas, s_fechas, fechas): Función encargada de analizar los test para una serie
 de intervalos de fechas para una serie de temas.
  - Argumentos:
      - diccionario: Diccionario que contiene los tests realizados por los estudiantes para cada uno de los temas 
      (la clave son los temas de los test y su valor un array con los test realizados por los estudiantes).
      - temas: Temas seleccionados para los que se quiere obtener los resultados.
      - s_fechas: Intervalos de fechas seleccionados para los cuales se quiere obtener los resultados. 
      - fechas: Array con los intervalos de fechas.
      
(Muestra información del conjunto de test de forma que podemos comparar los resultados obtenidos para los temas en cada 
uno de los intervalos de fechas)
'''


def analisis_temario_fechas(diccionario, temas, s_fechas, fechas):
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
        print("-----------------------------------------------------------------------------")
        print(str(f[0]).split(' ')[0] + " - " + str(f[1]).split(' ')[0])

        for t in temas:
            pruebas = []
            print("-----------------------------------------------------------------------------")
            print("TEMA " + str(t))
            print("-----------------------------------------------------------------------------")

            for p in diccionario[t]:
                if f[0] <= p.fecha <= f[1]:  # p.fecha >= f[0] and p.fecha <= f[1]:
                    pruebas.append(p)

            analisis_test(pruebas)


'''
def analisis_test(test): Función encargada de analizar un conjunto de pruebas mostrando el numero de veces que se ha 
finalizado el test, el numero de veces que se ha aprobado, el porcentaje de aprobados que tiene y la nota media del 
conjunto.
- Argumentos:
    - test: Conjunto de pruebas realizadas.
'''


def analisis_test(test):
    aprobado, porcentaje = aprobados(test)

    print("La nota media del test es: " + str(round(nota_media(test), 2)))
    print("El test se ha finalizado " + str(participacion(test)) + " veces")
    print("El test se ha aprobado " + str(aprobado) + " veces")
    print("El porcentaje de aprobados es del " + str(round(porcentaje, 2)) + "%")


'''
def participacion(pruebas): Función encargada de calcular el número de veces que se ha completado un test.
- Argumentos:
  - pruebas: Conjunto de pruebas realizadas para un determinado tema.
- Resultado: Número de veces que se ha completado un test.
'''


def participacion(pruebas):
    contador = 0
    for pr in pruebas:
        if pr.estado == "Finalizado":
            contador += 1

    return contador


'''
def aprobados(pruebas): Función encargada de calcular el número de veces que se ha aprobado un test y el porcentaje de 
aprobados respecto al número de veces que se ha realizado.
- Argumentos:
  - pruebas: Conjunto de pruebas realizadas para un determinado tema.
- Resultado:
  - aprobado: Número de veces que los estudiantes han aprobado el test.
  - % aprobados: Porcentaje de aprobados con respecto al número de veces que se ha realizado el test.
'''


def aprobados(pruebas):
    contador = 0
    aprobado = 0
    for pr in pruebas:
        if pr.estado == "Finalizado":
            contador += 1
            if float(pr.calificacion_total.replace(",", ".")) >= 5.0:
                aprobado += 1

    if contador == 0:
        return aprobado, 0
    else:
        return aprobado, round(aprobado * 100 / contador, 2)


'''
def ranking_test(diccionario, s_fechas, fechas, opcion): Función encargada de ordenar los temas de mejores a peores para
 una serie de valores.
- Argumentos:
  - diccionario: Diccionario que contiene los tests realizados por los estudiantes para cada uno de los temas 
  (la clave son los temas de los test y su valor un array con los test realizados por los estudiantes).
  - s_fechas: Intervalos de fechas seleccionados para los cuales se quiere obtener los resultados. 
  - fechas: Array con los intervalos de fechas.
  - opcion: Opción para el valor para el cual se quiere realizar el ranking (Nota media de los test, número de veces 
  que se ha completado el test, número de veces que se a aprobado el test y porcentaje de aprobados).
'''


def ranking_test(diccionario, s_fechas, fechas, opcion):
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
        temas = []
        print("-----------------------------------------------------------------------------")
        print(str(f[0]).split(' ')[0] + " - " + str(f[1]).split(' ')[0])
        for t in diccionario.keys():
            pruebas = []
            for p in diccionario[t]:
                if f[0] <= p.fecha <= f[1]:
                    pruebas.append(p)
            temas.append(pruebas)

        if opcion == "Nota Media":
            print("-----------------------------------------------------------------------------")
            print("NOTA MEDIA")
            print("-----------------------------------------------------------------------------")
            temas.sort(key=lambda x: nota_media(x), reverse=True)
            for t in temas:
                if len(t) > 0:
                    print("Tema: " + t[0].tema + ". Nota media: " + str(round(nota_media(t), 2)))
        elif opcion == "Participacion":
            print("-----------------------------------------------------------------------------")
            print("PARTICIPACIÓN DE LOS ALUMNOS")
            print("-----------------------------------------------------------------------------")
            temas.sort(key=lambda x: participacion(x), reverse=True)
            for t in temas:
                if len(t) > 0:
                    print("Tema: " + t[0].tema + ". Veces que se ha realizado el test: " + str(participacion(t)))
        elif opcion == "Aprobados":
            print("-----------------------------------------------------------------------------")
            print("TEST APROBADOS")
            print("-----------------------------------------------------------------------------")
            temas.sort(key=lambda x: aprobados(x)[0], reverse=True)
            for t in temas:
                if len(t) > 0:
                    n_aprobados, porcentaje = aprobados(t)
                    print("Tema: " + t[0].tema + ". Veces que se ha aprobado el test: " + str(round(n_aprobados, 2)))
        elif opcion == "% Aprobados":
            print("-----------------------------------------------------------------------------")
            print("PORCENTAJE DE APROBADOS")
            print("-----------------------------------------------------------------------------")
            temas.sort(key=lambda x: aprobados(x)[1], reverse=True)
            for t in temas:
                if len(t) > 0:
                    n_aprobados, porcentaje = aprobados(t)
                    print("Tema: " + t[0].tema + ". Veces que se ha realizado el test: " + str(participacion(t)))
                    print("Tema: " + t[0].tema + ". Veces que se ha aprobado el test: " + str(round(n_aprobados, 2)))
                    print("Tema: " + t[0].tema + ". Porcentaje de aprobados: " + str(round(porcentaje, 2)) + "%")


'''
Resultados_estudiante(identificador, estudiantes, temas, s_fechas, fechas, opcion): Función encargada de analizar los test 
realizados por un estudiante.
  - Argumentos:
      - identificador: Identificador del estudiante.
      - estudiantes: Diccionario con los estudiantes y sus test realizados. La clave del diccionario es el identificador 
      del estudiante y para cada clave su valor es un diccionario con los test. Este segundo diccionario tiene como 
      clave el tema al que pertenecen los test y para cada clave su valor es un array que contiene los test realizados 
      por los estudiantes.
      - temas: Temas seleccionados para los que se quiere obtener los resultados.
      - s_fechas: Intervalos de fechas seleccionados para los cuales se quiere obtener los resultados. 
      - fechas: Array con los intervalos de fechas.
      - opcion: Opción para el tipo de análisis que queremos realizar sobre los test realizados por el estudiante 
      
      (Evolución para cada uno de los temas para una serie de intervalos de fechas o comparativa de una serie de temas 
      para una serie de intervalos de fechas)
'''


def Resultados_estudiante(identificador, estudiantes, temas, s_fechas, fechas, opcion):
    finalizado = 0
    aprobado = 0
    porcentaje = 0

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
        print("-----------------------------------------------------------------------------")
        print("ESTUDIANTE: " + e)
        print("-----------------------------------------------------------------------------")

        pruebas = estudiantes[e].pruebas

        if opcion == "Fechas x Temas":

            if temas[0] == "Todos":
                temas = []
                for t in pruebas:
                    temas.append(t)

            for t in temas:

                print("-----------------------------------------------------------------------------")
                print("Tema: " + str(t))
                print("-----------------------------------------------------------------------------")

                for f in fechas:

                    print(str(f[0]).split(' ')[0] + " - " + str(f[1]).split(' ')[0])
                    print("-----------------------------------------------------------------------------")
                    prs = []
                    if t in pruebas:
                        for p in pruebas[t]:
                            if f[0] <= p.fecha <= f[1]:
                                prs.append(p)

                        finalizado = participacion(prs)
                        aprobado, porcentaje = aprobados(prs)

                    print("El estudiante ha finalizado un total de " + str(finalizado) + " test")
                    print("El estudiante ha aprobado un total de " + str(aprobado) + " test")
                    print("La nota media del estudiante es de " + str(round(nota_media(prs), 2)))
                    print("El el porcentaje de aprobados del estudiante es " + str(porcentaje))

        elif opcion == "Temas x Fechas":

            for f in fechas:
                print("-----------------------------------------------------------------------------")
                print(str(f[0]).split(' ')[0] + " - " + str(f[1]).split(' ')[0])

                for t in pruebas:
                    print("-----------------------------------------------------------------------------")
                    print("Tema: " + str(t))
                    print("-----------------------------------------------------------------------------")
                    prs = []
                    if t in pruebas:
                        for p in pruebas[t]:
                            if f[0] <= p.fecha <= f[1]:
                                prs.append(p)

                        finalizado = participacion(prs)
                        aprobado, porcentaje = aprobados(prs)

                        print("El estudiante ha finalizado un total de " + str(finalizado) + " test")
                        print("El estudiante ha aprobado un total de " + str(aprobado) + " test")
                        print("La nota media del estudiante es de " + str(round(nota_media(prs), 2)))
                        print("El el porcentaje de aprobados del estudiante es " + str(porcentaje))


'''
def ranking_test_estudiante(identificador, estudiantes, s_fechas, fechas, opcion): Función encargada de ordenar los 
temas para una serie de valores en ciertos intervalos de tiempo para los estudiantes.
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
'''


def ranking_test_estudiante(identificador, estudiantes, s_fechas, fechas, opcion):
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
        print("PARTICIPACIÓN DE LOS ALUMNOS")

    elif opcion == "Aprobados":
        print("-----------------------------------------------------------------------------")
        print("TEST APROBADOS")

    elif opcion == "% Aprobados":
        print("-----------------------------------------------------------------------------")
        print("PORCENTAJE DE APROBADOS")

    for e in estudiantes:

        print("-----------------------------------------------------------------------------")
        print("ESTUDIANTE: " + e)

        for f in fechas:
            temas = []
            print("-----------------------------------------------------------------------------")
            print(str(f[0]).split(' ')[0] + " - " + str(f[1]).split(' ')[0])
            print("-----------------------------------------------------------------------------")

            for t in estudiantes[e].pruebas:
                prs = []
                for p in estudiantes[e].pruebas[t]:
                    if f[0] <= p.fecha <= f[1]:
                        prs.append(p)
                temas.append(prs)

            if opcion == "Nota Media":

                temas.sort(key=lambda x: nota_media(x), reverse=True)
                for t in temas:
                    if len(t) > 0:
                        print("Tema: " + t[0].tema + ". Nota media: " + str(round(nota_media(t), 2)))
            elif opcion == "Participacion":

                temas.sort(key=lambda x: participacion(x), reverse=True)
                for t in temas:
                    if len(t) > 0:
                        print("Tema: " + t[0].tema + ". Veces que se ha realizado el test: " + str(participacion(t)))
            elif opcion == "Aprobados":

                temas.sort(key=lambda x: aprobados(x)[0], reverse=True)
                for t in temas:
                    if len(t) > 0:
                        n_aprobados, porcentaje = aprobados(t)
                        print(
                            "Tema: " + t[0].tema + ". Veces que se ha aprobado el test: " + str(round(n_aprobados, 2)))
            elif opcion == "% Aprobados":

                temas.sort(key=lambda x: aprobados(x)[1], reverse=True)
                for t in temas:
                    if len(t) > 0:
                        n_aprobados, porcentaje = aprobados(t)
                        print("Tema: " + t[0].tema + ". Porcentaje de aprobados: " + str(round(porcentaje, 2)) + "%")


'''
def ranking_estudiantes(estudiantes, s_temas, temas, s_fechas, fechas, opcion): Función encargada de 
ordenar a los estudiantes de mejores a peores para una serie de valores en ciertos intervalos de tiempo.

- Argumentos:
  - estudiantes: Diccionario con los estudiantes y sus test realizados. La clave del diccionario es el identificador del 
    estudiante y para cada clave su valor es un diccionario con los test. Este segundo diccionario tiene como clave el 
    tema al que pertenecen los test y para cada clave su valor es un array que contiene los test realizados por los 
    estudiantes.
  - s_temas: Temas seleccionados para los cuales se quiere obtener los resultados.
  - temas: Temas seleccionados para los que se quiere obtener los resultados.
  - s_fechas: Intervalos de fechas seleccionados para los cuales se quiere obtener los resultados. 
  - fechas: Array con los intervalos de fechas.
  - opcion: Opción para el valor para el cual se quiere realizar el ranking (Nota media de los test, número de veces que 
    se ha completado el test, número de veces que se a aprobado el test y porcentaje de aprobados).
'''


def ranking_estudiantes(estudiantes, s_temas, temas, s_fechas, fechas, opcion):
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

    if opcion == "Nota Media":

        print("NOTA MEDIA")
    elif opcion == "Participacion":

        print("PARTICIPACIÓN DE LOS ALUMNOS")

    elif opcion == "Aprobados":

        print("TEST APROBADOS")

    elif opcion == "% Aprobados":

        print("PORCENTAJE DE APROBADOS")

    for f in fechas:

        print("-----------------------------------------------------------------------------")
        print(str(f[0]).split(' ')[0] + " - " + str(f[1]).split(' ')[0])

        for t in temas:

            print("-----------------------------------------------------------------------------")
            print("Tema: " + str(t))
            print("-----------------------------------------------------------------------------")

            estd = []

            for e in estudiantes:

                prs = []
                if t in estudiantes[e].pruebas:
                    for p in estudiantes[e].pruebas[t]:
                        if f[0] <= p.fecha <= f[1]:
                            prs.append(p)

                    estudiantes[e].paux = prs
                    if len(prs) > 1:
                        estd.append(e)

            if opcion == "Nota Media":

                estd.sort(key=lambda x: nota_media(estudiantes[x].paux), reverse=True)  # .reverse()
                for e in estd:
                    print("Estudiante: " + e + ". Nota media: " + str(round(nota_media(estudiantes[e].paux), 2)))

            elif opcion == "Participacion":

                estd.sort(key=lambda x: participacion(estudiantes[x].paux), reverse=True)
                for e in estd:
                    print("Estudiante: " + e + ". Veces que se ha realizado el test: " + str(
                        participacion(estudiantes[e].paux)))

            elif opcion == "Aprobados":

                estd.sort(key=lambda x: aprobados(estudiantes[x].paux)[0], reverse=True)
                for e in estd:
                    n_aprobados, porcentaje = aprobados(estudiantes[e].paux)
                    print("Estudiante: " + e + ". Veces que se ha aprobado el test: " + str(round(n_aprobados, 2)))

            elif opcion == "% Aprobados":

                estd.sort(key=lambda x: aprobados(estudiantes[x].paux)[1], reverse=True)
                for e in estd:
                    n_aprobados, porcentaje = aprobados(estudiantes[e].paux)
                    print("Estudiante: " + e + ". Porcentaje de aprobados: " + str(round(porcentaje, 2)))
