from marshmallow import schema
from .database import *
from .serializer import *
#Metodo para retornar el usuario a partir del username (condiguracion de nuestros servicios a la base de datos.)
def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()



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



#Consultar , crear y eliminar Cursos
def get_curso_by_id(curso_id):
    #Metodo para buscar la categoria por Id
    return Curso.query.get(curso_id)

#Metodo para eliminar 
def eliminar_curso(curso_id):
    curso = get_curso_by_id(curso_id)

    db.session.delete(curso)
    db.session.commit()


#Metodo para Crear Curso :v
def crear_curso(nombre):
    curso = Curso(nombre=nombre)

    db.session.add(curso)
    db.session.commit()

#Metodo para obtener el listado de Cursos disponibles :V
def lista_cursos():
    schema = cursoSchema()
    data = Curso.query.all()
    cursos =[schema.dump(c) for c in data]
    return cursos