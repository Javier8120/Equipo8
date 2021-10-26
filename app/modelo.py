from flask_login import UserMixin
from .servicios import get_user_by_username

# Modelo de usuario - login
class UserModel(UserMixin):
    def __init__(self, user_data):
        self.id = user_data.username
        self.password = user_data.password
        self.avatar = user_data.avatar
       
     #metodo para obtener el usuario a partir del username  

    @staticmethod
    def get(username):
        """ Método para obtener el usuario a partir del username. """
        user_data = get_user_by_username(username)
        return UserModel(user_data)