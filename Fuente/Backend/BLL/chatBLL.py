from Backend.MPP.chatMPP import chat as chatMPP

class Bll_chat():
    def __init__(self):
        self.chatMPP = chatMPP()
        self.chat_MPP = chatMPP.ChatMPP()


    def get_menu(self, menu_id):
        # Lógica para obtener el menú por ID
        pass