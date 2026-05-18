from models.product import Product as ProductModel
from sqlalchemy.orm import Session
from schemas.product_schema import Product


def get_all_products(db: Session):
    return db.query(ProductModel).all()

def create_product(product: ProductModel, db: Session):
    db_product = ProductModel(
        name = product.name,
        sku = product.sku,
        price = product.price,
        description = product.description
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product