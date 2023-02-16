def bisiesto(anio):

    if anio % 4 != 0:
        return False
    elif anio % 100 !=0:
        return True
    elif anio % 400 !=0:
        return False
    else:
        return True
        
anio = input("Escriba un año: ")
anio = int(anio)
if bisiesto(anio):
    print('el año ', anio, 'es bisiesto')
else:
    print('el año ', anio, ' no es bisiesto' )
