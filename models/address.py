from sqlalchemy import (
    Integer,
    Column,
    String,
    ForeignKey
)

from sqlalchemy.orm import relationship

from core.database import Base


class Address(Base):

    __tablename__ = "customer_address"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    city = Column(String(20))

    state = Column(String(20))

    customer_id = Column(
        Integer,
        ForeignKey(
            "customer.id",
            ondelete="CASCADE"
        )
    )

    customer = relationship(
        "Customer",
        back_populates="addresses"
    )