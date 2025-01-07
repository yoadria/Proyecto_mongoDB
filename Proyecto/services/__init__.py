from .mongo_service import MongoService
from .crud_operations import insert_data, read_data

'''Fichero que empaqueta conexion y operaciones crud'''

__all__ = ["MongoService", "insert_data", "read_data", 'update_data']
