from sqlalchemy import Column, Boolean, Integer, String, ForeignKey
from api.database import Base
from sqlalchemy.orm import relationship

class Menu_Item_Price(Base):
  __tablename__ = 'menu_item_price'

  Menu_Item_id = Column(Integer, primary_key=True, index=True)
  Channel = Column(String(50))
  Store_Cluster = Column(String(100))
  Price = Column(String(20))
  Base_Price_Yn = Column(Boolean)

  # menu_item = relationship("Menu_Item", back_populates="menu_item_price")