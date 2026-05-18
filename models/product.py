from sqlalchemy import Column, Integer, String, Float
from core.database import Base

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(15))
    sku = Column(String(20))
    price = Column(Float)
    description = Column(String(50))

    # def __repr__(self):
    #     return f"Product(id={self.id}, name='{self.name}', sku='{self.sku}', description='{self.description}')"