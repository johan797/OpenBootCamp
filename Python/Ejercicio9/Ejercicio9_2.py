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

suma = reduce(lambda x, y: x + y, list(filtro))
print(f"la suma es {suma}")