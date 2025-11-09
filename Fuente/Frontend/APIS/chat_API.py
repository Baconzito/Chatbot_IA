from flask import Blueprint, request, jsonify
from Backend.BLL.chatBLL import ChatBLL

chat_bp = Blueprint('chat_API', __name__, url_prefix='/chat')

chat_BLL = ChatBLL()

@chat_bp.route("/get_menu", methods=["GET"])
def get_menu():
    try:
        menu = chat_BLL.get_menu(request.json) # recibe id_menu e id_chat
        if menu:
            return jsonify(menu), 200
        return jsonify({'message': 'Menu no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@chat_bp.route("/create_chat", methods=["POST"])
def create_chat(): # se guarda el chat_id en cookies igual que el token
    try:
        chat_id = chat_BLL.create_chat(request.json) # recibe token jwt
        if chat_id:
            return jsonify({"chat_id": chat_id}), 200
        return jsonify({'message': 'Fallo en chat'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
