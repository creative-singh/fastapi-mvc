from fastapi import FastAPI
from api.database import engine

# Routes
from api.routes.user_router import router as user_router
from api.routes.taxonomy_router import router as taxonomy_router
from api.routes.product_router import router as product_router
from api.routes.menu_item_router import router as menu_item_router
from api.routes.menu_item_price_router import router as menu_item_price_router

# Models
from api.models.user import Base as UserBase
from api.models.taxonomy import Base as TaxonomyBase
from api.models.product import Base as ProductBase
from api.models.menu_item import Base as MenuItemBase
from api.models.menu_item_price import Base as MenuItemPriceBase

# Create all tables
UserBase.metadata.create_all(bind=engine)
TaxonomyBase.metadata.create_all(bind=engine)
ProductBase.metadata.create_all(bind=engine)
MenuItemBase.metadata.create_all(bind=engine)
MenuItemPriceBase.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)
app.include_router(taxonomy_router)
app.include_router(product_router)
app.include_router(menu_item_router)
app.include_router(menu_item_price_router)