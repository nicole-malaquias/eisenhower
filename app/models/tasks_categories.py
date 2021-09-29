# import dataclasses
# from app.configs.database import db
# from sqlalchemy.orm import relationship

# from app.configs.database import db

   

# @dataclasses
# class TasksCategoriesModel(db.Model):
    
#     # task: 'TasksModel'
#     # categories: 'CategoryModel'
    
#     id: int
#     task_id: int
#     category_id: int

#     tasks_categories = db.Table('tasks_categories',
#     id  = db.Column(db.Integer, primary_key=True),
#     task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False),
#     category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False))
   
   
from app.configs.database import db

tasks_categories = db.Table('tasks_categories',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('task_id', db.Integer, db.ForeignKey('tasks.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id')))

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
# tasks_categories = db.Table('tasks_categories',
#     db.Column('id', db.Integer, primary_key=True),
#     db.Column('task_id', db.Integer, db.ForeignKey('tasks.id')),
#     db.Column('category_id', db.Integer, db.ForeignKey('categories.id')))
    
   
   
   
   
   
    # __tablename__ = 'tasks_categories'
    
    # id  = db.Column(db.Integer, primary_key=True)
    
    # task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    # category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
   
    