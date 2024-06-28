from sqlalchemy.orm import Session
from api.models.taxonomy import Taxonomy
from api.schemas.taxonomy_schemas import TaxonomyCreate

def get_taxonomies(db: Session):
  return db.query(Taxonomy).all()

async def create_taxonomy(db: Session, taxonomy: TaxonomyCreate):
  db_taxonomy = Taxonomy(**taxonomy.model_dump())
  db.add(db_taxonomy)
  db.commit()
  db.refresh(db_taxonomy)
  return db_taxonomy