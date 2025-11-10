import bcrypt

# Para almacenar la contraseña (en el registro del usuario)

def HashPassword(password):
    return bcrypt.hashpw(str(password).encode('utf-8'), bcrypt.gensalt())

# Para verificar la contraseña (login)
def CheckPassword(password, hashed_password):
    return bcrypt.checkpw(str(password).encode('utf-8'), hashed_password)
