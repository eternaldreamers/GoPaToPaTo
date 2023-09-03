import database.mongo_setup as mongo_setup

class Curriculum:
    COLLECTION = mongo_setup.database.cvs

    def __init__(self, user_email, education, experience, skills):
        self.user_email = user_email
        self.education = education
        self.experience = experience
        self.skills = skills

    def save(self):
        """
        Guarda o actualiza el CV en la base de datos.
        """
        existing_cv = self.find_by_email(self.user_email)
        cv_data = {
            "user_email": self.user_email,
            "education": self.education,
            "experience": self.experience,
            "skills": self.skills
        }
        if existing_cv:
            self.update()
        else:
            self.COLLECTION.insert_one(cv_data)

    @classmethod
    def find_by_email(cls, email):
        """
        Busca un CV por el email del usuario.
        """
        return cls.COLLECTION.find_one({"user_email": email})

    def update(self):
        """
        Actualiza un CV existente en la base de datos.
        """
        updated_data = {
            "education": self.education,
            "experience": self.experience,
            "skills": self.skills
        }
        self.COLLECTION.update_one({"user_email": self.user_email}, {"$set": updated_data})

    @classmethod
    def delete_by_email(cls, email):
        """
        Elimina un CV usando el email.
        """
        cls.COLLECTION.delete_one({"user_email": email})
