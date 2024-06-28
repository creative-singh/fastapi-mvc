from pydantic import BaseModel, Field

class MenuItem(BaseModel):
  Menu_Item_id: int
  Name: str = Field(..., max_length=255)
  Description: str
  Product_id: int

  class Config: 
    orm_mode = True

class MenuItemCreate(MenuItem):
  pass