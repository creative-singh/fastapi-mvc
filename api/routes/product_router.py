from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from api.database import get_db
from api.schemas.product_schemas import Product as ProductSchema, ProductCreate, ProductUpdate
from api.controllers.product_controller import get_products, create_product, update_product, delete_product
from typing import List, Annotated

router = APIRouter(
  prefix="/v1/products",
  tags=["products"]
)

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/", response_model=List[ProductSchema], summary="Get all the Products")
def read_products(db: db_dependency):
  products = get_products(db)
  return products

@router.post("/", response_model=ProductSchema, status_code=status.HTTP_201_CREATED, summary="Create new Product Entity")
async def create_new_product(product: ProductCreate, db: db_dependency):
  try: 
    products = await create_product(db, product)
    return products
  except Exception as e:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail=f"ERROR CREATING ENTITY: {e}"
    )

@router.put("/{product_id}", response_model=ProductSchema, summary="Update Product Entity by product_id")
async def update_product_by_id(
  product_id: int,
  product: ProductUpdate,
  db: db_dependency
):
  try:
    products = await update_product(db, product_id, product)
    if products is None:
      raise HTTPException(
        status_code=404, 
        detail=f"Entity with {product_id} not found"
      )
    return products
  except Exception as e:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail=f"ERROR UPDATING ENTITY: {e}"
    )
  
@router.delete("/{product_id}", status_code=status.HTTP_202_ACCEPTED, summary="Delete Product Entity By product_id")
async def delete_product_by_id(
  product_id: int,
  db: db_dependency
):
  try:
    success = await delete_product(db, product_id)
    if not success: 
      raise HTTPException(
        status_code=404, 
        detail=f"Entity with {product_id} not found"
      )
    return {"message": "Entity Deleted"}
  except Exception as e:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail=f"ERROR DELETING ENTITY: {e}"
    )