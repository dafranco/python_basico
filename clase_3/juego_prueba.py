
lista = []
for i in range(3):
  lista.append(['x','x','x'])

print('Bienvenido al juego de TateTi')
columna = input('Jugador 1 - Ingrese movimiento columna: ')
fila = input('Jugador 1 - Ingrese movimiento fila: ')
try:
  print(lista[int(columna)][int(fila)])
except IndexError:
  print('Tené cuidado con los índices. Utilizá números del 0 al 2')