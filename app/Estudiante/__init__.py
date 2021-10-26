from flask import Blueprint, blueprints
Estudiante = Blueprint('Estudiante', __name__, url_prefix='/Estudiante', template_folder='templates')
from . import vistas