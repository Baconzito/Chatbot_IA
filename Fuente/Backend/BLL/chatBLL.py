from Backend.MPP.chatMPP import ChatMPP
from datetime import datetime
from typing import Optional, Dict, Any

class ChatBLL:
    def __init__(self):
        self.chat_MPP = ChatMPP()

    def get_menu(self, menu_id):
        # Lógica para obtener el menú por ID
        return self.chat_MPP.get_menu_by_id(menu_id)
    
    def create_chat(self, chat_data: Dict[str, Any]) -> Optional[str]:
        """
        Recibe chat_data (debe contener id_usuario o user_id).
        Genera la fecha actual y delega en ChatMPP para crear el registro en BD.
        Retorna el id (string) del chat creado o None en caso de error.
        """
        try:
            id_usuario = chat_data.get('id_usuario') or chat_data.get('user_id') or chat_data.get('userId')
            if not id_usuario:
                raise ValueError("Falta id_usuario en chat_data")

            iniciado = datetime.utcnow().isoformat()
            inserted_id = self.chat_MPP.create_chat(id_usuario=id_usuario, iniciado=iniciado)
            return inserted_id  # puede ser str o None
        except Exception as e:
            print(f"ChatBLL.create_chat error: {e}")
            return None

    def close_chat(self, chat_id: str) -> bool:
        """
        Cierra el chat identificado por chat_id delegando en ChatMPP.
        Retorna True si se cerró correctamente, False en caso de error o no encontrado.
        """
        try:
            return self.chat_MPP.close_chat(chat_id)
        except Exception as e:
            print(f"ChatBLL.close_chat error: {e}")
            return False

