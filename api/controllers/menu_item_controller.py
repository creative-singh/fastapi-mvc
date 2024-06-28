from sqlalchemy.orm import Session
from fastapi import HTTPException
from api.models.menu_item import Menu_Item
from api.schemas.menu_item_schemas import MenuItemCreate

def get_menu_items(db: Session):
  return db.query(Menu_Item).all()

async def create_menu_item(db: Session, menu_item: MenuItemCreate):
  db_menu_item = Menu_Item(**menu_item.model_dump())
  db.add(db_menu_item)
  db.commit()
  db.refresh(db_menu_item)
  return db_menu_item