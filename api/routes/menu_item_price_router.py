from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from api.database import get_db
from api.schemas.menu_item_price_schemas import MenuItemPrice as MenuItemPriceSchema, MenuItemPriceCreate
from api.controllers.menu_item_price_controller import get_menu_item_prices, create_menu_item_price
from typing import List, Annotated

router = APIRouter(
  prefix="/v1/menu_item_prices",
  tags=["menu_item_prices"]
)

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/", response_model=List[MenuItemPriceSchema])
def read_menu_item_prices(db: db_dependency):
  menu_item_prices = get_menu_item_prices(db)
  return menu_item_prices

@router.post("/", response_model=MenuItemPriceSchema, status_code=status.HTTP_201_CREATED)
async def create_new_menu_item_price(menu_item_price: MenuItemPriceCreate, db: db_dependency):
  try: 
    menu_item_prices = await create_menu_item_price(db, menu_item_price)
    return menu_item_prices
  except Exception as e:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail=f"ERROR CREATING ENTITY: {e}"
    )