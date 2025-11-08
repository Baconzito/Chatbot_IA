from Backend.MPP import UserMPP 
from BE.Classes.User import User as UserBE
from Services.Intern.Password_Encripter import HashPassword as HP
import re

class UserBLL:
    def __init__(self):
        self.users_MPP = UserMPP.Mpp_User()
        # Initialize any required attributes or services
        pass

    def new_user(self, user_data):
        # Logic to create a user
        email = user_data.get('email')
        password = user_data.get('password')
        oUsuario = UserBE(email, HP(password))
        if not self.validar_Campos(oUsuario):
            return False
        return self.users_MPP.new_user(oUsuario)

    def get_user(self, user_id): #Traer usuario para mostrar perfil
        # Logic to get a user by ID
        
        pass

    def update_user_password(self, user_data):
        # Logic to update a user
        email = user_data.get('email')
        password = user_data.get('password')
        oUsuario = UserBE(email, HP(password))
        return self.users_MPP.update_user_password(oUsuario)

    def login(self, user_data):
        email = user_data.get('email')
        password = user_data.get('password')
        oUsuario = UserBE(email, HP(password))
        return self.users_MPP.login(oUsuario)
        
    
    def validar_Campos(self, user):
        if(user.Email == "" or user.Password == ""):
            return False
        regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(regex, user.Email):
            return False
        if len(user.Password) < 8 or not re.search(r'[A-Z]', user.Password) or not re.search(r'[a-z]', user.Password) or not re.search(r'\d', user.Password):
            return False
        return True