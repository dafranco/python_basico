import csv

# Función para leer el archivo CSV y devolver la lista de tuplas
def leer_alumnos_csv(nombre_archivo):
    alumnos = []
    with open(nombre_archivo, newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        next(lector)  # Omitir la fila de encabezado
        for fila in lector:
            nombre, edad, grado, promedio = fila
            # Convertir los datos numéricos y formar una tupla
            alumno = (nombre, int(edad), int(grado), float(promedio))
            alumnos.append(alumno)
    return alumnos

# Leer los datos del archivo
alumnos = leer_alumnos_csv('alumnos.csv')

# Imprimir la lista de tuplas
for alumno in alumnos:
    print(alumno)