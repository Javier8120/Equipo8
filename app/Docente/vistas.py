from flask import render_template as render, flash, redirect, url_for
from . import Docente
from app.modelo import UserModel



@Docente.route('/inicio', methods=['GET', 'POST'])
def InicioD():
   
  return render('Docente/Inicio.html')

    

  

