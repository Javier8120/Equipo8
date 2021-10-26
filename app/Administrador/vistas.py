from flask import render_template as render, flash, redirect, url_for
from flask_login import  login_user, logout_user, login_required
from . import Administrador
from app.modelo import UserModel
from .formularios import  RegistrarUsuario
from app.servicios import get_user_by_username, registro_usuarios



@Administrador.route('/Inicio', methods = ['GET', 'POST'])
@login_required
def Inicio():
    return render('Administrador/Inicio.html')

@Administrador.route('/perfil', methods = ['GET', 'POST'])
@login_required
def perfil():
    return render('Administrador/perfil.html')

@Administrador.route('/CrearUsuarios', methods=['GET', 'POST'])
@login_required
def CrearUsuarios():
    """ Método vista para el registro de usuarios. """
    register_form = RegistrarUsuario()
    context = {
        'register_form': register_form
    }
    if register_form.validate_on_submit():
        user = get_user_by_username(register_form.username.data)
        if user is None:
        #Proceso para registrar usuario :V
                user_data = {
                    'Rol':register_form.Rol.data,  
                    'nombre':register_form.nombre.data,
                    'apellido':register_form.apellido.data,    
                    'email':register_form.email.data,   
                    'cellphone':register_form.cellphone.data,   
                    'username':register_form.username.data,    
                    'password':register_form.password.data,  
                }

                registro_usuarios(user_data)
                user_model = UserModel(
                get_user_by_username(register_form.username.data)
                )   
                login_user(user_model)
                flash("Usuario Registrado Correctamente", category="info")
                return redirect(url_for("Administrador.CrearUsuarios")) 
                
        else:
            flash("ya existe este USUARIO en el sistema", category="warning")
        
            

    return render('Administrador/CrearUsuarios.html', **context)



@Administrador.route('VerUsuarios', methods = ['GET', 'POST'])
@login_required
def VerUsuarios():
    return render('Administrador/Gcursos.html')

@Administrador.route('/GestionCursos', methods = ['GET', 'POST'])
@login_required
def Gcursos():
    return render('Administrador/Gcursos.html')

@Administrador.route('/CAsignatura', methods = ['GET', 'POST'])
@login_required
def CAsignatura():
    return render('Administrador/CAsignatura.html')

@Administrador.route('/calendario', methods = ['GET', 'POST'])
@login_required
def calendario():
    return render('Administrador/calendario.html')

@Administrador.route('/novedades', methods = ['GET', 'POST'])
@login_required
def novedades():
    return render('Administrador/novedades.html')



@Administrador.route('/CerrarSesion')
@login_required
def CerrarSesion():
    logout_user()
    flash('Sesion Cerrada', category="info")
    return redirect(url_for('Autentificacion.Login'))