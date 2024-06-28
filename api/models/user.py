from sqlalchemy import Column, String, Boolean, Integer
from api.database import Base

class User(Base):
  __tablename__ = 'users'

  User_id = Column(Integer, primary_key=True, index=True)
  Name = Column(String, index=True)
  Email = Column(String, unique=True, index=True)
  Password = Column(String)