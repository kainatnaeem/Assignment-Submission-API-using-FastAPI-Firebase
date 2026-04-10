from pydantic import BaseModel, EmailStr

class SignUpSchema(BaseModel):
    name:str
    email:EmailStr
    password:str
    role:str   #teacher or student
    class Config: 
        json_schema_extra={
            "example": {
                "name":"kainat",
                "email": "sample@gmail.com",
                "password": "samplepassword",
                "role":"student or teacher"
            }
        }


class SigninSchema(BaseModel):
    email:str
    password:str


    class Config: 
        json_schema_extra={
            "example": {
                "email": "sample@gmail.com",
                "password": "samplepassword"
            }
        }
        