from sqlalchemy.orm import Session
from api.models.taxonomy import Taxonomy
from api.schemas.taxonomy_schemas import TaxonomyCreate, TaxonomyUpdate

def get_taxonomies(db: Session):
  return db.query(Taxonomy).all()

async def create_taxonomy(db: Session, taxonomy: TaxonomyCreate):
  db_taxonomy = Taxonomy(**taxonomy.model_dump())
  db.add(db_taxonomy)
  db.commit()
  db.refresh(db_taxonomy)
  return db_taxonomy

async def update_taxonomy(
    db: Session, 
    taxonomy_id: int,
    taxonomy_update: TaxonomyUpdate
  ):
  db_taxonomy = db.query(Taxonomy).filter(Taxonomy.Taxonomy_id == taxonomy_id).first()
  if not db_taxonomy:
    return None
  
  update_data = taxonomy_update.model_dump(exclude_unset=True)

  for key, value in update_data.items():
    setattr(db_taxonomy, key, value)

  db.commit()
  db.refresh(db_taxonomy)
  return db_taxonomy

async def delete_taxonomy(db: Session, taxonomy_id: int):
  db_taxonomy = db.query(Taxonomy).filter(Taxonomy.Taxonomy_id == taxonomy_id).first()
  if not db_taxonomy:
    return False
  
  db.delete(db_taxonomy)
  db.commit()
  return True

