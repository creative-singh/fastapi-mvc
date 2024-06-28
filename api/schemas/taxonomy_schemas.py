from pydantic import BaseModel, Field

class Taxonomy(BaseModel):
  Taxonomy_id: int
  Name: str = Field(..., min_length=1, max_length=255)
  Description: str
  Channel: str = Field(..., max_length=50)
  Category: str = Field(..., max_length=50)

  class Config: 
    orm_mode = True

class TaxonomyCreate(Taxonomy):
  pass