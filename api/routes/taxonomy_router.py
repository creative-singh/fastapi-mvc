from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from api.database import get_db
from api.controllers.taxonomy_controller import get_taxonomies, create_taxonomy
from typing import List, Annotated
from api.schemas.taxonomy_schemas import Taxonomy as TaxonomySchema, TaxonomyCreate

router = APIRouter(
  prefix="/v1/taxonomies",
  tags=["taxonomies"]
)

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/", response_model=List[TaxonomySchema])
def read_taxonomies(db: db_dependency):
  taxonomies = get_taxonomies(db)
  return taxonomies

@router.post("/", response_model=TaxonomySchema, status_code=status.HTTP_201_CREATED)
async def create_new_taxonomy(taxonomy: TaxonomyCreate, db: db_dependency):
  try: 
    taxonomies = await create_taxonomy(db, taxonomy)
    return taxonomies
  except Exception as e:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail=f"ERROR CREATING ENTITY: {e}"
    )
