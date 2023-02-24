import time

# Obtenemos la hora actual del sistema mediante la funcion localtime y
# su atributo tm_hour el cual nos da la hora del sistema
hora_actual = time.localtime().tm_hour

print(f"son las {hora_actual} horas")

# Verificamos si es más de las 7pm
if hora_actual >= 19:
    print("Es hora de ir a casa!")
else:
    # Calculamos el tiempo restante de trabajo
    horas_restantes = 19 - hora_actual
    minutos_restantes = horas_restantes * 60
   

    # Mostramos el mensaje con el tiempo restante
    print(f"Todavía quedan {horas_restantes} horas,{minutos_restantes} minutos.");
