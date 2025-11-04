from Backend.MPP.chatMPP import ChatMPP

class ChatBLL:
    def __init__(self):
        self.chat_MPP = ChatMPP()

    def get_menu(self, menu_id):
        # Lógica para obtener el menú por ID
        return self.chat_MPP.get_menu_by_id(menu_id)
    
    def create_chat(self, chat_data):
        # chat_data es un diccionario con la información del usuario (id)
        # Lógica para crear un nuevo chat
        pass