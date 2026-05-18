from sqlalchemy import Column, Integer, String
from core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    age = Column(Integer)
    score = Column(Integer)

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}', age='{self.age}')"