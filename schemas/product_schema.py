from pydantic import BaseModel, Field
from typing import Optional, Annotated

class Product(BaseModel):
    name: Annotated[str, Field(...,  description="name of product")]
    price: Annotated[float, Field(..., description="price of product")]
    sku: Optional[Annotated[str, Field(description="price of product")]] = None
    description: Optional[Annotated[str, Field(description="Product description")]] = None

class ProductResponse(Product):
    id: int

    class Config:
        from_attributes = True
