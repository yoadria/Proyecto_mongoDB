from pymongo import MongoClient

def conexion():

    try:
        
        client = MongoClient("mongodb://localhost:27017/")
        print("Conexión establecida con MongoDB")

        return client
            
        
    except Exception as e:
            print(f"Error al conectar con MongoDB: {e}")
