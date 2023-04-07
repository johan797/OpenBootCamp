import pickle

class Vehículo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

# Creamos un objeto 
mi_coche = Vehículo('Toyota', 'Fortuner', 2023)

#serializamos
with open('mi_coche.pickle', 'wb') as f:
    pickle.dump(mi_coche, f)

#desrializamos
with open('mi_coche.pickle', 'rb') as f:
    mi_coche_deserializado = pickle.load(f)
    print(mi_coche_deserializado.marca)
    print(mi_coche_deserializado.modelo)
    print(mi_coche_deserializado.año)