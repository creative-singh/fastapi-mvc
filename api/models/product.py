from sqlalchemy import Column, String, Integer, Text, ForeignKey
from api.database import Base
from sqlalchemy.orm import relationship

class Product(Base):
  __tablename__ = 'product'

  Product_id = Column(Integer, primary_key=True, index=True)
  Name = Column(String(255), unique=True, index=True)
  Description = Column(Text)
  Taxonomy_id = Column(Integer, ForeignKey('taxonomy.Taxonomy_id'))
  Country = Column(String(50))
  Brand = Column(String(50))

  taxonomy = relationship("Taxonomy", back_populates="product")
  menu_item = relationship("Menu_Item", back_populates="product")
