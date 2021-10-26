#Confugracion de la app // 
from flask import Flask
from flask_bootstrap import Bootstrap
from app import Administrador
from app.config import config   # Importando config.py
from .database import db
from .Autentificacion import Autentificacion
from .Administrador import Administrador
from .Docente import Docente
from .Estudiante import Estudiante
from flask_login import LoginManager
from .modelo import UserModel



login_manager = LoginManager()
login_manager.login_view = "Autentificacion.Login"
login_manager.login_message = "Oee!, Debes Iniciar Sesion para continuar"
@login_manager.user_loader
def load_user(username):
    return UserModel.get(username)
 
def create_app():
    # Crear app de FLASK
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(config)
    app.register_blueprint(Autentificacion)
    app.register_blueprint(Administrador)
    app.register_blueprint(Docente)
    app.register_blueprint(Estudiante)
    
    
    login_manager.init_app(app)
    db.init_app(app)
    return app