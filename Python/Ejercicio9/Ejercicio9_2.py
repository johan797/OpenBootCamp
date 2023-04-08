"""En este segundo ejercicio, tenéis que crear una aplicaci
 parámetro con filter y realizará una suma de todos estos 
 elementos obtenidos mediante reduce."""
from functools import reduce
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def filtrado(num):
    if num % 2 == 0:
        return True
    return False

filtro = filter(filtrado, lista_numeros)
"""En Python, un objeto iterable se agota cuando se ha recorrido
 completamente y no se puede volver a iterar sobre él. Esto se debe
   a que los objetos iterables sólo tienen un elemento siguiente al 
   que se puede acceder si su valor no es igual a None1. Si intenta 
   iterar sobre un objeto None, encontrará el TypeError: “NoneType” 
   el objeto no es iterable error1.

Si desea volver a iterar sobre un objeto iterable en Python, debe
 crear una nueva instancia del objeto iterable o convertirlo en 
 una lista o tupla"""
suma = reduce(lambda x, y: x + y, list(filtro))
print(f"la suma es {suma}")