# Configuracion de la base de datos (Modelos (Tablas))
# Clase Usuarios / Admin / Docente / Estudiante / Cursos / Materias /  
from werkzeug.security import generate_password_hash, check_password_hash   # Generar contraseña encriptada y chekear si ya esta--- def set Passwod   
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

# Docuementacion SQLAlCHEMY 
class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    Rol = db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    apeliido = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    cellphone = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    avatar = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username
    
#Generar contraseña encriptada
    def set_password(self, password):
        self.password = generate_password_hash(password)
#Chekear si ya esta protegida o no 
    def check_password(self, password):
        return check_password_hash(self.password, password)

class Docente(db.Model):
    __tablename__ = 'Docentes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id', ondelete='CASCADE'), nullable=False)
    usuario = db.relationship('User', backref=db.backref('Docentes', lazy=True))
class Estudiante(db.Model):
    __tablename__ = 'Estudiantes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id', ondelete='CASCADE'), nullable=False)
    usuario = db.relationship('User', backref=db.backref('Estudiantes', lazy=True))



class Curso(db.Model):
    __tablename__ = 'cursos'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class Asignatura(db.Model):
    __tablename__ = 'asignaturas'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    is_public = db.Column(db.Boolean, default=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id', ondelete='CASCADE'), nullable=False)
    curso = db.relationship('Curso', backref=db.backref('asignaturas', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('asignaturas', lazy=True))

