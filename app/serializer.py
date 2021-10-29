#Obtener diccionario a partir de listado de objetos que tenemos......
#lo primero es importar marshmallow-sqlalchemy==0.24.1
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.schema import load_instance_mixin
#importamos la base de datos :v
from .database  import *


class CursoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Curso
        fields = ('id','nombre',)
        load_instance = True
""" 
class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Curso
        fields = ('id','nombre',)
        load_instance = True """