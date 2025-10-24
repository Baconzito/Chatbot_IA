from flask import Blueprint, request, jsonify
from Backend.BLL.chatBLL import chat as BLLChat

chat_bp = Blueprint('users_API', __name__, url_prefix='/users')

chat_BLL = BLLChat.Bll_chat()


@chat_bp.route("/get_menu/<string:menu_id>", methods=["PUT"])
def get_menu(menu_id):
    
    return jsonify({'message': "Registro exitoso"}), 200
    