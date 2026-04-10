from fastapi import APIRouter, Form
from schemas.submission_schema import SubmissionSchema
from services.submission_service import *
router = APIRouter()

@router.post("/submitAssignment")
def submit_assignment(assignment_id : str = Form(...),
    student_id: str = Form(...),
    submission_txt: str = Form(...) ,
    grade : str = Form(...)
    ):
   
    submission_data = {
        "assignment_id": assignment_id,
        "student_id": student_id,
        "submission_txt": submission_txt,
        "grade":None
    }
    return submitAssignment(submission_data)

@router.put("/gradeAssignment/{submission_id}")
def grade_assignment(submission_id :str , grade : str = Form(...)):
    return updateGrade(submission_id, grade)