from pydantic import BaseModel
from typing import Optional


class SubmissionSchema(BaseModel):
    assignment_id:str
    student_id:str
    submission_txt:str
    grade:Optional[str] = None