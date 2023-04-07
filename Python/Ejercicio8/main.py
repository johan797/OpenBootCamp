"""
numero = 511
texto = "quijote"
flotante =1.2

#primera forma version vieja de formateo de una cadena, la peor
#print("el numero es %d y el texto es %s y tiene %f"%(numero,texto,flotante))
#print ("valor flotante %.2f" %flotante)

#segunda forma
print("el numero es {} y el texto es {} y tiene {}"
      .format(numero, texto, flotante))
print("el numero es {n1} y el texto es {txt} y tiene {ft}"
      .format(n1 =numero, txt= texto, ft =flotante))

# tercera forma
print(f'el numero es {numero} y el texto es { texto.upper() } y tiene {flotante}' )
""" 
# representaciones textuales de una clase
class juguete:
    nombre = ""
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
#str para salida informales y repr para salidas tecnicas codigo en depuracion
    def __str__(self):
        return f'Mi nombre es {self.nombre} y mi precio {self.precio}'
    
#With method overloading, multiple methods can have the same name with different parameters:
j1 = juguete("potato", 10.5)
print(j1)

"""Metodos en una cadena de texto
title() capitaliza las primeras letras
count() cuenta la existencia de un caracter
isdigit() saber si un caracter es numero
isalfha() si la cadena tiene solo letras
strip() elimina espacios al principio de la cadena
split() converte una cadena a una lista separa segun lo que se mete dentro del parentesis
endswith()"""

co