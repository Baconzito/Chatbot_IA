from flask import Blueprint, request, jsonify
import Backend.BLL.User as users_BLL

users_bp = Blueprint('users_API', __name__, url_prefix='/users')

#ABM de usuarios
@users_bp.route("/register", methods=["POST"])
def register():
    return jsonify({'message': "Registro exitoso"}), 200

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