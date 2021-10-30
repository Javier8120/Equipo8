from flask import render_template as render, flash, redirect, url_for
from . import Estudiante
from app.modelo import UserModel
from flask_login import  logout_user, login_required



@Estudiante.route('/inicio', methods=['GET', 'POST'])
@login_required
def InicioE():
   
  return render('Estudiante/Inicio.html')

@Estudiante.route('/perfil', methods=['GET', 'POST'])
@login_required
def perfil():
  return render('Estudiante/perfil.html')

@Estudiante.route('/matricular', methods=['GET', 'POST'])
@login_required
def matricular():
   
  return render('Estudiante/Matricular.html')

@Estudiante.route('/materias', methods=['GET', 'POST'])
@login_required
def MisMaterias():
   
  return render('Estudiante/materias.html')

@Estudiante.route('/Calificaciones', methods=['GET', 'POST'])
@login_required
def Calificaciones():
  return render('Estudiante/Calificaciones.html')

@Estudiante.route('/actividades', methods=['GET', 'POST'])
@login_required
def actividades():
  return render('Estudiante/actividades.html')

@Estudiante.route('/entregas', methods=['GET', 'POST'])
@login_required
def entregas():
  return render('Estudiante/entregas.html')

@Estudiante.route('/novedades', methods=['GET', 'POST'])
@login_required
def novedades():
  return render('Estudiante/novedades.html')


@Estudiante.route('/CerrarSesion')
@login_required
def CerrarSesion():
    logout_user()
    flash('Sesion Cerrada', category="info")
    return redirect(url_for('Autentificacion.Login'))

  