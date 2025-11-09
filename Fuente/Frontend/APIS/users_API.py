from flask import Blueprint, request, jsonify
from Backend.BLL.UserBLL import UserBLL  # Fixed import

users_bp = Blueprint('users_API', __name__, url_prefix='/users')

user_BLL = UserBLL()  # Create instance of UserBLL directly

#ABM de usuarios
@users_bp.route("/register", methods=["POST"])
def register():
    print("Entro al registro")
    if(user_BLL.new_user(request.json)):
        return jsonify({'message': "Registro exitoso"}), 200
    else:
        return jsonify({'message': "Error en el registro"}), 400


#Actualizacion contraseña
@users_bp.route("/change_password", methods=["PUT"])
def update_user_password():
    data = request.json
    return jsonify({'message': "Contraseña actualizada"}), 200


@users_bp.route("/logout", methods=["POST"])
def logout():
    return jsonify({'message': "Logout exitoso"}), 200
    
@users_bp.route("/login", methods=["POST"])
def login():
    try:
        if (user_BLL.login(request.json)):
            return jsonify({'message':"login exitoso"}), 200
        else:
            return jsonify({'message': "Credenciales inválidas"}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500

#Obtener usuario
@users_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    if (user_BLL.get_user(user_id)):
        return jsonify({'message': "Usuario encontrado"}), 200
    else:
        return jsonify({'message': "Usuario no encontrado"}), 401
    