from . import categories_blueprint, tasks_blueprint
from flask import Blueprint

bp = Blueprint('api_bp', __name__, url_prefix='/api')

bp.register_blueprint(categories_blueprint.bp)
bp.register_blueprint(tasks_blueprint.bp)

