from Services.Extern.Conection import MongoDBConnection
from BE.Classes.User import User

class Mpp_User:
    def __init__(self):
        """Inicializa el mapper para usuarios usando MongoDB."""
        self.connection = MongoDBConnection()
        self.db_name = "chatbot_ia"
        self.collection = "Users"

    def get_user(self, Id):
        """Busca y devuelve un usuario por su Id."""
        try:
            docs = self.connection.find_documents(
                self.db_name,
                self.collection,
                query={"Id": Id},
                limit=1
            )
            if docs and len(docs) > 0:
                doc = docs[0]
                return User(doc["Id"], doc["Email"], doc["Password"])
            return None
        except Exception as e:
            print(f"Error getting user: {e}")
            return None

    def new_user(self, usr):
        """Crea un nuevo usuario en la base de datos."""
        try:
            user_doc = {
                "Email": usr.Email,
                "Password": usr.Password
            }
            result = self.connection.insert_document(
                self.db_name,
                self.collection,
                document=user_doc
            )
            return result is not None
        except Exception as e:
            print(f"Error creating user: {e}")
            return False

    def update_user(self, usr):
        """Actualiza los datos de un usuario existente."""
        try:
            db = self.connection.get_database(self.db_name)
            if not db:
                return False
                
            result = db[self.collection].update_one(
                {"Id": usr.Id},
                {"$set": {
                    "Email": usr.Email,
                    "Password": usr.Password
                }}
            )
            return result.modified_count > 0
        except Exception as e:
            print(f"Error updating user: {e}")
            return False
        finally:
            self.connection.close()

    def login(self, usr):
        """Autentica a un usuario por email y contraseña."""
        try:
            docs = self.connection.find_documents(
                self.db_name,
                self.collection,
                query={"Email": usr.Email, "Password": usr.Password},
                limit=1
            )
            return docs is not None and len(docs) > 0
        except Exception as e:
            print(f"Error during login: {e}")
            return False
        
    def delete_user(self, usr):
        """Elimina un usuario de la base de datos."""
        try:
            db = self.connection.get_database(self.db_name)
            if not db:
                return False
                
            result = db[self.collection].delete_one({"Id": usr.Id})
            return result.deleted_count > 0
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False
        finally:
            self.connection.close()