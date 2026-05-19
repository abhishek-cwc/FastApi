from fastapi import FastAPI

from core.database import Base, engine
from routers import user_router, product_router, customer_router, address_router
from middlewares.logging_middleware import logging_middleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.middleware("http")(logging_middleware)

app.include_router(user_router.router)
app.include_router(product_router.router)
app.include_router(customer_router.router)
app.include_router(address_router.router)
