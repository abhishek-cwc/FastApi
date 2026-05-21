from fastapi import APIRouter, Depends, Request
from core.database import SessionLocal, get_db
from sqlalchemy.orm import Session
from models.customer import Customer as CustomerModel
from schemas.customer_schema import Customer, CustomerResponse, Login, CustomerCreateResponse
from resourcemodel.customer import create_customer, login_customer, is_customer_login, get_customer_info
from utils.helper import is_customer_login as customer_login

router = APIRouter(prefix="/customer")


@router.post("/register", response_model=CustomerCreateResponse)
def register(customer: Customer, db: Session = Depends(get_db)):
    return create_customer(customer, db)

@router.post("/login")
def login(customer: Login, db: Session = Depends(get_db)):
    return login_customer(customer, db)

@router.post("/is_auth", response_model=CustomerResponse)
def is_auth(request: Request, db: Session = Depends(get_db)):
    return is_customer_login(request, db)


@router.get("/", response_model=CustomerResponse, summary="Get customers deatil")
def get_customer_detail(db: Session = Depends(get_db), customer: CustomerModel = Depends(customer_login)):
    return get_customer_info(customer , db)
