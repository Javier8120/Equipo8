from .database import *
#Metodo para retornar el usuario a partir del username (condiguracion de nuestros servicios a la base de datos.)
def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

#Registro de usuarios

def registro_usuarios(user_data):
    user = User(
    Rol= user_data['Rol'],
    nombre=user_data['nombre'],
    apeliido=user_data['apellido'],
    email=user_data['email'],
    cellphone=user_data['cellphone'],
    username=user_data['username'],
    password=user_data['password'],
   
    )
    user.set_password(user_data['password'])
    db.session.add(user)
    db.session.commit()
