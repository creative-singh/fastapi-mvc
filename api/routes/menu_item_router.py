from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from api.database import get_db
from api.schemas.menu_item_schemas import MenuItem as MenuItemSchema, MenuItemCreate, MenuItemUpdate
from api.controllers.menu_item_controller import get_menu_items, create_menu_item, update_menu_item, delete_menu_item
from typing import List, Annotated

router = APIRouter(
  prefix="/v1/menu_items",
  tags=["menu_items"]
)

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/", response_model=List[MenuItemSchema], summary="Get all the Menu Item")
def read_menu_items(db: db_dependency):
  menu_items = get_menu_items(db)
  return menu_items

@router.post("/", response_model=MenuItemSchema, status_code=status.HTTP_201_CREATED, summary="Create new Menu Item Entity")
async def create_new_menu_item(menu_item: MenuItemCreate, db: db_dependency):
  try: 
    menu_items = await create_menu_item(db, menu_item)
    return menu_items
  except Exception as e:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail=f"ERROR CREATING ENTITY: {e}"
    )
  
@router.put("/{menu_item_id}", response_model=MenuItemSchema, summary="Update Menu Item Entity by menu_item_id")
async def update_menu_items(
  menu_item_id: int,
  menu_item_update: MenuItemUpdate,
  db: db_dependency
):
  try:
    menu_items = await update_menu_item(db, menu_item_id, menu_item_update)
    if menu_items is None:
      raise HTTPException(
        status_code=404, 
        detail=f"Entity with {menu_item_id} not found"
      )
    return menu_items
  except Exception as e:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail=f"ERROR UPDATING ENTITY: {e}"
    )

@router.delete("/{menu_item_id}", status_code=status.HTTP_202_ACCEPTED, summary="Delete Menu Item Entity by menu_item_id")
async def delete_menu_items(
  menu_item_id: int,
  db: db_dependency
): 
  try:
    success = await delete_menu_item(db, menu_item_id)
    if not success:
      raise HTTPException(
        status_code=404,
        detail=f"Entity with {menu_item_id} not found"
      )
    return {"message": "Entity Deleted"}
  except Exception as e:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail=f"ERROR DELETING ENTITY: {e}"
    )

