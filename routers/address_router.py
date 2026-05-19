from fastapi import APIRouter, Depends
from core.database import get_db
from sqlalchemy.orm import Session
from schemas.address_schema import Address
from resourcemodel.address import create_address
from models.customer import Customer
from utils.helper import is_customer_login

router = APIRouter(prefix="/address")

@router.post("/create")
def create(address: Address, db: Session = Depends(get_db), customer: Customer = Depends(is_customer_login)):
    return create_address(address,customer, db)
