import sys
import os
# Agrega la carpeta 'Fuente' al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from flask import Flask
from flask_cors import CORS

# APIS internas
from users_API import users_bp as Users_API
from chat_API import chat_bp as Chat_API


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)


# Blueprints de APIs
app.register_blueprint(Chat_API)
app.register_blueprint(Users_API)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
