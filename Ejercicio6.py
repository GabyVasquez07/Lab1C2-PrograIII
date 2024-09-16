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
       # Obtener los valores de peso y altura
        peso = self.peso_spinbox.value()
        altura = self.altura_spinbox.value()

        # Obtener la unidad de medida seleccionada (metros o pies)
        unidad = self.unidad_combobox.currentText()

        # Si la altura está en pies, convertirla a metros (1 pie = 0.3048 metros)
        if unidad == "Pies":
            altura = altura * 0.3048

        # Calcular el IMC
        imc = peso / (altura ** 2)

        # Determinar la categoría del IMC según los estándares de la OMS
        if imc < 18.5:
            categoria = "Bajo peso"
        elif 18.5 <= imc < 24.9:
            categoria = "Peso normal"
        elif 25.0 <= imc < 29.9:
            categoria = "Sobrepeso"
        else:
            categoria = "Obesidad"

        # Determinar el mensaje según el sexo seleccionado
        if self.radio_hombre.isChecked():
            mensaje_adicional = "Recuerda hacer ejercicio regularmente, ¡cuida tu salud!"
        elif self.radio_mujer.isChecked():
            mensaje_adicional = "Mantén una dieta balanceada y ejercicio para mantenerte en forma."
        else:
            mensaje_adicional = ""

        # Mostrar el IMC calculado, la categoría y el mensaje adicional
        QMessageBox.information(self, "Resultado del IMC", 
                                f"Su IMC es: {imc:.2f}\nCategoría: {categoria}\n\n{mensaje_adicional}")
# Crear la aplicación y mostrar la ventana
app = QApplication(sys.argv)
ventana = IMCCalculator()
ventana.show()
app.exec()