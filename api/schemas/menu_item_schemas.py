from pydantic import BaseModel, Field
from typing import Optional

class MenuItem(BaseModel):
  Menu_Item_id: int
  Name: str = Field(..., max_length=255)
  Description: str
  Product_id: int

  class Config: 
    orm_mode = True

class MenuItemCreate(MenuItem):
  pass

class MenuItemUpdate(BaseModel):
  Name: Optional[str]
  Description: Optional[str]
  Product_id: Optional[int]