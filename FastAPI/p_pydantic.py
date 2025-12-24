from fastapi import FastAPI
from enum import IntEnum #importing IntEnum used for defining enumeration of integer values
from typing import Optional
from pydantic import BaseModel, Field  #importing BaseModel to create data models
#importing Field to add extra validation and metadata to model fields

api = FastAPI()

class PriorityLevel(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1

class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length=1, max_length=100 , description='name of the todo ')  # Field with validation for name
    todo_dscription: str = Field(..., description= 'description of the todo' ) # Field with validation for description
    priority: PriorityLevel = Field(PriorityLevel.LOW, description='priority level of the todo')  # Field with default value and description

class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):  #not as request body but as response model
    todo_id: int = Field(..., description='unique identifier for the todo')  # Field for todo_id with description



class TodoUpdate(BaseModel):
    todo_name: Optional[str] = Field(None, min_length=1, max_length=100, description='name of the todo')  # Optional field for name
    todo_description: Optional[str] = Field(None, description='description of the todo')  # Optional field for description
    priority: Optional[PriorityLevel] = Field(None, description='priority level of the todo')  # Optional field for priority


all_todos = [
    { to