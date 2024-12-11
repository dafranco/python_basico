class InvalidMoveError(Exception):
    """Excepción personalizada para movimientos inválidos en el juego de Ta Te Ti."""
    def __init__(self, message="Movimiento inválido. Intenta nuevamente."):
        self.message = message
        super().__init__(self.message)
