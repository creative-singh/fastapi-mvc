from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
  User_id: int
  Name: str = Field(..., max_length=100)
  Email: EmailStr
  Password: str = Field(..., min_length=8)

  class Config: 
    orm_mode = True