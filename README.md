# Gestion de notas :V

# Instalar Python - https://www.python.org/  - instalar pip -> se selecciona en la instalación de python.
Python 3.9.7
pip 21.3

# Opcional - Descargar SQL-LITE - https://www.sqlite.org/index.html

# Instalar node - https://nodejs.org/es/
node v14.15.1
npm 6.14.11


# Instalar el ambiente virtual
cd ../../
pip install virtualenv==20.2.2
virtualenv venv

# Activar el entorno virtual en Windows
./Entorno/scripts/activate

# node-modules - carpeta static
cd app/static
npm init
npm install sweetalert2


# Agregamos las dependencias al archivo de requerimientos y ejecutamos el comandos - archivo en la raíz del proyecto 
cd ../../
pip install -r requirements.txt

# Correr al app en desarrollo
set FLASK_APP=main.py
set FLASK_DEBUG=1
set FLASK_ENV=development
flask run
# Para PowerShell
$env:FLASK_APP='main.py'
$env:FLASK_DEBUG=1
$env:FLASK_ENV='development'

# Usuario Base
    - app/migrate.py
    username: Javier
    pwd: Adm1n**123
    
# NOTA (OPCIONAL) Reinicar (Base de datos) y configuración (user Default) 
    - Configurar usuario por defecto en app/migrate.py
ip:port/database


