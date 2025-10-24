from flask import Blueprint, request, jsonify
from Backend.BLL.UserBLL import UserMPP as BLLUser

users_bp = Blueprint('users_API', __name__, url_prefix='/users')

user_BLL = BLLUser.Bll_User()

#ABM de usuarios
@users_bp.route("/register", methods=["POST"])
def register():
    if(user_BLL.new_user(request.json)):
        return jsonify({'message': "Registro exitoso"}), 200
    else:
        return jsonify({'message': "Error en el registro"}), 400

@users_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return jsonify({'message': "Usuario eliminado"}), 200

#Actualizacion general
@users_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    return jsonify({'message': "Actualizaciion exitosa"}), 200

#Actualizacion contraseña
@users_bp.route("/<int:user_id>/password", methods=["PUT"])
def update_user_password(user_id):
    return jsonify({'message': "Contraseña actualizada"}), 200

#Login y Logout
@users_bp.route("/login", methods=["POST"])
def login():
    return jsonify({'message': "Login exitoso"}), 200

@users_bp.route("/logout", methods=["POST"])
def logout():
    return jsonify({'message': "Logout exitoso"}), 200
    
#Obtener usuario
@users_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return jsonify({'message': "Usuario encontrado"}), 200