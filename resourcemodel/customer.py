import os
from schemas.customer_schema import Customer as CustomerSchema, Login
from sqlalchemy.orm import Session
from models.customer import Customer as CustomerModel
from fastapi import HTTPException, Request
from pwdlib import PasswordHash
import jwt
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def create_customer(customer: CustomerSchema, db: Session):

    customer_obj = db.query(CustomerModel).filter(CustomerModel.email == customer.email).first()

    if customer_obj:
        raise HTTPException(status_code=400, detail="User email already exist")

    password_hash = get_password_hash(customer.password)
    customer_obj = CustomerModel(
        email = customer.email,
        password = password_hash
    )

    db.add(customer_obj)
    db.commit()
    db.refresh(customer_obj)
    return customer_obj


def login_customer(customer: Login, db: Session):
    customer_obj = db.query(CustomerModel).filter(CustomerModel.email == customer.email).first()
    if not customer_obj:
        raise HTTPException(401, detail="email not exists")
    
    hashed_password = get_password_hash(customer.password)
    if not verify_password(customer.password, hashed_password):
        raise HTTPException(401, detail="Password is wrong")

    token = jwt.encode({'id':customer_obj.id, 'email':customer_obj.email}, SECRET_KEY, ALGORITHM)
    return {'token': token}

def is_customer_login(request: Request, db: Session):
    print(request.headers.get("authorization"))
    auth_header = request.headers.get("authorization")
    if not auth_header:
        raise HTTPException(401, detail="authorization header is missing")
    
    token = auth_header.split(" ")[-1]
    
    if not token:
        raise HTTPException(401, detail="token is missing")

    customer = jwt.decode(token, SECRET_KEY, ALGORITHM)
    return customer

