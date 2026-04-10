from pydantic import BaseModel
from datetime import date

class AssignmentSchema(BaseModel):
    title:str
    description:str
    duedate:date