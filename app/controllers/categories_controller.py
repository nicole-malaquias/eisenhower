from dataclasses import asdict
import sqlalchemy
from app.configs.database import db
from app.models.categories_model import CategoryModel
from app.models.tasks_categories_model import TaskCategoriesModel
from flask import jsonify, request

from app.models.tasks_model import TasksModel


def insert_categories(): 
    
    data = request.json

    try:
        category = CategoryModel(**data)
    
        db.session.add(category)
        db.session.commit()
        return  jsonify(category),201
    
    except sqlalchemy.exc.IntegrityError:
        
        return {"msg":"Category already exists!"},409
            
def update_categories(id: int):
        
        category = CategoryModel.query.get(id)
        data = request.json
            
        CategoryModel.query.filter_by(id=id).update(data)
        
        db.session.commit()
        category = CategoryModel.query.get(id)
        
        if category is not None:
            
            return jsonify(category),200
        
        return {"msg":"category not found!"}
     
def delete_categories(id:int):
   
   
    subquery = CategoryModel.query.get(id)
    if subquery is None:
         return {"msg":"category not found!"}
     
     
    db.session.delete(subquery)
    db.session.commit()
    return "",204
    
def get_all_categories():
    
    categories = CategoryModel.query.all()
    return jsonify(categories),200
   
 
 
 
 