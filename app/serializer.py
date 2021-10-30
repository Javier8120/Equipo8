#Obtener diccionario a partir de listado de objetos que tenemos......
#lo primero es importar marshmallow-sqlalchemy==0.24.1
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
#importamos la base de datos :v
from .database import *


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model: User
        fields = ('id', 'name', 'lastName', 'username', 'email', 'password', 'is_admin', 'cellphone', 'avatar',)
        load_instance = True

class CursoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model: Curso
        fields = ('id', 'name',)
        load_intance = True
