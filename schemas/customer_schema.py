from pydantic import BaseModel, EmailStr, Field
from typing import Annotated, Optional, List
from schemas.address_schema import AddressResponse


class Customer(BaseModel):
    email: Annotated[EmailStr, Field(..., description="customer email")]
    password: Annotated[str, Field(..., description="customer password")]

class CustomerCreateResponse(BaseModel):
    id: int
    email: str

class CustomerResponse(BaseModel):
    id: int
    email: str
    addresses: Optional[list[AddressResponse]] = []

    class Config:
        from_attributes = True

class Login(BaseModel):
    email: Annotated[EmailStr, Field(..., description="customer email")]
    password: Annotated[str, Field(..., description="customer password")]    
