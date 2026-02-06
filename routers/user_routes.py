from fastapi import APIRouter

router = APIRouter()

@router.post("/users")
def signup():
    return {"message": "User signup successfully"}
