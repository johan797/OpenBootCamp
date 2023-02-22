#En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga
#como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos,
#imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
    #metodo integrado para inicializar clase
    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota
        
    # metodo imprimir
    def imprimir(self):
               print(self.nombre, 'tu nota es: ' , self.nota)
               
   # metodo aprobacion
    def aprobacion(self):
            if self.nota < 3:
                print("Has Suspendido!")
            else:
                print("Has aprobado!")
 
 
 

alumno1=Alumno("Juan", 5)
alumno2=Alumno("Pedro", 2.5)
 
alumno1.imprimir()
alumno1.aprobacion()
alumno2.imprimir()
alumno2.aprobacion()
