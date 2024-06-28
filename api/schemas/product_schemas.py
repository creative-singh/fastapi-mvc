from pydantic import BaseModel, Field

class Product(BaseModel):
  Product_id: int
  Name: str = Field(..., max_length=255)
  Description: str
  Taxonomy_id: int
  Country: str = Field(..., max_length=50)
  Brand: str = Field(..., max_length=50)

  class Config: 
    orm_mode = True

class ProductCreate(Product):
  pass