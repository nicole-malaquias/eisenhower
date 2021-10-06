from flask import Flask 
from flask_migrate import Migrate  

def init_app(app: Flask):
    
    from app.models.categories_model import CategoryModel
    from app.models.eisenhowers_model import EisenhowersModel
    from app.models.tasks_model import TasksModel
    from app.models.tasks_categories_model import TaskCategoriesModel
    
    Migrate(app, app.db)
    
