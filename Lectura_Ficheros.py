import csv
from datetime import datetime

from Clases import *

'''
def calcular_fecha(fecha): Función encargada de convertir la fecha proporciada por el fichero (string) en un objeto 
tipo datetime con formato %d/%m/%Y.
  - Argumentos:
      - fecha: Fecha en la que el test se ha realizado.
  - Resultado: Objeto de tipo datetime que con la fecha en formato %d/%m/%Y.
'''


def calcular_fecha(fecha):
    dia = fecha.split(" ")[0]
    m = fecha.split(" ")[2]
    ano = fecha.split(" ")[4]
    mes = ""

    if m == "enero":
        mes = "01"
    elif m == "febrero":
        mes = "02"
    elif m == "marzo":
        mes = "03"
    elif m == "abril":
        mes = "04"
    elif m == "mayo":
        mes = "05"
    elif m == "junio":
        mes = "06"
    elif m == "julio":
        mes = "07"
    elif m == "agosto":
        mes = "08"
    elif m == "septiembre":
        mes = "09"
    elif m == "octubre":
        mes = "10"
    elif m == "noviembre":
        mes = "11"
    elif m == "diciempre":
        mes = "12"

    return datetime.strptime(dia + '/' + mes + '/' + ano, '%d/%m/%Y')


'''
  def leer(fila): Función encargada de procesar la información de cada una de las líneas del fichero.
  - Argumentos:
      - fila: Array con cada uno de los campos de las líneas del fichero.
  - Resultado: La función devuelve un objeto Prueba con la información leída del fichero.
'''


def leer(fila, tema):
    identificador = fila[1]
    estado = fila[2]
    fecha = calcular_fecha(fila[3].split("  ")[0])
    calificacion_total = fila[6]

    t = Prueba(identificador, tema, estado, fecha, calificacion_total)

    return t


'''
def leer_fichero_test(nombre_archivo): Función encargada de abrir y leer el contenido del fichero.
  - Argumentos:
      - nombre_archivo: Nombre del archivo.
  - Resultado: La función devuelve un array con los objetos de tipo prueba obtenidos a partir de la información del 
  fichero.
'''


'''def leer_fichero_test(nombre_archivo, tema):
    try:
        with open(nombre_archivo, "r") as archivo:
            tests = []

            lector = csv.reader(archivo, delimiter=",")
            next(lector, None)
            for fila in lector:
                tests.append(leer(fila, tema))

            return tests

    except FileNotFoundError:
        return None'''


'''
def lectura_tema(archivo, diccionario_tema, tema): La función se encarga de leer el contenido del fichero y 
organizar los test realizados por los estudiantes por tema.
  - Argumento:
      - archivo: Nombre del archivo.
      - diccionario_tema: Diccionario con los test realizados.
      - tema: Tema de la asignatura al que corresponden los test.

  - Resultado: La función devuelve un diccionario con los test realizados por los estudiantes. La clave del diccionario 
  es el tema al que pertenecen los test y para cada clave su valor es un array que contiene un conjunto de arrays con 
  los test realizados por los estudiantes.
  
  (De esta forma podemos ver el rendimiento general del grupo en cada uno de los temas)
'''


def lectura_tema(archivo, diccionario_tema, tema):

    try:
        with open(archivo, "r") as archv:
            tests = []

            lector = csv.reader(archv, delimiter=",")
            next(lector, None)
            for fila in lector:
                tests.append(leer(fila, tema))
    except FileNotFoundError:
        return None
    else:
        if tema in diccionario_tema:
            if len(tests) != 0:
                for p in tests:
                    diccionario_tema[tema].append(p)
        else:
            diccionario_tema[tema] = []
            if len(tests) != 0:
                for p in tests:
                    diccionario_tema[tema].append(p)

        return diccionario_tema


'''
**lectura_fecha(archivo, diccionario_fecha, tema):** La función se encarga de leer el contenido del fichero y 
organizar los test realizados por los estudiantes por fecha.
  - Argumento:
      - archivo: Nombre del archivo.
      - diccionario_fecha: Diccionario con los test realizados.
      - tema: Tema de la asignatura al que corresponden los test.

  - Resultado: La función devuelve un diccionario con los test realizados por los estudiantes. La clave del diccionario 
  es la fecha en la que se realizó el test y para cada clave su valor es un array que contiene un conjunto de arrays con 
  los test de cada tema realizados por los estudiantes en dicha fecha.
  
  (De esta forma podemos ver el progreso de los estudiantes en cada uno de los temas para ciertos periodos de tiempo)
  '''


