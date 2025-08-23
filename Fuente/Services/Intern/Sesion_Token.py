import jwt
import datetime

# Clave secreta para firmar el token (guárdala en un lugar seguro)
_SECRET_KEY = "mi_clave_secreta"
def Get_key():
    return _SECRET_KEY
def Set_key(key):
    pass

def CreateToken(usr):
    # Datos que quieres incluir en el token (payload)
    payload = {
        'user_id': usr.Id,  # El ID del usuario
        'Email': usr.Email,  # El nombre de usuario
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Expiración del token (1 hora)
    }

    # Generar el token JWT
    token = jwt.encode(payload, _SECRET_KEY, algorithm='HS256')

    return token

def DecodeToken(token):
    try:
        # Decodificar el token
        payload = jwt.decode(token, _SECRET_KEY, algorithms=['HS256'])

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
