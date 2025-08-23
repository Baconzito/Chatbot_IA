from Services.Extern import Conection as cx
from BE.Classes import User
from Backend.MPP import Sp

class Mpp_User:
    def __init__(self):
        pass
    def get_user(Id):
        try:
            conn = cx.get_connection()
            cursor = conn.cursor()
            cursor.execute(Sp.StoredProcedures_User["Get_User"],Id)
            usr = User(cursor["Id"], cursor["Email"], cursor["Password"])
            return usr
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        return None

    def new_user(usr):
        try:
            conn = cx.get_connection()
            cursor = conn.cursor()
            cursor.execute(Sp.StoredProcedures_User["New_User"],(usr.Email, usr.Password))
            conn.commit()
            return True
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        return False

    def update_user(usr):
        try:
            conn = cx.get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE Users SET Email = {usr.Email}, Password = {usr.Password} WHERE Id = {usr.Id}")
            conn.commit()
            return True
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        return False

    def delete_user(usr):
        try:
            conn = cx.get_connection()
            cursor = conn.cursor()
            sp = Sp.StoredProcedures_User["Delete_User"]
            cursor.execute("EXEC {sp}",usr.Id)
            conn.commit()
            return True
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        return False