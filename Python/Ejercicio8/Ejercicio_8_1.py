# Abrimos el archivo 'mi_primer_archivo.txt' en modo escritura ('w')
file = open('mi_archivo.txt', 'w')

# Escribimos en el archivo la cadena de texto '¡He creado mi primer archivo!\n'
file.write('¡Escribo mi primer archivo!\n')

# Cerramos el archivo
file.close()

# Abrimos el archivo 'mi_primer_archivo.txt' en modo lectura y escritura ('r+')
file = open('mi_archivo.txt', 'r+')

# Leemos la primera línea del archivo, pero no hacemos nada con ella
file.readline()

# Escribimos en el archivo la cadena de texto 'Esta es la segunda vez que escribo.\n'
file.write('Escribo otra vez en mi archivo.\n')

# Movemos el puntero al inicio del archivo
file.seek(0)

# Imprimimos todo el contenido del archivo
print(file.read())

# Cerramos el archivo
file.close()