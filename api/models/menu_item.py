from sqlalchemy import Column, String, Text, Integer, ForeignKey
from api.database import Base
from sqlalchemy.orm import relationship

class Menu_Item(Base):
  __tablename__ = 'menu_item'

  Menu_Item_id =  Column(Integer, primary_key=True, index=True)
  Name = Column(String(255), unique=True, index=True)
  Description = Column(Text)
  Product_id = Column(Integer, ForeignKey('product.Product_id'))
  
  product = relationship("Product", back_populates="menu_item")
  # menu_item_price = relationship("Menu_Item_Price", back_populates="menu_item")