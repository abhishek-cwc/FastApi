from pydantic import BaseModel, EmailStr, Field
from typing import Annotated, Optional


class Customer(BaseModel):
    email: Annotated[EmailStr, Field(..., description="customer email")]
    password: Annotated[str, Field(..., description="customer password")]


class CustomerResponse(BaseModel):
    id: int
    email: str

class Login(BaseModel):
    email: Annotated[EmailStr, Field(..., description="customer email")]
    password: Annotated[str, Field(..., description="customer password")]    
