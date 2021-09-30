import sqlalchemy
from app.configs.database import db
from app.models.categories_model import CategoryModel
from app.models.eisenhowers_model import EisenhowersModel
from app.models.tasks_model import TasksModel
from flask import jsonify, request

def insert_task():

    data = request.json
    urgency = data['urgency']
    importance = data['importance']
    
    if 1 <= urgency <= 2 and 1<=  importance <= 2 :
        
        try:
            
            type_eisenhowers = check_eisenhowers(urgency, importance)
            eise = EisenhowersModel(type=type_eisenhowers)
            
            db.session.add(eise)
            db.session.commit()
            
            task = TasksModel(
                name = data['name'],
                description = data['description'],
                duration = data['duration'],
                urgency= urgency,
                importance= importance,
                eisenhower_id = eise.id)         
            
            db.session.add(task)
            db.session.commit()
            
            categories = data['categories']
            check_category(categories)
                                
            eisenhower =  EisenhowersModel.query.get(task.eisenhower_id)

            r = {
                "id": task.id,"name":task.name, "description": task.description, "duration": task.duration, "eisenhower_classification": eisenhower.type,
                "categories": data['categories']
            }
  
            return jsonify(r),201

            
        except sqlalchemy.exc.IntegrityError:
        
            return {"msg":"Tasks already exists!"},409
        
    return {
        "error":{"valid_options":{
                    "importance":[1,2],
                     "urgency":[1,2]},
                 
            },
        "recieved_options":{
            "importance":importance,
            "urgency": urgency
        }
    },404      
    
def update_task(id: int): 
    
    data = request.json
    task = TasksModel.query.get(id)

    validar_keys = TasksModel.validate_keys(data)
    
    if validar_keys :
        
        has_urgency = 'urgency' in data
        has_importance = 'importance' in data
        has_categories = 'categories' in data
        
        temp_urgency = task.urgency
        temp_importane = task.importance
        
        if has_urgency :
            temp_urgency = data['urgency']
        
        if has_importance :
            temp_importane = data['importance']
            
        
        new_eisenhower = check_eisenhowers(temp_urgency,temp_importane)
        update_eisenhower(task.eisenhower_id, new_eisenhower)
        
        if has_categories:
            check_category(data['categories'])
            
        TasksModel.query.filter_by(id=id).update(data)
        db.session.commit()
        task = TasksModel.query.get(id)
        
        r = {
                "id": task.id,"name":task.name, "description": task.description, "duration": task.duration, "eisenhower_classification": new_eisenhower,
                "categories": task.categories
            }
    
        return jsonify(r),201
    
    return {"msg":"Field to be updated is invalid"}
    
def delete_task(id: int):
    
    ...

def check_eisenhowers(urgency,importance):
    
    if importance == 1 and urgency == 1:
        return 'Do It First'
    
    if importance == 1 and urgency == 2:
        return 'Delegate It'
    
    if importance == 2 and urgency == 1:
        return 'Schedule It'
    
    if importance == 2 and urgency == 2:
        return 'Delete It'

def update_eisenhower(id,new_type):
    insert = {"type": new_type}
    EisenhowersModel.query.filter_by(id=id).update(insert)
    
def check_category(categories):
    for i in categories :
        
        category = CategoryModel.query.filter_by(name = i['name'])
            
        if category is None :
            
            category = CategoryModel(name=i['name'], description="")
            
            db.session.add(category)
            
            db.session.commit()
    