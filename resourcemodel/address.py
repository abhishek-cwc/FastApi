from models.address import Address as AddressModel
from schemas.address_schema import Address
from sqlalchemy.orm import Session
from models.customer import Customer

def create_address(address: Address, customer: Customer, db: Session):
    address_obj = AddressModel (
        city = address.city,
        state = address.state,
        customer_id = customer.get("id")
    )

    db.add(address_obj)
    db.commit()
    db.refresh(address_obj)

    return address_obj
