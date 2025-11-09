from flask import Blueprint, request, jsonify
from Backend.BLL.chatBLL import ChatBLL

chat_bp = Blueprint('chat_API', __name__, url_prefix='/chat')

chat_BLL = ChatBLL()

@chat_bp.route("/get_menu/<string:menu_id>", methods=["GET"])
def get_menu(menu_id):
    try:
        menu = chat_BLL.get_menu(menu_id)
        if menu:
            return jsonify(menu), 200
        return jsonify({'message': 'Menu not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
