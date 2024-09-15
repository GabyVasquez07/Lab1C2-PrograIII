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
         # Etiqueta y campo de entrada para el nombre
        self.nombre = QLabel("Ingresa tu nombre completo:")
        self.entrada_N = QLineEdit()
        # Etiqueta y campo de entrada para el número de DUI
        self.DUI = QLabel("Ingresa tu número de DUI:")
        self.entrada_D = QLineEdit()
        boton = QPushButton("Subir información")
        boton.clicked.connect(self.mostrar_mensaje)  # Conectar el botón al método para mostrar la clave
        layout.addWidget(self.nombre)
        layout.addWidget(self.entrada_N)
        layout.addWidget(self.DUI)
        layout.addWidget(self.entrada_D)
        layout.addWidget(boton)
        central.setLayout(layout)
        self.setCentralWidget(central)

    def mostrar_mensaje(self):
        #Obtener los valores del nombre y el dui
        nombre = self.entrada_N.text()
        dui = self.entrada_D.text()
         # Verificar si ambos campos tienen datos
        if not nombre or not dui:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingrese todos los datos.")
        else:
            # Mostrar los datos ingresados en un cuadro de diálogo
            QMessageBox.information(self, "Datos Ingresados",
                                    f"Nombre: {nombre}\nDUI: {dui}")
        
app = QApplication(sys.argv)
ventana = ventanap()
ventana.show()
app.exec()