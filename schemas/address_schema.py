from pydantic import BaseModel, Field
from typing import Annotated, Optional, Type

class Address(BaseModel):
    city: Annotated[str, Field(..., description="city")]
    state: Annotated[str, Field(..., description="state")]

class AddressResponse(BaseModel):
    id : Annotated[int, Field(..., description="address id")]
    city: Annotated[str, Field(..., description="city")]
    state: Annotated[str, Field(..., description="state")]
    customer_id: Annotated[int, Field(..., description="customer id")]    