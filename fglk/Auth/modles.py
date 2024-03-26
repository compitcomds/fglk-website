from flask_login import UserMixin
from bson.objectid import ObjectId

class Student(UserMixin):
    def __init__(self, user_id:str, name:str, role:str, courses:ObjectId, email:str, token:str):
        self.user_id = user_id
        self.name = name
        self.role=role
        self.courses=courses
        self.email=email
        self.token=token
    def get_id(self):
        return str(self.user_id)

    @staticmethod
    def get(user_id, name, role):
        return Student(user_id=user_id, name=name, role=role, courses=courses, email=email, token=token)
    

class Admin(UserMixin):
    def __init__(self, user_id:str, name:str, role:str, email:str,token:str):
        self.user_id = user_id
        self.name = name
        self.role=role
        self.email=email
        self.token=token
    def get_id(self):
        return str(self.user_id)

    @staticmethod
    def get(user_id, name, role):
        return Admin(user_id=user_id, name=name,role=role, email=email, token=token)