from flask import render_template as render, flash, redirect, url_for
from . import Docente
from app.modelo import UserModel
from flask_login import  logout_user, login_required



@Docente.route('/Inicio', methods=['GET', 'POST'])
@login_required
def Inicio():
  return render('Docente/Inicio.html')


@Docente.route('/perfil', methods=['GET', 'POST'])
@login_required
def perifil():
  return render('Docente/PerfilD.html')
  

@Docente.route('/asignar', methods=['GET', 'POST'])
@login_required
def asignar():
  return render('Docente/asignar.html')
  

@Docente.route('/Calificar', methods=['GET', 'POST'])
@login_required
def Calificar():
  return render('Docente/Calificar.html')
  
@Docente.route('/CursoD', methods=['GET', 'POST'])
@login_required
def CursoD():
  return render('Docente/CursoD.html')
  
@Docente.route('/CerrarSesion')
@login_required
def CerrarSesion():
    logout_user()
    flash('Sesion Cerrada', category="info")
    return redirect(url_for('Autentificacion.Login'))
