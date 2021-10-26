from flask import render_template as render, flash, redirect, url_for
from . import Estudiante
from app.modelo import UserModel



@Estudiante.route('/inicio', methods=['GET', 'POST'])
def InicioD():
   
  return render('Estudiante/Inicio.html')

    