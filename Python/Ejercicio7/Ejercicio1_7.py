import modulo_operaciones

a = input("ingrese el primer numero: ")
a = float(a)
b = input("ingrese el segundo numero: ")
b = float(b)
print("La suma de", a, "y", b, "es:", modulo_operaciones.sumar(a, b))
print("La resta de", a, "y", b, "es:", modulo_operaciones.restar(a, b))
print("El producto de", a, "y", b, "es:", modulo_operaciones.multiplicar(a, b))
print("La division de", a, "y", b, "es:", modulo_operaciones.dividir(a, b))
