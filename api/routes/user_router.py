from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database import get_db
from api.schemas.user_schemas import User as UserSchema
from api.controllers.user_controller import get_users
from typing import List

router = APIRouter()

@router.get("/", response_model=dict, summary="API to check Server Health", tags=["Health"])
async def health_check():
  return {"status": "Healthy"}

@router.get("/users", response_model=List[UserSchema], summary="Sample API intial setup with Users", tags=["Sample Users"])
async def read_users(db: Session = Depends(get_db)):
  users = get_users(db)
  return users

  