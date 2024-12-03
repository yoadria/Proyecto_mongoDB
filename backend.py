from pymongo import MongoClient
from faker import Faker
import random

# Configurar la conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["ProyectoDB"]  # Nombre de la base de datos

# Colecciones
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
            "telefono": fake.phone_number(),
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
            "telefono": fake.phone_number(),
            "email": fake.email()
        })
    medicos_col.insert_many(medicos)

    # Generar datos aleatorios para citas
    citas = []
    for _ in range(20):
        citas.append({
            "paciente_id": random.choice(pacientes)["_id"],  # Referencia a paciente
            "medico_id": random.choice(medicos)["_id"],      # Referencia a médico
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
