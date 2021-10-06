from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import backref, relationship, validates   
   
@dataclass
class TaskCategoriesModel(db.Model):
    
    id : int 
   
    __tablename__ = 'tasks_categories'
    
    id  = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    
    tasks = relationship('TasksModel', backref=backref('task_categories', cascade='all, delete-orphan'))
    category = db.relationship("CategoryModel", backref=backref('ct'))

    
    
   
   
   
   
   
   
   
   
   
   
   
