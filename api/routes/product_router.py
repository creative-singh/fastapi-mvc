from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from api.database import get_db
from api.schemas.product_schemas import Product as ProductSchema, ProductCreate
from api.controllers.product_controller import get_products, create_product
from typing import List, Annotated

router = APIRouter(
  prefix="/v1/products",
  tags=["products"]
)

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/", response_model=List[ProductSchema])
def read_products(db: db_dependency):
  products = get_products(db)
  return products

@router.post("/", response_model=ProductSchema, status_code=status.HTTP_201_CREATED)
async def create_new_product(product: ProductCreate, db: db_dependency):
  try: 
    products = await create_product(db, product)
    return products
  except Exception as e:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail=f"ERROR CREATING ENTITY: {e}"
    )