from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from api.database import get_db
from api.schemas.menu_item_schemas import MenuItem as MenuItemSchema, MenuItemCreate
from api.controllers.menu_item_controller import get_menu_items, create_menu_item
from typing import List, Annotated

router = APIRouter(
  prefix="/v1/menu_items",
  tags=["menu_items"]
)

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/", response_model=List[MenuItemSchema])
def read_menu_items(db: db_dependency):
  menu_items = get_menu_items(db)
  return menu_items

@router.post("/", response_model=MenuItemSchema, status_code=status.HTTP_201_CREATED)
async def create_new_menu_item(menu_item: MenuItemCreate, db: db_dependency):
  try: 
    menu_items = await create_menu_item(db, menu_item)
    return menu_items
  except Exception as e:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail=f"ERROR CREATING ENTITY: {e}"
    )