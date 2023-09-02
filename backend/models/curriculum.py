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
        cv_data = {
            "user_email": self.user_email,
            "education": self.education,
            "experience": self.experience,
            "skills": self.skills
        }
        self.COLLECTION.insert_one(cv_data)

    @classmethod
    def find_by_email(cls, email):
        """
        Busca un CV por el email del usuario.
        """
        return cls.COLLECTION.find_one({"user_email": email})