from sqlalchemy.orm import Session
from fastapi import HTTPException
from api.models.menu_item_price import Menu_Item_Price
from api.schemas.menu_item_price_schemas import MenuItemPriceCreate

def get_menu_item_prices(db: Session):
  return db.query(Menu_Item_Price).all()

async def create_menu_item_price(db: Session, menu_item_price: MenuItemPriceCreate):
  db_menu_item_price = Menu_Item_Price(**menu_item_price.model_dump())
  db.add(db_menu_item_price)
  db.commit()
  db.refresh(db_menu_item_price)
  return db_menu_item_price
