from fastapi import APIRouter, Depends
from schemas.product_schema import ProductResponse, Product 
from core.database import SessionLocal, get_db
from core.database_async import AsyncSessionLocal, get_async_db
from resourcemodel.product import get_all_products, create_product, async_get_all_products
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio
import time


router = APIRouter()


@router.get("/products", response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    time.sleep(5)
    return get_all_products(db)

@router.get("/async_products", response_model=list[ProductResponse])
async def async_get_products(db: AsyncSession  = Depends(get_async_db)):
    await asyncio.sleep(5)
    return await async_get_all_products(db)


@router.post("/products", response_model=ProductResponse)
def add_product(product: Product, db: Session = Depends(get_db)):
    return create_product(product, db)