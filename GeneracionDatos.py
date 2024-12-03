from pymongo import MongoClient
from faker import Faker
import Conexion
import random

# Configurar la conexión a MongoDB

client = Conexion.conexion()

db = client["ProyectoDB"]
pacientes_col = db["pacientes"]
medicos_col = db["medicos"]
citas_col = db["citas"]

def generar_datos(): 

    # Generar datos aleatorios para pacientes
    fake = Faker()
    pacientes = []

    for _ in range(10):


        pacientes.append({
            "nombre": fake.name(),
            "edad": random.randint(18, 90),
            "direccion": fake.address(),
            "telefono": "6" + str(random.randint(0,99999999)),
            "email": fake.email()
        })
    pacientes_col.insert_many(pacientes)

    # Generar datos aleatorios para médicos
    especialidades = ["Cardiología", "Dermatología", "Pediatría", "Neurología", "Oncología"]

    medicos = []
    for _ in range(5):

        medicos.append({
            "nombre": fake.name(),
            "especialidad": random.choice(especialidades),
            "telefono": "6" + str(random.randint(0,99999999)),
            "email": fake.email()
        })
    medicos_col.insert_many(medicos)

    # Generar datos aleatorios para citas
    citas = []
    for _ in range(20):
        citas.append({

            "paciente": (random.choice(pacientes)["_id"],random.choice(pacientes)["nombre"]),  # Referencia a paciente
            "medico": (random.choice(medicos)["_id"], random.choice(medicos)["nombre"]),     # Referencia a médico
            "fecha": fake.date_time_this_year(),
            "motivo": fake.sentence(nb_words=6)
        })
    citas_col.insert_many(citas)

    print("Datos generados e insertados correctamente.")

def menu():

    while True:
        
        print("\n--- Menú Principal ---")
        print("1. Generar datos")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            generar_datos()
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()
