from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    """ Formulario de login. """
    username = StringField("Usuario", validators=[DataRequired(), Length(min=5, max=10, message="El Usuario debe tener entre 6 y 10 caracteres")])
    password = PasswordField("Contraseña", validators=[DataRequired(), Length(min=6, max=10, message='La contraseña debe tener entre 6 y 10 caracteres')])
    submit = SubmitField("Login")

    