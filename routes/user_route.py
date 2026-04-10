from fastapi import APIRouter
from schemas.user_schema import SignUpSchema, SigninSchema
from services.user_service import *

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def signup(data: SignUpSchema):
    return  register_user(data)

@router.post("/login")  
def login(data:SigninSchema):
    return signin_user(data) 