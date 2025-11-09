from dataclasses import dataclass, asdict
from Services.Extern.Conection import MongoDBConnection
from typing import Optional, List, Dict, Any
from datetime import datetime
from bson import ObjectId

class ChatMPP:
    def __init__(self):
        # Initialize MongoDB connection (uses env var if configured)
        self.db_conection = MongoDBConnection()
        # No need for _ensure_db() since we're using MongoDB

    def get_menu_by_id(self, chat_id: str, menu_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves a menu by its ID using the MongoDB connection.
        
        Args:
            menu_id (str): The ID of the menu to retrieve
            
        Returns:
            Optional[Dict[str, Any]]: The menu document if found, None otherwise
        """
        try:
            menu = self.db_conection.get_menu_by_id(
                menu_id=menu_id,
                close_after=True
            )
            self.add_menu_to_chat(chat_id, menu_id)
            return menu
        except Exception as e:
            print(f"Error retrieving menu from database: {e}")
            return None

    def create_chat(self, id_usuario: str, id_menu: str):
        """
        Crea un documento Chat en la colección 'Chats'.
        Args:
            id_usuario: id del usuario que inicia el chat
            iniciado: fecha/hora de inicio en ISO format (si no se pasa, se genera ahora)
        Returns:
            inserted_id (str) del chat creado o None en caso de error
        """
        try:
            iniciado = datetime.utcnow().isoformat()
            doc = {
                "id_usuario": id_usuario,
                "iniciado": iniciado,
                "activo": True
            }
            inserted_id = self.db_conection.insert_document(
                db_name="chatbot_ia",
                collection_name="Chats",
                document=doc,
                close_after=True
            )
            if inserted_id:
                return str(inserted_id)
            return None
        except Exception as e:
            print(f"Error creating chat: {e}")
            return None

    def add_menu_to_chat(self, id_chat, id_menu):
        if not id_menu or not id_chat:
            return None
        try:
            enviado = datetime.utcnow().isoformat()
            doc = {
                "id_chat": id_chat,
                "enviado": enviado,
                "id_menu": id_menu
            }
            inserted_id = self.db_conection.insert_document(
                db_name="chatbot_ia",
                collection_name="Messages",
                document=doc,
                close_after=True
            )
            return str(inserted_id) if inserted_id else None
        except Exception as e:
            print(f"Error adding menu to chat: {e}")
            return None

    def close_chat(self, chat_id: str):
        """
        Marca el chat como cerrado (estado = False).
        Se asume que el identificador del chat es un string (no ObjectId).
        Busca por varias posibles claves (_id,) y devuelve
        True si se encontró el documento (aunque ya estuviera cerrado), False en caso contrario.
        """
        try:
            # Asegurar conexión
            if not getattr(self.db_conection, "client", None):
                self.db_conection.connect()

            db = self.db_conection.get_database("chatbot_ia")
            if db is None:
                return False

            query = {
                "$or": [
                    {"_id": chat_id}
                ]
            }

            result = db["Chats"].update_one(
                query,
                {"$set": {"activo": False}}
            )
            if result.matched_count > 0:
                return self.get_menu_by_id(chat_id, id_menu="75")
            return None
        except Exception as e:
            print(f"Error closing chat: {e}")
            return None
        finally:
            try:
                self.db_conection.close()
            except Exception:
                pass

