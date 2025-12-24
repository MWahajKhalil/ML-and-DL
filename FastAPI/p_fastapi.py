from fastapi import FastAPI

api = FastAPI()

all_todos = [
    
        {'todo_id' :1 , 'todo_name' : 'Sports', 'todo_description': 'go to play cricket'},
        {'todo_id' :2 , 'todo_name' : 'School', 'todo_description': 'go to Univeristy'},
        {'todo_id' :3 , 'todo_name' : 'Shopping', 'todo_description': 'go to Shopping'},
        {'todo_id' :4 , 'todo_name' : 'Studying', 'todo_description': 'go to Study '},
        {'todo_id' :5 , 'todo_name' : 'Pray', 'todo_description': 'go to Mosque'},

]


@api.get ('/')   #this is an endpoint
def index():
    return {"message": "My name is Wahaj "
    "I am learning FastAPI"}

#to return specific todo based on todo_id
#For example: localhost:8000/todos/2. and it will return todo with id 2 (school)
@api.get('/todos/{todo_id}')  #teated as an inifomration that we are getting from user (endpoint with path parameter)
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return {'The resulted to is ': todo}
    return {'message': 'Todo not found'}

            




#to return all todos,we have to remove this endpoint still trworks because of query parameter(see below)
# @api.get('/todos')  #endpoint to get all todos
# def get_all_todos():
#     return all_todos






#query parameter example
@api.get('/todos')                               #endpoint to get todo by query parameter
def get_todo_by_query(first_n: int = None):     #if no todo_id is provided, it will be None
    if first_n:                                  #if todo_id is provided                   #loop through all todos
        return all_todos[:first_n]              #return first n todos means
    
    else:
        return all_todos                        #return all todos

#the difference between path parameter and query parameter is that 
#path parameter is part of the URL and query parameter is after the ? in the URL
#path parameter is required and query parameter is optional
# for example:
#path parameter: localhost:8000/todos/2
#query parameter: localhost:8000/todos/?todo_id=2











#post request to create a new todo
@api.post('/todos')  #endpoint to create a new todo 
def create_todo(todo: dict):   #todo is a dictionary
    new_todo_id = max(todo['todo_id'] for todo in all_todos) + 1 #get the max todo_id and add 1 to it

    new_todo = {
        'todo_id': new_todo_id,
        'todo_name': todo['todo_name'],
        'todo_description': todo['todo_description'] #get todo_name and todo_description from the request body
    }

    all_todos.append(new_todo)  #append the new todo to the all_todos list
    return {'message': 'Todo created successfully', 'todo': new_todo}




#put request to update a todo
@api.put('/todos/{todo_id}')  #endpoint to update a todo
def update_todo(todo_id: int, updated_todo: dict):  #updated_todo is a dictionary
    for todo in all_todos:
        if todo['todo_id']== todo_id:
            todo['todo_name'] =  updated_todo['todo_name']  #get the todo_name from the request body, if not present, keep the old value
            todo['todo_description'] = updated_todo['todo_description']  #get the todo_description from the request body, if not present, keep the old value
            return {'message': 'Todo updated successfully', 'todo': todo}
    return {'message': 'Todo not found'}




# #delete request to delete a todo
# @api.delete('/todos/{todo_id}')  #endpoint to delete a todo
# def delete_todo(todo_id: int):
#     for todo in all_todos:
#         if todo['todo_id'] == todo_id:
#             all_todos.remove(todo)
#             return {'message': 'Todo deleted successfully'}
#     return {'message': 'Todo not found'}    


@api.delete('/todos/{todo_id}')
 #endpoint to delete all todos
def delete_todo(todo_id: int):
     for index, todo in enumerate(all_todos):
         if todo['todo_id'] == todo_id:
             deleted_todo = all_todos.pop(index)
             return {'message': 'Todo deleted successfully', 'todo': deleted_todo}
     return {'message': 'Todo not found'}   


#both delete endpoints are same, the second one also returns the deleted todo
#in 2nd endpoint, we are using enumerate to get the index of the todo to be deleted
#enumerate returns both index and value of the list item