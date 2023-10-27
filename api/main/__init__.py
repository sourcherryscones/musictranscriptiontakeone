from flask import Blueprint

bp = Blueprint('main', __name__)

from api.main import routes