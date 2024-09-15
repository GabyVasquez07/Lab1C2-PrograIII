"""
Construir un programa que muestre una ventana a traves de la cual se pueda leer su numero de cedula
y su nombre completo
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
        self.nombre= QLabel("Ingresa tu nombre completo:")
        self.entrada = QLineEdit()
        self.DUI =QLabel("Ingresa tu numero de DUI:")
        self.entrada2=QLineEdit()
        boton = QPushButton("Haz click aqui")
        boton.clicked.connect(self.mostrar_mensaje)  # Conectar el botón al método para mostrar la clave
        layout.addWidget(self.nombre)
        layout.addWidget(self.entrada)
        layout.addWidget(self.DUI)
        layout.addWidget(self.entrada2)
        layout.addWidget(boton)
        central.setLayout(layout)
        self.setCentralWidget(central)

    def mostrar_mensaje(self):
        pass
        
app = QApplication(sys.argv)
ventana = ventanap()
ventana.show()
app.exec()