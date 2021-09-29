from flask import Blueprint
from app.controllers.tasks_controller import insert_task, update_task,delete_task


bp = Blueprint('tasks_bp', __name__, url_prefix='/task')

bp.get('/')(insert_task)
bp.post('/')(insert_task)
bp.get('/<int:id>')(update_task)
bp.delete('/<int:id>')(delete_task)


