from fastapi import APIRouter, Depends
from schemas.product_schema import ProductResponse, Product 
from core.database import SessionLocal
from resourcemodel.product import get_all_products, create_product
from sqlalchemy.orm import Session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()


@router.get("/products", response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return get_all_products(db)

@router.post("/products", response_model=ProductResponse)
def add_product(product: Product, db: Session = Depends(get_db)):
    return create_product(product, db)