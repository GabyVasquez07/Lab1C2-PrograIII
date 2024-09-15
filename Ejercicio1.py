"""
Construir un programa que muestre una ventana en la cual aparezca su nombre completo y su edad centrados.
"""
import sys
from PyQt5.QtWidgets import (QMainWindow,QApplication,QLabel,
                            QWidget,QVBoxLayout)
from PyQt5 import QtWidgets,uic
from PyQt5.QtCore import Qt

class ventanap(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.resize(400,400)
        self.setWindowTitle('Ejercicio 1')
        layout= QVBoxLayout()
        central=QWidget(self)
        self.nombre= QLabel("Nombre: Gabriela Estefani Vasquez Hidalgo")
        self.edad= QLabel("Edad: 20 años")
         #Centrar el texto en las etiquetas
        self.nombre.setAlignment(Qt.AlignCenter)
        self.edad.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.nombre)
        layout.addWidget(self.edad)
        self.nombre.setStyleSheet("QLabel { font-size: 24px; }")  # Texto más grande para el nombre
        self.edad.setStyleSheet("QLabel { font-size: 20px; }")   # Texto más grande para la edad
        central.setLayout(layout)
        self.setCentralWidget(central)
        
app = QApplication(sys.argv)
ventana = ventanap()
ventana.show()
app.exec()