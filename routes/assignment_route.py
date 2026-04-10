from fastapi import APIRouter, UploadFile, File, Form
from schemas.assignment_schema import AssignmentSchema
from services.assignment_service import *
router = APIRouter()

@router.post('/createAssignment')
def create_assignment(
    title: str = Form(...),
    description: str = Form(...),
    duedate: str = Form(...)
):
    assignment_data = {
        "title": title,
        "description": description,
        "duedate": duedate
    }
    return createAssignment(assignment_data)

@router.post("/get")
def get_assignments():
    return getAssignments()