from pydantic import BaseModel

class Userschemas(BaseModel):
    email: str
    password: str
