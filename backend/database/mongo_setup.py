from pymongo import MongoClient

# Constantes
DATABASE_NAME = "cv_platform"
MONGO_URI = "mongodb://localhost:27017/"

# Crear una conexión global al cliente MongoDB
client = MongoClient(MONGO_URI)

# Crear una conexión global a la base de datos
database = client[DATABASE_NAME]


def init_db():
    """
    Función para inicializar la base de datos. Puedes agregar configuraciones iniciales aquí si lo deseas.
    """
    collections = database.list_collection_names()
    pass
