from sqlalchemy.orm import Session
from api.models.product import Product
from api.schemas.product_schemas import ProductCreate, ProductUpdate

def get_products(db: Session):
  return db.query(Product).all()

async def create_product(db: Session, product: ProductCreate):
  db_product = Product(**product.model_dump())
  db.add(db_product)
  db.commit()
  db.refresh(db_product)
  return db_product

async def update_product(
    db: Session,
    product_id: int,
    product_update: ProductUpdate
  ):
  db_product = db.query(Product).filter(Product.Product_id == product_id).first()
  if not db_product: 
    return None
  
  update_data = product_update.model_dump(exclude_unset=True)

  for key, value in update_data.items():
    setattr(db_product, key, value)

  db.commit()
  db.refresh(db_product)
  return db_product
  
async def delete_product(db: Session, product_id: int):
  db_product = db.query(Product).filter(Product.Product_id == product_id).first()
  if not db_product: 
    return False
  
  db.delete(db_product)
  db.commit()
  return True