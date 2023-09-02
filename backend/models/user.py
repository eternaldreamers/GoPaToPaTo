import database.mongo_setup as mongo_setup

class User:
    COLLECTION = mongo_setup.database.users

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def save(self):
        """
        Guarda o actualiza el usuario en la base de datos.
        """
        user_data = {
            "name": self.name,
            "email": self.email,
            "password": self.password
        }
        self.COLLECTION.insert_one(user_data)

    @classmethod
    def find_by_email(cls, email):
        """
        Busca un usuario por su email.
        """
        return cls.COLLECTION.find_one({"email": email})
