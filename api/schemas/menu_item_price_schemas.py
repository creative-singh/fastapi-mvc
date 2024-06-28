from pydantic import BaseModel, Field, field_validator
from typing import Optional

class MenuItemPrice(BaseModel):
  Menu_Item_id: int
  Channel: str = Field(..., max_length=50)
  Store_Cluster: str = Field(..., max_length=100)
  Price: str
  Base_Price_Yn: bool

  # @field_validator('Price')
  # def position_price(cls, val):
  #   if float(val) <= 0:
  #     raise ValueError('Price must be greater than 0')
  #   return val

  class Config: 
    orm_mode = True

class MenuItemPriceCreate(MenuItemPrice):
  pass

class MenuItemPriceUpdate(BaseModel):
  Channel: Optional[str]
  Store_Cluster: Optional[str]
  Price: Optional[str]
  Base_Price_Yn: Optional[bool]