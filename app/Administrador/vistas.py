from flask import render_template as render, flash, redirect, url_for
import flask
from flask_login import  logout_user, login_required
from . import Administrador
from .formularios import  *
from app.servicios import *



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
    validar=False
    if register_form.validate_on_submit():
        user = get_user_by_username(register_form.username.data)
        Email = get_user_by_email(register_form.email.data)
        if user is None and Email is None: 
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
                validar=True
                registro_usuarios(user_data)
                flash("Usuario Registrado Correctamente", category="info")
                return redirect(url_for("Administrador.CrearUsuarios"))     
        else:
            
            if validar==False and Email is not None:
                flash("El correo digitado ya se encuentra registrado", category="warning")
            elif validar==False and user is not None:
                flash("El usuario digitado ya se encuentra registrado", category="warning")
            #elif validar==False:
             #   flash("Tanto el Correo como el usuario digitado se encuentran registrados", category="warning")
            
    return render('Administrador/CrearUsuarios.html', **context)

@Administrador.route('VerUsuarios', methods = ['GET', 'POST'])
@login_required
def VerUsuarios():
    return render('Administrador/Gcursos.html')


@Administrador.route('/cursos', methods=['GET', 'POST'])
@login_required
def cursos():
    cursos = list_cursos()
    register_form = RegisterCursoForm()
    context = {
        'register_form': register_form,
        'delete_form': DeleteCursoForm(),
        'cursos': cursos
    }

    if register_form.validate_on_submit():
        create_curso(register_form.name.data)
        flash("Curso registrao exitosamente.", category="success")

        return redirect(url_for('Administrador.cursos'))        

    return render('Administrador/cursos.html', **context)

@Administrador.route('/curso/delete/<curso_id>', methods=['POST'])
@login_required
def delete_curso_view(curso_id):
    delete_curso(curso_id)
    flash("Curso eliminado", category="success")   

    return redirect(url_for('Administrador.cursos')) 





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