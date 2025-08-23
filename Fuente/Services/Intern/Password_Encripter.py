import bcrypt

# Para almacenar la contraseña (en el registro del usuario)

def HashPassword(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Para verificar la contraseña (al momento de iniciar sesión)
def CheckPassword(password, hashed_password):
    return bcrypt.checkpw(HashPassword(password), hashed_password)
