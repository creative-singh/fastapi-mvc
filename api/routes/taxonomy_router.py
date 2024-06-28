from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from api.database import get_db
from api.controllers.taxonomy_controller import get_taxonomies, create_taxonomy, update_taxonomy, delete_taxonomy
from typing import List, Annotated
from api.schemas.taxonomy_schemas import Taxonomy as TaxonomySchema, TaxonomyCreate, TaxonomyUpdate

router = APIRouter(
  prefix="/v1/taxonomies",
  tags=["taxonomies"]
)

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/", response_model=List[TaxonomySchema], summary="Get all the Taxonomies")
def read_taxonomies(db: db_dependency):
  taxonomies = get_taxonomies(db)
  return taxonomies

@router.post("/", response_model=TaxonomySchema, status_code=status.HTTP_201_CREATED, summary="Create new Taxonomy Entity")
async def create_new_taxonomy(taxonomy: TaxonomyCreate, db: db_dependency):
  try: 
    taxonomies = await create_taxonomy(db, taxonomy)
    return taxonomies
  except Exception as e:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail=f"ERROR CREATING ENTITY: {e}"
    )

@router.put("/{taxonomy_id}", response_model=TaxonomySchema, summary="Update Taxonomy Entity By taxonomy_id")
async def update_taxonomy_by_id(
  taxonomy_id: int, 
  taxonomy: TaxonomyUpdate, 
  db: db_dependency
):
  try:
    taxonomies = await update_taxonomy(db, taxonomy_id, taxonomy)
    if taxonomies is None:
      raise HTTPException(
        status_code=404, 
        detail=f"Entity with {taxonomy_id} not found"
      )
    return taxonomies
  except Exception as e:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail=f"ERROR UPDATING ENTITY: {e}"
    )
  
@router.delete("/{taxonomy_id}", status_code=status.HTTP_202_ACCEPTED, summary="Delete Taxonomy Entity By taxonomy_id")
async def delete_taxonomy_by_id(
  taxonomy_id: int, 
  db: db_dependency
):
  try:
    success = await delete_taxonomy(db, taxonomy_id)
    if not success:
      raise HTTPException(
          status_code=404, 
          detail=f"Entity with {taxonomy_id} not found"
        )
    return {"message": "Entity Deleted"}
  except Exception as e:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail=f"ERROR DELETING ENTITY: {e}"
    )
  