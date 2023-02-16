# Escribe un programa que sea
#capaz de mostrar los números del 1 al 100 en orden inverso.


#PRIMERA FORMA
i=100

while i >= 1:
  print(i, end=" ")
  i-=1
print(' \n')


#SEGUNDA FORMA

for x in range(100, 0, -1):
  print(x, end=" ")
print(' ')

