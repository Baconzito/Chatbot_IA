import jwt
import datetime
from pathlib import Path
from dotenv import load_dotenv
import os

# Clave secreta para firmar el token (guárdala en un lugar seguro)

env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

def Get_key():
    return os.getenv("JWT_SECRET_KEY")

def CreateToken(usr):
    # Datos que quieres incluir en el token (payload)
    delta = int(os.getenv("JWT_EXPIRATION"))
    payload = {
        '_id': usr.Id,  # El ID del usuario
        'email': usr.Email,  # El nombre de usuario
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=int(delta))  # Expiración del token (1 hora)
    }

    # Generar el token JWT
    token = jwt.encode(payload, Get_key(), algorithm='HS256')

    return token

def DecodeToken(token):
    try:
        # Decodificar el token
        payload = jwt.decode(token, Get_key(), algorithms=['HS256'])

        return payload
    except jwt.ExpiredSignatureError:
        # El token ha expirado
        return None
    except jwt.InvalidTokenError:
        # El token no es válido
        return None
    except Exception as e:
        # Cualquier otro error
        print(e)
        return None
