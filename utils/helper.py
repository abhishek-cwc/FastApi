from fastapi import Request, HTTPException, Depends
import jwt
import os
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from models.customer import Customer as CustomerModel
from core.database import get_db

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')

def is_customer_login(request: Request, db: Session = Depends(get_db)):
    #print(request.headers.get("authorization"))
    auth_header = request.headers.get("authorization")
    if not auth_header:
        raise HTTPException(401, detail="authorization header is missing")
    
    token = auth_header.split(" ")[-1]
    
    if not token:
        raise HTTPException(401, detail="token is missing")

    customer = jwt.decode(token, SECRET_KEY, ALGORITHM)
    return customer