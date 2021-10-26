from flask import Blueprint, blueprints
Administrador = Blueprint('Administrador', __name__, url_prefix='/Administrador', template_folder='templates')
from . import vistas