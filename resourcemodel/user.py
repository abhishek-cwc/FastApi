from sqlalchemy.orm import Session
from models.user import User
from schemas.user_schema import UserCreate, UserUpdate
from fastapi import HTTPException

def create_user(db: Session, user: UserCreate):
    db_user = User(
        name=user.name,
        email=user.email,
        age = user.age
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(limit, sort_by, db: Session):
    return db.query(User).order_by(getattr(User, sort_by)).limit(limit=limit).all()

def get_users_by_id(user_id, db: Session):

    user =  db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise  HTTPException(status_code=201, detail=f"user with id {user_id} not found")
    
    return user

def update_user_data(user_id, user: UserUpdate, db:Session):
    db_user = get_users_by_id(user_id, db)
    update_data = user.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)   
    return db_user
        