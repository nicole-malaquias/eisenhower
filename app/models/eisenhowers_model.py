
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship


@dataclass
class EisenhowersModel(db.Model):
    
    id: int
    type:str

    __tablename__ = 'eisenhowers'
    
    id  = db.Column(db.Integer,primary_key=True)
    type = db.Column(db.String(100))
    
    task = db.relationship("TasksModel", backref="eisenhower")
   
    
    