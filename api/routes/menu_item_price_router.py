from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from api.database import get_db
from api.schemas.menu_item_price_schemas import MenuItemPrice as MenuItemPriceSchema, MenuItemPriceCreate, MenuItemPriceUpdate
from api.controllers.menu_item_price_controller import get_menu_item_prices, create_menu_item_price, update_menu_item_price, delete_menu_item_price
from typing import List, Annotated

router = APIRouter(
  prefix="/v1/menu_item_prices",
  tags=["menu_item_prices"]
)

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/", response_model=List[MenuItemPriceSchema], summary="Get all the Menu Item Price")
def read_menu_item_prices(db: db_dependency):
  menu_item_prices = get_menu_item_prices(db)
  return menu_item_prices

@router.post("/", response_model=MenuItemPriceSchema, status_code=status.HTTP_201_CREATED, summary="Create new Menu Item Price Entity")
async def create_new_menu_item_price(menu_item_price: MenuItemPriceCreate, db: db_dependency):
  try: 
    menu_item_prices = await create_menu_item_price(db, menu_item_price)
    return menu_item_prices
  except Exception as e:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail=f"ERROR CREATING ENTITY: {e}"
    )
  
@router.put("/{menu_item_price_id}", response_model=MenuItemPriceSchema, summary="Update Menu Item Price Entity By menu_item_id")
async def update_menu_items(
  menu_item_id: int,
  menu_item_update: MenuItemPriceUpdate,
  db: db_dependency
):
  try:
    menu_items = await update_menu_item_price(db, menu_item_id, menu_item_update)
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

@router.delete("/{menu_item_id}", status_code=status.HTTP_202_ACCEPTED, summary="Delete Menu Item Price Entity By menu_item_id")
async def delete_menu_items_price(
  menu_item_id: int,
  db: db_dependency
): 
  try:
    success = await delete_menu_item_price(db, menu_item_id)
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

