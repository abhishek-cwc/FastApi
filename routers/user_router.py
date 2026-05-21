from fastapi import APIRouter, Depends, Path, Query
from sqlalchemy.orm import Session

from core.database import SessionLocal, get_db
from schemas.user_schema import UserCreate, UserResponse, UserUpdate
from resourcemodel.user import create_user, get_users, get_users_by_id, update_user_data

from models.customer import Customer
from utils.helper import is_customer_login

router = APIRouter()


@router.post("/users")
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/users", response_model=list[UserResponse])
def all_users(
    limit: int = Query(4, le=10),
    sort_by: str = Query('id'),
    db: Session = Depends(get_db),
    user: Customer = Depends(is_customer_login)
    ):
    return get_users(limit, sort_by, db)

@router.get("/user/{user_id}", response_model=UserResponse)
def get_user_detail(
    user_id: int = Path(..., description="admin user id", examples="1"),
    db : Session = Depends(get_db)
    ):
    return get_users_by_id(user_id, db)

@router.patch("/user/{user_id}", response_model=UserResponse)
def update_user(
    user: UserUpdate,
    user_id: int = Path(..., description="admin user id", examples="1"),
    db : Session = Depends(get_db)
    ):
    return update_user_data(user_id, user, db)