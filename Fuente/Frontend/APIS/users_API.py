from flask import Blueprint, request, jsonify
from Backend.BLL.UserBLL import UserBLL  # Fixed import
import traceback

users_bp = Blueprint('users_API', __name__, url_prefix='/users')

user_BLL = UserBLL()


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
    data = request.json # json contiene email:<email>, password:<new_password>
    if(user_BLL.update_user_password(data)):
        return jsonify({'message': "Contraseña actualizada"}), 200
    else:
        return jsonify({'message': "Error al actualizar la contraseña"}), 400

@users_bp.route("/logout", methods=["POST"])
def logout():
    if(user_BLL.logout(request.json)): # json contiene token:<sesion_token>
        return jsonify({'message': "Logout exitoso"}), 200 # cerrar chat de sesion
    
@users_bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json() # json contiene email:<email>, password:<password>
        token = user_BLL.login(data) # retorna token o None
        if (token):
            return jsonify({'token': token}), 200
        else:
            return jsonify({'message': "Credenciales inválidas"}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@users_bp.route("/upload_photo", methods=["POST"])
def upload_photo():
    try:
        email = request.form.get('email')
        foto = request.files.get('foto')
        if not email or not foto:
            return jsonify({'message': 'Faltan datos'}), 400

        if user_BLL.upload_photo(email, foto):
            return jsonify({'message': 'Foto subida correctamente'}), 200
        else:
            return jsonify({'message': 'Error al guardar la foto'}), 500
    except Exception as e:
        print("Error en upload_photo:", traceback.format_exc())
        return jsonify({'message': 'Error interno del servidor'}), 500

#Obtener usuario

@users_bp.route("/get_user", methods=["POST"])
def get_user():
    try:
        usr = user_BLL.get_user(request.json)
        if (usr): # json contiene token:<sesion_token>
            return jsonify({'message': "Usuario encontrado","usuario":usr}), 200
        else:
            return jsonify({'message': "Usuario no encontrado"}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    