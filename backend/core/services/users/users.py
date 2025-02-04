from pydantic import BaseModel, EmailStr
from typing import Optional
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from common.db.database import get_db
from common.db.models import User
from .router import router


class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None


class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr

    class Config:
        orm_mode = True  # Enable SQLAlchemy model compatibility


# CREATE a new user
@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# READ all users
@router.get("/", response_model=list[UserResponse])
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


# READ a single user by ID
@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# UPDATE a user
@router.put("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: str, user_data: UserUpdate, db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user_data.name:
        user.name = user_data.name
    if user_data.email:
        user.email = user_data.email

    db.commit()
    db.refresh(user)
    return user


# DELETE a user
@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return None  # No content (204)
