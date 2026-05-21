from fastapi import FastAPI

from core.database import Base, engine
from routers import user_router, product_router, customer_router, address_router
from middlewares.logging_middleware import logging_middleware
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):

    # Connect DB
    Base.metadata.create_all(bind=engine)

    # Connect Redis
    # Connect Kafka
    # Load ML model

    yield

    # Close DB
    engine.dispose()

    # Close Redis
    # Close Kafka

app = FastAPI(lifespan=lifespan)

#Base.metadata.create_all(bind=engine)



app.middleware("http")(logging_middleware)

app.include_router(user_router.router)
app.include_router(product_router.router)
app.include_router(customer_router.router)
app.include_router(address_router.router)
