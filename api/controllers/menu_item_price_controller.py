from sqlalchemy.orm import Session
from fastapi import HTTPException
from api.models.menu_item_price import Menu_Item_Price
from api.schemas.menu_item_price_schemas import MenuItemPriceCreate, MenuItemPriceUpdate

def get_menu_item_prices(db: Session):
  return db.query(Menu_Item_Price).all()

async def create_menu_item_price(db: Session, menu_item_price: MenuItemPriceCreate):
  db_menu_item_price = Menu_Item_Price(**menu_item_price.model_dump())
  db.add(db_menu_item_price)
  db.commit()
  db.refresh(db_menu_item_price)
  return db_menu_item_price

async def update_menu_item_price(db:Session, menu_item_id: int, menu_item_update: MenuItemPriceUpdate):
  db_menu_item_price = db.query(Menu_Item_Price).filter(Menu_Item_Price.Menu_Item_id == menu_item_id).first()
  
  if not db_menu_item_price:
    return None
  
  update_data = menu_item_update.model_dump(exclude_unset=True)

  for key, value in update_data.items():
    setattr(db_menu_item_price, key, value)

  db.commit()
  db.refresh(db_menu_item_price)
  return db_menu_item_price

async def delete_menu_item_price(db: Session, menu_item_price_id: int):
  db_menu_item_price = db.query(Menu_Item_Price).filter(Menu_Item_Price.Menu_Item_id == menu_item_price_id).first()
  if not db_menu_item_price:
    return False
  
  db.delete(db_menu_item_price)
  db.commit()
  return True