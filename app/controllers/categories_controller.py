from dataclasses import asdict
import sqlalchemy
from app.configs.database import db
from app.models.categories_model import CategoryModel
from app.models.tasks_categories import TaskCategoriesModel
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
        
        temp_name = category.name
        temp_description = category.description
        
        name = 'name' in data 
        description = 'description' in data
        
        if name :
            temp_name = data['name']
        
        if description :
            temp_description = data['description']
            
            
        CategoryModel.query.filter_by(id=id).update({'name':temp_name, 'description':temp_description})
        
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
    
    todas_categorias_query = CategoryModel.query.all()
    # query = db.session.query(AlunoModel, AulaModel).select_from(AlunoModel).join(alunos_aulas).join(AulaModel).filter(AulaModel.id == 2).all()

    query = db.session.query(TasksModel, CategoryModel).select_from(CategoryModel).join(TaskCategoriesModel).join(TasksModel).filter(TaskCategoriesModel.category_id == CategoryModel.id ).all()

    print(query)
    return jsonify('oi')
 