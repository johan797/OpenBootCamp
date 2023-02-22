class Dino:
    _encendido= False

    def apaga(self):
        self._encendido = False
        
    def enciende(self):
        self._encendido = True
        
    def isEncendido(self):
        return self._encendido

        
      
#instancia de clase Dino
d1 = Dino()


# en python todas las clases son public por lo tanto podemos modificar su
#propiedad encendido d.apaga= False
print(d1._encendido)
print(d1.isEncendido())
#cada instancia de clase tiene un espacio de memoria
d2 = Dino()
#el siguiente print bota none porque no se puede imprimir la llamada a una funcion
print(d2.apaga())
print(d2.isEncendido())

# las clases estatica no permiten instanciar solo tiene un solo espacio de memoria

#HERENCIA
