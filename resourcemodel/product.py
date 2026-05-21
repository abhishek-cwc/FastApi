from models.product import Product as ProductModel
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.product_schema import Product
from sqlalchemy import select



def get_all_products(db: Session):
    return db.query(ProductModel).all()

async def async_get_all_products(db: AsyncSession):
    result = await db.execute(select(ProductModel))
    return result.scalars().all()    


def create_product(product: ProductModel, db: Session):
    db_product = ProductModel(
        name = product.name,
        sku = product.sku,
        price = product.price,
        description = product.description
    )

    db.add(db_product)
    try:
        db.commit()
        db.refresh(db_product)
    except Exception:
        db.rollback()
        raise
    return db_product


async def async_create_product(
    product: Product,
    db: AsyncSession
):
    db_product = ProductModel(
        name=product.name,
        sku=product.sku,
        price=product.price,
        description=product.description
    )

    db.add(db_product)
    try:
        await db.commit()
        await db.refresh(db_product)

    except Exception:
        db.rollback()
        raise    

    
    return db_product