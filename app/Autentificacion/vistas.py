from flask import render_template as render, flash, redirect, url_for
from flask_login import login_user
from . import Autentificacion
from app.modelo import UserModel
from .formularios import LoginForm
from app.servicios import get_user_by_username


@Autentificacion.route('/', methods=['GET', 'POST'])
def Login():
    """ Método vista para el login de usuarios. """
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
# Verifiquemos el metodo del boton enviar (submit)
    if login_form.validate_on_submit():
        user = get_user_by_username(login_form.username.data)
        if user is not None:
            if user.check_password(login_form.password.data):
                user_model = UserModel(user)
                login_user(user_model)
                flash("Bienvenido al sistema", category="info")
                return redirect(url_for("Administrador.Inicio"))
            else:
                flash("Credenciales incorrectas", category="error")
        else:
            flash("Credenciales incorrectas", category="error")
    
    return render('Autentificacion/login.html', **context)


