from Backend.MPP import UserMPP 
from BE.Classes.User import User as UserBE
from Services.Intern.Password_Encripter import HashPassword as HP
from Services.Intern.Password_Encripter import CheckPassword as CP
from Services.Intern.Sesion_Token import CreateToken, DecodeToken
import re
import os
from werkzeug.utils import secure_filename
from bson.objectid import ObjectId
import base64

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

    # def get_user(self, data): #Traer usuario para mostrar perfil
    #     try:
        
    #     # Logic to get a user by token
    #         token = data.get('token')
    #         payload = DecodeToken(token)
    #         if payload is None:
    #             return None

    #         user_id = payload.get('_id')
    #         usuario = self.users_MPP.get_user(user_id)
    #         if not usuario:
    #             return None

    #         # Soporta tanto dicts desde el MPP como objetos BE
    #         user_json = {
    #                 "_id": getattr(usuario, "Id", user_id) or user_id,
    #                 "email": getattr(usuario, "email", None),
    #                 "photo": getattr(usuario, "photo", None)
    #         }

    #         return user_json
    #     except Exception as e:
    #         print(f"Error in get_user BLL: {e}")
    #         return None
    
    def get_user(self, data): #Traer usuario para mostrar perfil
        try:
            token = data.get('token')
            payload = DecodeToken(token)
            if payload is None:
                return None

            user_id = payload.get('_id')
            usuario = self.users_MPP.get_user(user_id)
            if not usuario:
                return None

            def to_serializable(v):
                if v is None:
                    return None
                # ObjectId -> str
                if isinstance(v, ObjectId):
                    return str(v)
                # bytes -> intentar utf-8, si no -> base64
                if isinstance(v, (bytes, bytearray)):
                    try:
                        return v.decode('utf-8')
                    except Exception:
                        return base64.b64encode(bytes(v)).decode('ascii')
                # otros tipos primitivos quedan igual
                return v

            # Soporta tanto dicts desde el MPP como objetos BE
            if isinstance(usuario, dict):
                user_json = {
                    "_id": to_serializable(usuario.get("_id", user_id)),
                    "email": to_serializable(usuario.get("Email")),
                    "photo": to_serializable(usuario.get("Photo"))
                }
            else:
                user_json = {
                    "_id": to_serializable(getattr(usuario, "Id", user_id) or user_id),
                    "email": to_serializable(getattr(usuario, "Email", None)),
                    "photo": to_serializable(getattr(usuario, "Photo", None))
                }

            # Nunca devolver la contraseña ni datos sensibles
            return user_json
        except Exception as e:
            print(f"Error in get_user BLL: {e}")
            return None

    def update_user_password(self, user_data):
        # Logic to update a user
        try:
            email = user_data.get('email')
            password = user_data.get('password')
            oUsuario = UserBE(email, HP(password))
            return self.users_MPP.update_user_password(oUsuario)
        except Exception as e:
            print(f"Error in update_user_password BLL: {e}")
            return False
        
    def login(self, user_data):
        try:
            email = user_data.get('email')
            password = user_data.get('password')
            oUsuario = UserBE(email, HP(password))
            user_bd = self.users_MPP.login(oUsuario)
            if not user_bd:
                return None
            oUsuario.Id = str(user_bd["_id"])
            if(CP(password, user_bd["password"])):
                return CreateToken(oUsuario)
            return 1 # Credenciales inválidas
        except Exception as e:
            print(f"Error in login BLL: {e}")
    
    def validar_Campos(self, Email, Password):
        if(Email == "" or Password == ""):
            return False
        regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(regex, Email):
            return False
        if len(Password) < 8 or not re.search(r'[A-Z]', Password) or not re.search(r'[a-z]', Password) or not re.search(r'\d', Password):
            return False
        return True
    
    def upload_photo(self, email, file):
        try:
            upload_folder = os.path.join(os.getcwd(), "uploads", "usuarios")
            os.makedirs(upload_folder, exist_ok=True)

            filename = secure_filename(email + os.path.splitext(file.filename)[1])  # pisa la anterior
            file_path = os.path.join(upload_folder, filename)
            file.save(file_path)

            # Actualiza la referencia en BD
            relative_path = f"uploads/usuarios/{filename}"
            return self.users_MPP.update_user_photo(email, relative_path)
        except Exception as e:
            print("Error en upload_photo BLL:", e)
            return False