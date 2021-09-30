from app.controllers.tasks_controller import (delete_task, insert_task,
                                              update_task)
from flask import Blueprint

bp = Blueprint('tasks_bp', __name__, url_prefix='/task')

bp.get('/')(insert_task)
bp.post('/')(insert_task)
bp.patch('/<int:id>')(update_task)
bp.delete('/<int:id>')(delete_task)


