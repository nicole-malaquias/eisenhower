
from dataclasses import asdict
from app.configs.database import db
from app.exc.FieldInvalidErrors import FieldError
from app.exc.ImportanceErrors import ImportanceErrors
from app.models.categories_model import CategoryModel
from app.models.eisenhowers_model import EisenhowersModel
from app.models.tasks_categories import TaskCategoriesModel
from app.models.tasks_model import TasksModel
from flask import jsonify, request


def insert_task():
  
    data = request.json
   
    check_field = check_field_to_insert(data)
    eisenhower = check_eisenhower(data['urgency'],data['importance'])
    id_eisenhower = search_id_eisenhower(eisenhower)
   
    
    try:
       
        if check_field :
            
            if len(eisenhower) == 0:
               
                raise  ImportanceErrors(data)
            
            check_categories_exists(data)
            
            
            task = TasksModel(
                name=data['name'],
                description=data['description'],
                duration=data['duration'],
                importance=data['importance'],
                urgency=data['urgency'],
                eisenhower_id = id_eisenhower,
            )
            db.session.add(task)
            db.session.commit()
            
            create_categories_task(task.id,data)
            
            response = create_response_insert(task.id)
       
            return jsonify(response),201

        raise FieldError(data)
    
    
    except ImportanceErrors as err:
        
        return jsonify( err.message ),404
   
    except FieldError as err:
        return jsonify( err.message ),422
    
def update_task():
    
    ...




















def delete_task(id:int):
    
    subquery = TasksModel.query.get(id)
    
    if subquery is None:
         return {"msg":"category not found!"}
     
     
    db.session.delete(subquery)
    db.session.commit()
    return "",204
    
def check_eisenhower(urgency,importance):
    
    if importance == 1 and urgency == 1:
        return 'Do It First'
    
    if importance == 1 and urgency == 2:
        return 'Delegate It'
    
    if importance == 2 and urgency == 1:
        return 'Schedule It'
    
    if importance == 2 and urgency == 2:
        return 'Delete It'
    
    return ''

def search_id_eisenhower(name):
  
    eise = EisenhowersModel.query.filter_by(type = name).all()[0]
    return eise.id
    
def check_field_to_insert(data):
    
    field = ['categories','name','description','duration','importance','urgency']
    quantity_input = len([input for input in data if input.lower() in field])
  
    if quantity_input == 6 :
        return True 
    return False 

def check_categories_exists(data):
    
    categories = data['categories']
    
    query_categories = CategoryModel.query.all()
    list_categories_exists = [item.name for item in query_categories]
    
    for category in categories:
        
        if category['name'] not in list_categories_exists :
           
            new_category = CategoryModel(name= category['name'] ,description="")
            db.session.add(new_category)
            db.session.commit()

def create_categories_task(id,data):
    
    categories = data['categories']
    
    for category in categories :
        
        name_category = category['name']
        id_category = CategoryModel.query.filter_by(name = name_category ).all()[0].id

        new_task_category = TaskCategoriesModel(task_id = id, category_id = id_category)
        db.session.add(new_task_category)
        db.session.commit()
        
        print(new_task_category)
   
def create_response_insert(id):
    
    objecto = TasksModel.query.get(id)
    
    response = asdict(objecto)
    response['eisenhower'] = objecto.eisenhower.type
    del response['eisenhower_id']
    
    query_categories =  db.session.query(CategoryModel.name).filter(TaskCategoriesModel.task_id == TasksModel.id).filter(TaskCategoriesModel.category_id == CategoryModel.id).filter(TasksModel.id == id).all() 
    covert = [dict(x) for x in query_categories]
  
  
    response['categories'] = covert
    
    return response























