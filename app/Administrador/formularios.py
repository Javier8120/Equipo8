from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField,RadioField, SelectField
from wtforms.fields.html5 import EmailField 
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegistrarUsuario(FlaskForm):
    Rol= SelectField('Selecione Rol', choices=[('1','Administrador'),('2','Docente'), ('3','Estudiante')])
    nombre = StringField("Nombre", validators=[DataRequired(), Length(min=3, max=20, message="El nombre debe tener entre 3 y 20 caracteres")])
    apellido = StringField("Apellido", validators=[DataRequired(), Length(min=3, max=20, message="El o los apellidos deben tener entre 2 y 20 caracteres")])
    email  = EmailField("Correo", validators=[DataRequired(), Email(), Length(min=5, max=40, message="El correo debe tener entre 5 y 40 caracteres")])
    cellphone = StringField("Celular", validators=[DataRequired(), Length(min=10, max=11, message="Este campo debe tener entre 10 y 11 caracteres")])
    username = StringField("Username", validators=[DataRequired(), Length(min=5, max=10, message="El usuario debe tener entre 5 y 10 caracteres")])
    password =  PasswordField("Contraseña", validators=[
        DataRequired(),
        Length(min=6, max=15, message="La contraseña debe tener entre 6 y 15 caracteres"),
        EqualTo('password_confirm')
    ])
    password_confirm = PasswordField("Confimarción de contraseña", validators=[DataRequired(), Length(min=6, max=20, message="La contraseña debe tener entre 6 y 15 caracteres")])
    submit = SubmitField("Crear")
  


# Formulario para eliminar Cursos
class EliminarCursoForm():
    submit = SubmitField("Eliminar Curso")

# Formulario para registrar cursos
class RegistroCursoForm():
    name = StringField("Curso", validators=[DataRequired(), Length(min=2, max=30, message="Este campo debe contener de 2 a 30 caracteres")])
