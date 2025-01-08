from services.mongo_service import MongoService

db = MongoService()

def validacion_id(collection_name, dni):
    try:
        collection = db.get_collection(collection_name)
        if collection.find_one({"DNI": dni}) is not None:
            raise Exception("Error: ya existe otra persona con el mismo DNI")
    except Exception as e:
        raise Exception(f"Error al validar ID: {str(e)}")
