from flask import Blueprint, request, jsonify
from Backend.BLL.chatBLL import chat as BLLChat

users_bp = Blueprint('users_API', __name__, url_prefix='/users')

user_BLL = BLLChat.UserBLL()
