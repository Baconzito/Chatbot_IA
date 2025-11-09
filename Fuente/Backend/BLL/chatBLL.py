from Backend.MPP.chatMPP import ChatMPP
from datetime import datetime
from typing import Optional, Dict, Any
from Services.Intern.Sesion_Token import DecodeToken

class ChatBLL:
    def __init__(self):
        self.chat_MPP = ChatMPP()

    def get_menu(self, data):
        # Lógica para obtener el menú por ID
        menu_id = data.get('id_menu')
        chat_id = data.get('id_chat')
        if(menu_id == "75"):
            return self.chat_MPP.close_chat(chat_id)    
        return self.chat_MPP.get_menu_by_id(chat_id, menu_id)
 
    
    def create_chat(self, chat_data: Dict[str, Any]) -> Optional[str]:
        """
        Recibe chat_data (debe contener id_usuario o user_id).
        Genera la fecha actual y delega en ChatMPP para crear el registro en BD.
        Retorna el id (string) del chat creado o None en caso de error.
        """
        try:
            token = chat_data.get('token')
            id_usuario = DecodeToken(token)["_id"]
            if not id_usuario:
                raise ValueError("Falta el token o es inválido")

            inserted_id = self.chat_MPP.create_chat(id_usuario=id_usuario)
            return inserted_id  # puede ser str o None
        except Exception as e:
            print(f"ChatBLL.create_chat error: {e}")
            return None

    