class Puerta:
    def __init__(self, esta_abierta):
        """
        Inicializa la puerta en estado cerrada.
        """
        self.abierta = esta_abierta

    def abrir(self):
        """
        Cambia el estado de la puerta a abierta
        """
        self.abierta = True
        self.color = 'azul'

    def cerrar(self):
        """
        Cambia el estado de la puerta a cerrada
        """
        self.abierta = False

    def estado(self):
        """
        Retorna el estado actual de la puerta (True para abierta, False para cerrada).
        """
        return self.abierta

    def imprimir_estado(self):
        """
        Imprime el estado actual de la puerta en texto legible.
        """
        print("La puerta está abierta." if self.abierta else "La puerta está cerrada.")
        print(self.color)

def cuadrado(numero):
  return numero * numero

print(type(cuadrado))
# Instanciar la clase (crear una puerta)
mi_puerta = Puerta(True)
otra_puerta = Puerta(False)

# Enviar mensajes a la puerta y usar imprimir_estado
#mi_puerta.imprimir_estado()  # Estado inicial
mi_puerta.abrir()
#mi_puerta.imprimir_estado()  # Estado tras abrir
mi_puerta.cerrar()
mi_puerta.imprimir_estado()  # Estado tras cerrar