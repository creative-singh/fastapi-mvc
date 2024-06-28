from sqlalchemy.orm import Session
from api.models.product import Product
from api.schemas.product_schemas import ProductCreate

def get_products(db: Session):
  return db.query(Product).all()

async def create_product(db: Session, product: ProductCreate):
  db_product = Product(**product.model_dump())
  db.add(db_product)
  db.commit()
  db.refresh(db_product)
  return db_product