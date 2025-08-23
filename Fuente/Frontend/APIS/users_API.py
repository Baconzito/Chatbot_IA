from flask import Blueprint, request, jsonify

users_bp = Blueprint('users_API', __name__, url_prefix='/users')

@users_bp.route("/submit", methods=["POST"])
def login():
    return jsonify({'message': "Login exitoso"}), 200

@users_bp.route("/submit", methods=["POST"])
def logout():
    return jsonify({'message': "Login exitoso"}), 200
    
@users_bp.route("/submit", methods=["POST"])
def register():
    return jsonify({'message': "Login exitoso"}), 200

