from flask import Blueprint, blueprints
Docente = Blueprint('Docente', __name__, url_prefix='/Docente', template_folder='templates')
from . import vistas