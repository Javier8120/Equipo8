from flask import render_template as render, flash, redirect, url_for,request

from flask_login import  logout_user, login_required
from . import Administrador
from .formularios import  *
from app.servicios import *
import sqlite3
from sqlite3 import Error

#Sesión.
Administrador.secret_key="millavesecretaa"

# Conexion con la base de datos :v
def obtener_conexion():
    try:
        conexion = sqlite3.connect('database.db')
        return conexion
    except Error:
        print(Error)

def obtener_conexion2():
    try:
        conexion2 = sqlite3.connect('GestionDeNotas.db')
        return conexion2
    except Error:
        print(Error)

#CONTINUAMOS

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

#HOLA MUNDO 2

@Administrador.route('VerUsuarios', methods = ['GET', 'POST'])
@login_required
def VerUsuarios():
    conexion2=obtener_conexion2()
    cursor = conexion2.cursor()
    cursor.execute('SELECT * FROM Users ORDER BY nombre DESC')
    db_rows = cursor.fetchall()
    print(db_rows)
    
    return render("Administrador/VerUsuarios.html", holas=db_rows)

@Administrador.route("/eliminar/<string:id>")
def eliminarU(id):
    conexion=obtener_conexion2()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Users WHERE id = {0}".format(id))
    conexion.commit()
    conexion.close()

    flash("Contacto Eliminado Satisfactoriamente")

    return redirect(url_for("Administrador.VerUsuarios"))

@Administrador.route("/editar/<id>")
def get_contacto1(id):
    conexion=obtener_conexion2()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Users WHERE id = ({})".format(id))
    db_rows = cursor.fetchall()

    return render("Administrador/EditarUsuarios.html", contactos1= db_rows[0])

@Administrador.route("/actualizar/<string:id>", methods = ["GET", "POST"])
def actualizar_contacto(id):
    #try:
    
        if request.method == 'POST':
            Rol = request.form['ROL']
            Nombre = request.form['Nombre']
            Apellido = request.form['Apellido']
            Correo = request.form['Correo']

            print(Rol,Nombre,Apellido,Correo)
            print(id)

            conexion=obtener_conexion2()
            cursor = conexion.cursor()
            #strsql="UPDATE Users SET (Rol,nombre,apliido,email) WHERE id={} VALUES ('{}','{}','{}','{}')".format(Rol,Nombre,Apellido,Correo,id) 
            cursor.execute("UPDATE Users SET Rol=?, nombre=?, apeliido=?, email=? WHERE id=?",[Rol,Nombre,Apellido,Correo,id])
            
            conexion.commit()
            conexion.close()
        
            flash("Usuario Actualizado Correctamente")
            return redirect(url_for("Administrador.VerUsuarios"))

    #except:
        #return ("error")
        
        
 

#EDICION



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



#HOLA MUNDO

@Administrador.route('/CAsignatura', methods = ['GET', 'POST'])
@login_required
def CAsignatura():

    conexion=obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM CREAR ORDER BY NombreMateria DESC')
    db_rows = cursor.fetchall()
    print(db_rows)

    if request.method == "POST":
        Nombre_Completo= request.form['Nombre_Completo']
        print(Nombre_Completo)
        conexion = obtener_conexion()
        cursor = conexion.cursor()
    
        strsql = "INSERT INTO CREAR (NombreMateria) VALUES ('{}')".format(Nombre_Completo)
        cursor.execute(strsql)
        conexion.commit()
        conexion.close()
        flash ("Materia Creada Satisfactoriamente")

    return render('Administrador/CAsignatura.html', contactos=db_rows)
    

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