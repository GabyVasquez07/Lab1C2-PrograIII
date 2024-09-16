import sys
from PyQt5 import uic, QtWidgets
#Acá importamos los paquetes a utilizar, siendo estos sys, PyQt5, uic y QtWidgets
"""
Construir un programa que muestre una ventana a través de la cual se puedan leer 10 datos
característicos de una persona.
"""
class VentanaPersona(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana_persona3.ui", self)
        self.boton_guardar.clicked.connect(self.guardar_datos)
#Creamos la clase, y cargamos el archivo de la interfaz gráfica llamado "ventana_persona3.ui" en donde realizamos el diseño
    def guardar_datos(self):
        nombre = self.nombre.text() #Creamos el método para guardar los datos, tomando de referencia los nombres de los objetos en el designer
        edad = self.edad.text()
        sexo = self.sexo.text()
        altura = self.altura.text()
        peso = self.peso.text()
        tonopiel = self.tonopiel.text()
        colorojos = self.colorojos.text()
        colorcabello = self.colorcabello.text()
        tipocabello = self.tipocabello.text()
        complexion = self.complexion.text()
        print("\nBienvenido")
        print("\nEstos son los datos que usted ha ingresado:\n------------------ ")
        print(f"Nombre: {nombre},\nEdad: {edad},\nSexo: {sexo},\nAltura: {altura},\nPeso: {peso},\nTono de piel: {tonopiel},\nColor de ojos: {colorojos},\nColor de cabello: {colorcabello},\nTipo de Cabello: {tipocabello},\nComplexion: {complexion}")
        print("---------------------")
        # Imprimimos los datos que ha añadido el usuario

app = QtWidgets.QApplication([])
ventana = VentanaPersona() #Creamos la instancia para llamar la clase y su método, y finalmente utilizamos el método show para mostrar nuestra ventana
ventana.show()
sys.exit(app.exec_())

