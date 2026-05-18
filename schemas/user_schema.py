from pydantic import BaseModel, EmailStr, Field, computed_field
from typing import Type, Optional, Annotated

class UserCreate(BaseModel):
    name: Annotated[str, Field(min_length=4, max_length=20, description="user email")]
    email: EmailStr = Field(description="User email") 
    age: int = Field(le= 75, ge= 18)

    @computed_field
    @property
    def score(self) -> int:
        if self.age >= 35 and self.age <= 50:
            return 10
        elif self.age > 50:
            return 7
        return 2

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None

class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True