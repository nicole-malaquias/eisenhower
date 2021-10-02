
from app.models.tasks_categories import TaskCategoriesModel

from app.configs.database import db
from dataclasses import dataclass



@dataclass
class CategoryModel(db.Model):

    id: int
    name: str
    description : str

    __tablename__ = 'categories'
    
    id  = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False , unique=True)
    description = db.Column(db.String(100))


    
    
    
    
