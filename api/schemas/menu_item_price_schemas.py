from pydantic import BaseModel, Field

class MenuItemPrice(BaseModel):
  Menu_Item_id: int
  Channel: str = Field(..., max_length=50)
  Store_Cluster: str = Field(..., max_length=100)
  Price: str
  Base_Price_Yn: bool

  class Config: 
    orm_mode = True

class MenuItemPriceCreate(MenuItemPrice):
  pass