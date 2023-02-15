
peso = input("Escriba su peso en kg: ")
estatura = input ("Escriba su estatura en metros: " )
print(type(peso))
print(type(estatura))
peso=int(peso)
estatura= float(estatura)
epow=(estatura**2)
IndiceMasa = peso/epow
#redondeando con round
print(" Tu indice de masa corporal es: ", round(IndiceMasa, 2))
#redondeando con fstrings
print(" Tu indice de masa corporal es: ",f'{IndiceMasa:.2f}')
print(" Tu indice de masa corporal es: ","%.2f" % (IndiceMasa))
