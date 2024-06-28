from sqlalchemy.orm import Session
from fastapi import HTTPException
from api.models.menu_item import Menu_Item
from api.schemas.menu_item_schemas import MenuItemCreate, MenuItemUpdate

def get_menu_items(db: Session):
  return db.query(Menu_Item).all()

async def create_menu_item(db: Session, menu_item: MenuItemCreate):
  db_menu_item = Menu_Item(**menu_item.model_dump())
  db.add(db_menu_item)
  db.commit()
  db.refresh(db_menu_item)
  return db_menu_item

async def update_menu_item(db:Session, menu_item_id: int, menu_item_update: MenuItemUpdate):
  db_menu_item = db.query(Menu_Item).filter(Menu_Item.Menu_Item_id == menu_item_id).first()
  if not db_menu_item:
    return None
  update_data = menu_item_update.model_dump(exclude_unset=True)

  for key, value in update_data.items():
    setattr(db_menu_item, key, value)

  db.commit()
  db.refresh(db_menu_item)
  return db_menu_item
   
async def delete_menu_item(db:Session, menu_item_id: int):
  db_menu_item = db.query(Menu_Item).filter(Menu_Item.Menu_Item_id == menu_item_id).first()
  if not db_menu_item:
    return False
  
  db.delete(db_menu_item)
  db.commit()
  return True