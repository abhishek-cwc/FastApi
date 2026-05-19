from fastapi import APIRouter, Depends, Request
from core.database import SessionLocal, get_db
from sqlalchemy.orm import Session
from schemas.customer_schema import Customer, CustomerResponse, Login
from resourcemodel.customer import create_customer, login_customer, is_customer_login


router = APIRouter(prefix="/customer")


@router.post("/register", response_model=CustomerResponse)
def register(customer: Customer, db: Session = Depends(get_db)):
    return create_customer(customer, db)

@router.post("/login")
def login(customer: Login, db: Session = Depends(get_db)):
    return login_customer(customer, db)

@router.post("/is_auth", response_model=CustomerResponse)
def is_auth(request: Request, db: Session = Depends(get_db)):
    return is_customer_login(request, db)
