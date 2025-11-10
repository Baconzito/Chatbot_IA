from Services.Extern.Conection import MongoDBConnection
from BE.Classes.User import User
import datetime

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
                query={"_id": Id},
                limit=1
            )
            if docs and len(docs) > 0:
                doc = docs[0]
                user_id = str(doc.get("_id"))
                return User( doc.get("email"), doc.get("password"), id=user_id, photo=doc.get("foto", None))
            return None
        except Exception as e:
            print(f"Error getting user: {e}")
            return None

    def new_user(self, usr):
        """Crea un nuevo usuario en la base de datos."""
        try:
            user_doc = {
                "email": usr.Email,
                "password": usr.Password,
                "ultima_modificacinon": datetime.datetime.utcnow()
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

    def update_user_password(self, usr):
        """Actualiza la password de un usuario existente."""
        try:
            self.connection.connect()
            db = self.connection.get_database(self.db_name)
            # comparar explícitamente con None (Database no soporta truthiness)
            if db is None:
                print("No se pudo obtener la DB:", self.db_name)
                return False

            # soportar tanto usr.email / usr.password como usr.Email / usr.Password
            email = getattr(usr, "Email", None)
            password = getattr(usr, "Password", None)

            if not email or not password:
                print("Datos incompletos para update_user_password:", email, password)
                return False

            result = db[self.collection].update_one(
                {"email": email},
                {"$set": {
                    "password": password
                }}
            )
            if(result.matched_count > 0 or result.modified_count > 0):
                return True
            else:
                return False  
        except Exception as e:
            print(f"Error updating user: {e}")
            return False
        finally:
            self.connection.close()
            
    def login(self, usr):
        """
        Autentica a un usuario buscando primero por email y luego validando contraseña.
        Returns:
            tuple: (bool, str) - (éxito/fallo, id del usuario si éxito o None si fallo)
        """
        try:
            docs = self.connection.find_documents(
                self.db_name,
                self.collection,
                query={"email": usr.Email},
                limit=1
            )
            if docs and len(docs) > 0:
                stored_user = docs[0]
                return stored_user
        except Exception as e:
            print(f"Error during login: {e}")
            return False, None
        finally:
            self.connection.close()
            
    def update_user_photo(self, email, photo_path):
        """Actualiza la ruta de la foto del usuario."""
        try:
            self.connection.connect()
            db = self.connection.get_database(self.db_name)
            result = db[self.collection].update_one(
                {"email": email},
                {"$set": {"foto": photo_path}}
            )
            if(result.matched_count > 0 or result.modified_count > 0):
                return True
            else:
                return False       
        except Exception as e:
            print(f"Error updating user photo: {e}")
            return False
        finally:
            self.connection.close()