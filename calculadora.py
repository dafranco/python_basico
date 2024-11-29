#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculadora')
        self.setGeometry(100, 100, 300, 400)

        # Layout vertical principal
        self.layout = QVBoxLayout()

        # Pantalla de entrada
        self.pantalla = QLineEdit(self)
        self.pantalla.setAlignment(Qt.AlignRight)
        self.layout.addWidget(self.pantalla)

        # Layout horizontal para los botones
        self.botones_layout = QVBoxLayout()

        # Definir botones
        self.botones = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"]
        ]

        for fila in self.botones:
            fila_layout = QHBoxLayout()
            for boton in fila:
                boton_obj = QPushButton(boton, self)
                boton_obj.clicked.connect(self.on_click)
                fila_layout.addWidget(boton_obj)
            self.botones_layout.addLayout(fila_layout)

        self.layout.addLayout(self.botones_layout)

        self.setLayout(self.layout)

    def on_click(self):
        boton = self.sender().text()
        if boton == "=":
            try:
                resultado = eval(self.pantalla.text())
                self.pantalla.setText(str(resultado))
            except Exception as e:
                self.pantalla.setText("Error")
        elif boton == "C":
            self.pantalla.clear()
        else:
            self.pantalla.setText(self.pantalla.text() + boton)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculadora = Calculadora()
    calculadora.show()
    sys.exit(app.exec_())