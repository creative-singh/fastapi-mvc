from sqlalchemy.orm import Session
from fastapi import HTTPException
from api.models.user import User

def get_users(db: Session):
  return db.query(User).all()