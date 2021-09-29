from flask import Blueprint
from app.controllers.categories_controller import insert_categories,update_categories,delete_categories


bp = Blueprint('categories_bp', __name__, url_prefix='/category')


bp.post('/')(insert_categories)
bp.patch('/<int:id>')(update_categories)
bp.delete('/<int:id>')(delete_categories)






