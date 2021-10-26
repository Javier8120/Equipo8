from .database import *

def create_db():
    #Metodo para la creacion de la base de datos 
    db.drop_all()
    db.create_all()

def init_db():
    #Metodo para inicializar nuestra base de datos :V
    create_db()
    #Usuario por defecto (admin)
    admin = User(
        Rol='1',
        nombre='Javier',
        apeliido='Moreno',
        email='morenofj@uninorte.edu.co',
        cellphone='3104207720',
        username='Javier',
        
    )
    admin.set_password("Adm1n**123")
    db.session.add(admin) 
    db.session.commit()  #Registrar Cambios
   