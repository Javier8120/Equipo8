from flask import Blueprint
Autentificacion = Blueprint('Autentificacion', __name__, url_prefix='/', template_folder='templates')
from . import vistas