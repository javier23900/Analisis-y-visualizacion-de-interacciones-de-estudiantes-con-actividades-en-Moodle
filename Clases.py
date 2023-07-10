"""
CLASE PRUEBA

Recoge la información de cada uno de los test realizados por el alumno:

  - Identificador: Identificador del alumno.
  - Tema: Tema al que corresponde el test realizado.
  - Estado: Estado del test (finalizado o pendiente)
  - Fecha: Fecha en la que se realizó el test.
  - Calificación total: Nota obtenida por el alumno en el test.
  """


class Prueba:

    def __init__(self, identificador, tema, estado, fecha, calificacion_total):
        self.identificador = identificador
        self.tema = tema
        self.estado = estado
        self.fecha = fecha
        self.calificacion_total = calificacion_total


'''
CLASE ESTUDIANTE

Recoge la información de cada uno de los alumnos:

  - Identificador: Identificador del alumno.
  - Pruebas: Diccionario que recoge las pruebas realizadas por el estudiante.
'''


class Estudiante:

    def __init__(self, identificador, pruebas):
        self.identificador = identificador
        self.pruebas = pruebas
        self.paux = []


'''
CLASE REGISTROS

Recoge la información de los registros (accesos a Moodle) de los estudiantes.

- fecha: Fecha del acceso a Moodle.
- hora: Hora del acceso a Moodle.
- identificador: Identificador del alumno.
- contexto: Contexto del acceso a Moodle.
- componente: Componente del acceso a Moodle.
- nombre_evento: Nombre del evento.
- descripcion: Descripción del evento.
- origen: Forma de acceso a Moodle.
- IP: Dirección IP desde el que se accede a Moodle.
'''


class Registros:

    def __init__(self, fecha, hora, identificador, contexto, componente, nombre_evento, descripcion, origen, IP):
        self.fecha = fecha
        self.hora = hora
        self.identificador = identificador
        self.contexto = contexto
        self.componente = componente
        self.nombre_evento = nombre_evento
        self.descripcion = descripcion
        self.origen = origen
        self.IP = IP
