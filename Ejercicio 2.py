"""
Construir un programa que muestre una ventana y que lea una clave secreta sin mostrar 
los caracteres que la componen.
"""
import sys
from PyQt5.QtWidgets import (QMainWindow,QApplication,QLabel,
                            QWidget,QVBoxLayout,QLineEdit,QPushButton,QMessageBox)
from PyQt5 import QtWidgets,uic

class ventanap(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(300, 300)
        self.setWindowTitle('Ejercicio 3')
        layout= QVBoxLayout()
        central=QWidget(self)
        self.texto= QLabel("Ingresa la clave secreta")
        self.entrada = QLineEdit()
        self.entrada.setEchoMode(QLineEdit.Password)  # Modo de contraseña para ocultar los caracteres
        boton = QPushButton("Haz click aqui")
        boton.clicked.connect(self.mostrar_mensaje)  # Conectar el botón al método para mostrar la clave
        layout.addWidget(self.texto)
        layout.addWidget(self.entrada)
        layout.addWidget(boton)
        central.setLayout(layout)
        self.setCentralWidget(central)

    # Método para mostrar la clave secreta
    def mostrar_mensaje(self):
        QMessageBox.information(self, "Información", "Clave guardada con éxito")


app = QApplication(sys.argv)
ventana = ventanap()
ventana.show()
app.exec()