from core.database import Base

from sqlalchemy import (
    Column,
    Integer,
    String
)

from sqlalchemy.orm import relationship


class Customer(Base):

    __tablename__ = "customer"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    email = Column(
        String(100),
        nullable=False
    )

    password = Column(
        String(200),
        nullable=False
    )

    addresses = relationship(
        "Address",
        back_populates="customer",
        cascade="all, delete"
    )