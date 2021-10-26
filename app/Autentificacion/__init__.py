from flask import Blueprint, blueprints


Autentificacion = Blueprint('Autentificacion', __name__, url_prefix='/', template_folder='templates')
from . import vistas