class Puerta:
    def __init__(self):
        """
        Inicializa la puerta en estado cerrada.
        """
        self.abierta = False

    def abrir(self):
        """
        Cambia el estado de la puerta a abierta si está cerrada.
        """
        if not self.abierta:
            self.abierta = True

    def cerrar(self):
        """
        Cambia el estado de la puerta a cerrada si está abierta.
        """
        if self.abierta:
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


# Instanciar la clase (crear una puerta)
mi_puerta = Puerta()

# Enviar mensajes a la puerta y usar imprimir_estado
mi_puerta.imprimir_estado()  # Estado inicial
mi_puerta.abrir()
mi_puerta.imprimir_estado()  # Estado tras abrir
mi_puerta.cerrar()
mi_puerta.imprimir_estado()  # Estado tras cerrar