from pymongo import MongoClient
from bson.objectid import ObjectId

# Modelos
class Paciente:
    
    def __init__(self, nombre, edad, genero, direccion, telefono, email):

        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.direccion = direccion
        self.telefono = telefono
        self.email = email


class Medico:
    
    def __init__(self, nombre, especialidad, telefono, email):
        self.nombre = nombre
        self.especialidad = especialidad
        self.telefono = telefono
        self.email = email
    

class Cita:
    
    def __init__(self, id_paciente, id_medico, fecha, motivo):
        self.id_paciente = id_paciente
        self.id_medico = id_medico
        self.fecha = fecha
        self.motivo = motivo
    

