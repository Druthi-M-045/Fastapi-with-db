from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from db import get_db
from repositories.user_repo import UserRepo
from schemas.user_schemas import UserSchema

from models import User

router = APIRouter()

@router.post("/signup")
def signup(user_request: UserSchema, db: Session = Depends(get_db)):
    new_user = User(email=user_request.email, password=user_request.password)
    user_repo = UserRepo(db)
    user_repo.add_user(new_user)
    return {"message": "User signup successfully"}

@router.post("/login")
def login():
    return{"message": "User logged in successfully"}