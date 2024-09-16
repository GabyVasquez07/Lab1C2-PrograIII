import sys
from PyQt5 import uic, QtWidgets
#Primero importamos los paquetes a utilizar, en este caso, sys, PyQt5 incluyendo la uic y el QtWidgets
class VentanaMascotas(QtWidgets.QMainWindow):#Creamos la clase para las mascotas
    def __init__(self):
        super().__init__()
        uic.loadUi("uiventana5.ui", self) #Cargamos la interface uiventana5.ui a partir del método loadUi
        self.boton_guardar.clicked.connect(self.guardar_datos)
        #guardamos los datos a través del botón creado en la interfaz gráfica
    def guardar_datos(self):#creamos el método para guardar los datos
        mascota1_nombre = self.mascota1_nombre.text()
        mascota1_edad = self.mascota1_edad.text()
        mascota1_tipo = self.mascota1_tipo.text()
#Correlacionamos las variables con los nombres de los objetos en el designer
        mascota2_nombre = self.mascota2_nombre.text()
        mascota2_edad = self.mascota2_edad.text()
        mascota2_tipo = self.mascota2_tipo.text()

        mascota3_nombre = self.mascota3_nombre.text()
        mascota3_edad = self.mascota3_edad.text()
        mascota3_tipo = self.mascota3_tipo.text()
        #Imprimimos los datos que ha ingresado el usuario
        print("\nBienvenido\nEstos son los datos que usted ha ingresado:")
        print("---------------------------------------------------------------------------------------------------------")
        print("Estos son los datos de las mascotas: ")
        print(f"Mascota 1: Nombre: {mascota1_nombre}, Edad: {mascota1_edad}, Tipo de animal: {mascota1_tipo}")
        print(f"Mascota 2: Nombre: {mascota2_nombre}, Edad: {mascota2_edad}, Tipo de animal: {mascota2_tipo}")
        print(f"Mascota 3: Nombre: {mascota3_nombre}, Edad: {mascota3_edad}, Tipo de animal: {mascota3_tipo}")
        print("---------------------------------------------------------------------------------------------------------")

app = QtWidgets.QApplication([])
ventana = VentanaMascotas()#Creamos la intancia para llamar la clase y usamos el método show para mostrar la ventana
ventana.show()
sys.exit(app.exec_())
