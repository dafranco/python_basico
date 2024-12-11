# Para utilizarlo en el interprete interactivo utilizar
# from clase_4.ejemplo_herencia import *

class Mamifero:
  def __init__(self):
    pass

  def comer(self, alimento):
    print(f'Estoy comiendo {alimento}')

  def respirar(self):
    print('Mi respiración es inconsciente')


class Perro(Mamifero):
  def __init__(self):
    pass

  def ladrar(self):
    print('Guau')

class Delfin(Mamifero):
  def comer(self, alimento):
    super().comer(alimento)
    print('Debo comer bajo el agua')

  def respirar(self):
    print('Debo respirar conscientemente cada 10 minutos')
