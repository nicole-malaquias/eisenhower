
from sqlalchemy.orm import backref, relationship
from app.models.tasks_categories_model import TaskCategoriesModel

from app.configs.database import db
from dataclasses import dataclass

@dataclass
class CategoryModel(db.Model):
   
    id: int
    name: str
    description : str
    task: str
    
    __tablename__ = 'categories'
    
    id  = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False , unique=True)
    description = db.Column(db.String(255))

    task = relationship('TasksModel',secondary='tasks_categories', backref=db.backref('category'),viewonly=True)

    
    
    
    
    
