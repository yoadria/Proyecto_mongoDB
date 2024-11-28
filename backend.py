from pymongo import MongoClient
from faker import Faker
import random

# Configurar la conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["ProyectoDB"]  # Nombre de la base de datos

# Inicializar Faker
fake = Faker()

# Colecciones
pacientes_col = db["pacientes"]
medicos_col = db["medicos"]
citas_col = db["citas"]

# Generar datos aleatorios para pacientes
pacientes = []
for _ in range(10):
    pacientes.append({
        "nombre": fake.name(),
        "edad": random.randint(18, 90),
        "direccion": fake.address(),
        "telefono": fake.phone_number(),
        "email": fake.email()
    })

# Insertar los datos en la colección de pacientes
pacientes_col.insert_many(pacientes)

# Generar datos aleatorios para medicos
especialidades = ["Cardiología", "Dermatología", "Pediatría", "Neurología", "Oncología"]
medicos = []
for _ in range(5):
    medicos.append({
        "nombre": fake.name(),
        "especialidad": random.choice(especialidades),
        "telefono": fake.phone_number(),
        "email": fake.email()
    })

# Insertar los datos en la colección de médicos
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

# Insertar los datos en la colección de citas
citas_col.insert_many(citas)

print("Datos insertados correctamente.")
