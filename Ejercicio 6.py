"""
Calculadora de IMC
El programa calcula el IMC de una persona en base a su peso (en kilogramos) y altura (en metros).
Luego, interpreta el resultado según las categorías estándar de la Organización Mundial de la Salud (OMS),
que clasifica el IMC en varios rangos como bajo peso, normal, sobrepeso y obesidad. Es una herramienta 
sencilla para monitorear la salud física.
El usuario ingresa su peso y su altura, seleccionando si la altura está en metros o pies mediante un ComboBox.
 Además, elige si es hombre o mujer con un RadioButton. El programa convierte la altura a metros 
 (si es necesario), calcula el IMC y muestra la categoría según los estándares de la OMS, 
 junto con un mensaje personalizado para hombres o mujeres.
"""
import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, 
                             QWidget, QVBoxLayout, QSpinBox, QDoubleSpinBox, 
                             QPushButton, QMessageBox, QComboBox, QRadioButton, QHBoxLayout)


class IMCCalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(400, 300)
        self.setWindowTitle('Ejercicio 6')

        layout = QVBoxLayout()
        central_widget = QWidget(self)

        # Etiqueta y SpinBox para el peso
        self.label_peso = QLabel("Ingrese su peso (kg):")
        self.peso_spinbox = QSpinBox()
        self.peso_spinbox.setRange(30, 300)  # Rango de peso válido
        self.peso_spinbox.setValue(70)  # Valor inicial

        # Etiqueta y DoubleSpinBox para la altura
        self.label_altura = QLabel("Ingrese su altura:")
        self.altura_spinbox = QDoubleSpinBox()
        self.altura_spinbox.setRange(0.50, 8.00)  # Rango de altura válido
        self.altura_spinbox.setSingleStep(0.01)  # Paso de 1 cm
        self.altura_spinbox.setValue(1.75)  # Valor inicial

        # ComboBox para seleccionar la unidad de medida (metros o pies)
        self.label_unidad = QLabel("Seleccione la unidad de medida:")
        self.unidad_combobox = QComboBox()
        self.unidad_combobox.addItems(["Metros", "Pies"])

        # RadioButton para seleccionar el sexo (Hombre o Mujer)
        self.label_sexo = QLabel("Seleccione su sexo:")
        self.radio_hombre = QRadioButton("Hombre")
        self.radio_mujer = QRadioButton("Mujer")

        # Agrupamos los RadioButtons en un layout horizontal
        sexo_layout = QHBoxLayout()
        sexo_layout.addWidget(self.radio_hombre)
        sexo_layout.addWidget(self.radio_mujer)

        # Botón para calcular el IMC
        self.boton_calcular = QPushButton("Calcular IMC")
        self.boton_calcular.clicked.connect(self.calcular_imc)

        # Añadir los widgets al layout
        layout.addWidget(self.label_peso)
        layout.addWidget(self.peso_spinbox)
        layout.addWidget(self.label_altura)
        layout.addWidget(self.altura_spinbox)
        layout.addWidget(self.label_unidad)
        layout.addWidget(self.unidad_combobox)
        layout.addWidget(self.label_sexo)
        layout.addLayout(sexo_layout)
        layout.addWidget(self.boton_calcular)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def calcular_imc(self):
       pass

# Crear la aplicación y mostrar la ventana
app = QApplication(sys.argv)
ventana = IMCCalculator()
ventana.show()
app.exec()
