from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField,RadioField
from wtforms.fields.html5 import EmailField 
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrarUsuario(FlaskForm):
    Rol= RadioField('Rol', choices=[('1','Administrador'),('2','Docente'), ('3','Etudiante')])
    nombre = StringField("Nombre", validators=[DataRequired(), Length(min=2, max=20)])
    apellido = StringField("Apellido", validators=[DataRequired(), Length(min=2, max=20)])
    email  = EmailField("Correo", validators=[DataRequired(), Email(), Length(min=5, max=60)])
    cellphone = StringField("Celular", validators=[DataRequired(), Length(min=7, max=20)])
    username = StringField("Username", validators=[DataRequired(), Length(min=5, max=10)])
    password =  PasswordField("Contraseña", validators=[
        DataRequired(),
        Length(min=6, max=20),
        EqualTo('password_confirm')
    ])
    password_confirm = PasswordField("Confimarción de contraseña", validators=[DataRequired(), Length(min=6, max=20)])
    

    submit = SubmitField("Crear")
  

