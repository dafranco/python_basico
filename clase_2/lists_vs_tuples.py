alumnos_lists = [
  ['David Franco', 'francodavid20@gmail.com', 'Abogacía'],
  ['Leonel Messi', 'messi.leonel@gmail.com', 'Profesorado de Educación física']
]
print('---Alumnos con lista---')
for alumno in alumnos_lists:
  nombre = alumno[0]
  email = alumno[1]
  carrera = alumno[2]
  print(nombre + ' ' + email + ' ' + carrera)

alumno_tuple = [
  ('David Franco', 'francodavid20@gmail.com', 'Abogacía'),
  ('Leonel Messi', 'messi.leonel@gmail.com', 'Profesorado de Educación física')
]

print('---Alumnos con tupla---')
for alumno in alumno_tuple:
  nombre, email, carrera = alumno
  print(nombre + ' ' + email + ' ' + carrera)