from flask import Flask
from flask_cors import CORS

# APIS internas
from users_API import users_bp as Users_API


app = Flask(__name__)
CORS(app)  

# Blueprints de APIs
app.register_blueprint(Users_API)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
