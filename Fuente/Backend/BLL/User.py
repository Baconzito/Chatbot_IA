import MPP.User 
import BE.Classes.User as User
import re

class Bll_User:
    def __init__(self):
        self.users_MPP = MPP.User()
        # Initialize any required attributes or services
        pass

    def new_user(self, user_data):
        # Logic to create a user
        email = user_data.get('email')
        password = user_data.get('password')
        oUsuario = User.User(email, password)
        if not self.validar_Campos(oUsuario):
            return False
        return self.users_MPP.new_user(oUsuario)

    def get_user(self, user_id):
        # Logic to get a user by ID
        pass

    def update_user(self, user_id, user_data):
        # Logic to update a user
        pass

    def delete_user(self, user_id):
        # Logic to delete a user
        pass

    def list_users(self):
        # Logic to list all users
        pass

    # Add any other methods that exist in Mpp_User
    
    def validar_Campos(self, user):
        if(user.Email == "" or user.Password == ""):
            return False
        regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(regex, user.Email):
            return False
        if len(user.Password) < 8 or not re.search(r'[A-Z]', user.Password) or not re.search(r'[a-z]', user.Password) or not re.search(r'\d', user.Password):
            return False
        return True