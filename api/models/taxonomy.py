from sqlalchemy import Column, String, Text, Integer
from api.database import Base
from sqlalchemy.orm import relationship

class Taxonomy(Base):
  __tablename__ = 'taxonomy'

  Taxonomy_id = Column(Integer, primary_key=True, index=True)
  Name = Column(String(255), unique=True, index=True)
  Description = Column(Text)
  Channel = Column(String(50))
  Category = Column(String(50))

  product = relationship("Product", back_populates="taxonomy")