def lectura_fecha(archivo, diccionario_fecha, tema):
    try:
        with open(archivo, "r") as archivo:

            lector = csv.reader(archivo, delimiter=",")
            # Omitir el encabezado
            next(lector, None)
            for fila in lector:
                t = leer(fila, tema)

                fecha = t.fecha
                tema = t.tema

                if fecha in diccionario_fecha:
                    if tema in diccionario_fecha[fecha]:
                        diccionario_fecha[fecha][tema].append(t)
                    else:
                        diccionario_fecha[fecha][tema] = []
                    diccionario_fecha[fecha][tema].append(t)
                else:
                    diccionario_fecha[fecha] = {}
                    diccionario_fecha[fecha][tema] = []
                    diccionario_fecha[fecha][tema].append(t)

        return diccionario_fecha

    except FileNotFoundError:
        return None


'''
def test_por_alumno(nombre_archivo, estudiantes, tema): La función se encarga de leer el contenido del fichero y 
organizar los test realizados por los estudiantes por tema.
  - Argumento:
      - nombre_archivo: Nombre del archivo.
      - estudiantes: Diccionario con los estudiantes del grupo.
  - Resultado: La función devuelve un diccionario con los estudiantes y sus test realizados. La clave del diccionario 
  es el identificador del estudiante y para cada clave su valor es un diccionario con los test. Este segundo diccionario 
  tiene como clave el tema al que pertenecen los test y para cada clave su valor es un array que contiene los test 
  realizados por los estudiantes.
'''


def test_por_alumno(nombre_archivo, estudiantes, tema):

    tests = {}

    try:
        with open(nombre_archivo, "r") as archivo:
            lector = csv.reader(archivo, delimiter=",")

            next(lector, None)
            for fila in lector:
                t = leer(fila, tema)

                if t.identificador not in tests:
                    tests[t.identificador] = {}
                    if t.tema not in tests[t.identificador]:
                        tests[t.identificador][t.tema] = []
                        tests[t.identificador][t.tema].append(t)
                    else:
                        tests[t.identificador][t.tema].append(t)
                else:
                    if t.tema not in tests[t.identificador]:
                        tests[t.identificador][t.tema] = []
                        tests[t.identificador][t.tema].append(t)
                    else:
                        tests[t.identificador][t.tema].append(t)

            for id in tests.keys():
                if id not in estudiantes:
                    estudiante = Estudiante(id, {})
                    estudiantes[id] = estudiante
                    for t in tests[id].keys():
                        if t not in estudiantes[id].pruebas:
                            estudiantes[id].pruebas[t] = tests[id][t]
                        else:
                            estudiantes[id].pruebas[t].append(tests[id][t])
                else:
                    for t in tests[id].keys():
                        if t not in estudiantes[id].pruebas:
                            estudiantes[id].pruebas[t] = tests[id][t]
                        else:
                            estudiantes[id].pruebas[t].append(tests[id][t])

        return estudiantes

    except FileNotFoundError:
        return None


'''
def leer_registros(fila): Función encargada de procesar la información de cada una de las líneas del 
fichero.
  - Argumentos:
      - fila: Array con cada uno de los campos del fichero.

  - Resultado: La función devuelve un objeto Registro con la información leída del fichero.
'''


def leer_registros(fila):

    if len(fila) > 1:

        Fecha = datetime.strptime(fila[1].split()[0], '%d/%m/%Y')
        hora = datetime.strptime(fila[1].split()[1], '%H:%M')
        identificador = fila[2]
        contexto = fila[3]
        componente = fila[4]
        nombre_evento = fila[5]
        descripcion = fila[6]
        origen = fila[7]
        IP = fila[8]

        r = Registros(Fecha, hora, identificador, contexto, componente, nombre_evento, descripcion, origen, IP)

        return r


'''
def leer_registros(nombre_archivo, registros): Función encargada de abrir y leer el contenido del fichero.
  - Argumentos:
      - nombre_archivo: Nombre del archivo.
      - registros: Diccionario con los accesos semanales a Moodle de cada uno de los estudiantes.
  - Resultado: La función devuelve un diccionario. La clave del diccionario es el identificador del estudiante. 
  Para cada clave su valor es un array con objetos de tipo 'Registro' que contienen los accesos a Moodle del estudiante 
  para cada uno de los temas en una semana en concreto.
'''


def fichero_registros(nombre_archivo, registros):

    try:
        with open(nombre_archivo, "r") as archivo:
            lector = csv.reader(archivo, delimiter=",")
            # Omitir el encabezado
            next(lector, None)
            for fila in lector:
                r = leer_registros(fila)
                if len(fila) > 1:
                    if r.identificador not in registros:
                        registros[r.identificador] = []
                        registros[r.identificador].append(r)
                    else:
                        registros[r.identificador].append(r)

        return registros

    except FileNotFoundError:
        return None
