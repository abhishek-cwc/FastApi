from fastapi import FastAPI

from core.database import Base, engine
from routers import user_router, product_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router.router)
app.include_router(product_router.router)
