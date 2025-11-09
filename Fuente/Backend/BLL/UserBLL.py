from Backend.MPP import UserMPP 
from BE.Classes.User import User as UserBE
from Services.Intern.Password_Encripter import HashPassword as HP
from Services.Intern.Password_Encripter import CheckPassword as CP
from Services.Intern.Sesion_Token import CreateToken, DecodeToken
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
        if not self.validar_Campos(email, password):
            return False
        oUsuario = UserBE(email, HP(password))
        
        return self.users_MPP.new_user(oUsuario)

    def get_user(self, data): #Traer usuario para mostrar perfil
        # Logic to get a user by token
        token = data.get('token')
        payload = DecodeToken(token)
        if payload is None:
            return None
        user_id = payload.get('_id')
        return self.users_MPP.get_user(user_id)

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
        bd_pass = self.users_MPP.login(oUsuario)
        if(CP(password, bd_pass)):
            return CreateToken(oUsuario)
        return 1 # Credenciales inválidas
        
    
    def validar_Campos(self, Email, Password):
        if(Email == "" or Password == ""):
            return False
        regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(regex, Email):
            return False
        if len(Password) < 8 or not re.search(r'[A-Z]', Password) or not re.search(r'[a-z]', Password) or not re.search(r'\d', Password):
            return False
        return True