from core.database import Base
from sqlalchemy import Column, INT, String, VARCHAR

class Customer(Base):
    __tablename__ = "customer"

    id =  Column(INT, primary_key=True, index=True)
    email = Column(VARCHAR(20), nullable=False)
    password = Column(String(200), nullable=False)
