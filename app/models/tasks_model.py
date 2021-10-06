
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import backref, relationship
from app.models.tasks_categories_model import TaskCategoriesModel

@dataclass
class TasksModel(db.Model):
    
    id: int
    name: str
    description: str
    duration: int
    importance: int
    urgency: int
    
    __tablename__ = 'tasks'
    
    id  = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False )
    description = db.Column(db.String(1023))
    duration = db.Column(db.Integer)
    importance = db.Column(db.Integer)
    urgency = db.Column(db.Integer)
    
    eisenhower_id = db.Column(db.Integer, db.ForeignKey('eisenhowers.id'), nullable=False)
   
    
    # category = relationship('CategoryModel')