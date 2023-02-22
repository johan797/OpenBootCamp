#En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
#Color
#Ruedas
#Puertas
#Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
#Velocidad
#Cilindrada
# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class vehiculo:
  def __init__(self, color, ruedas, puertas):

    self.color = color
    self.ruedas =  ruedas
    self.puertas = puertas
  def printFeatures(self):
    print('tu vehiculo tiene las siguientes caracteristicas', self.color, self.ruedas, self.puertas)
          
    

class coche(vehiculo):
  def __init__(self, color, ruedas, puertas,velocidad, cilindrada):
    super().__init__(color, ruedas, puertas)
    self.velocidad= velocidad
    self.cilindrada =cilindrada

  def othersFeatures(self):
    print('tu vehiculo tambien tiene las siguientes caracteriticas',"COLOR: ",self.color,"RUEDAS: ",
          self.ruedas,"PUERTAS: ", self.puertas,"VELOCIDAD: ", self.velocidad,"CILINDRADA: ", self.cilindrada)

bmw = coche("rojo", 27, "2", "100Km/h", "2000cc")

bmw.othersFeatures()


