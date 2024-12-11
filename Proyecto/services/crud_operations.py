from .mongo_service import MongoService

db = MongoService()

def insert(collection_name, data):
    collection = db.get_collection(collection_name)
    result = collection.insert_one(data)
    return result.inserted_id
