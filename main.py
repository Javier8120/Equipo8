from flask import render_template as render, flash, send_from_directory
from app import create_app  # Funcion create_app que esta en Init
from app.migrate import init_db   #Funcion Init que esta en migrate 

app = create_app()

# Errores.... 
@app.errorhandler(404)
def not_found(error):
    return render('errors/error404.html', error=error)
@app.errorhandler(500)
def internal_server_error(error):
    return render('errors/error500.html')



# Actualiza la base de datos si genero cambios en alguna columna :v
@app.route('/CrearTablas')
def CrearTablas():
    init_db()
    return "Base de datos creada correctamente """



