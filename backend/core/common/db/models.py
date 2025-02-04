from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

from .id_generator import generate_uid

Base = declarative_base()


class BaseModel(Base):
    """Base model that includes common fields: id, created_at, updated_at."""

    # Prevents SQLAlchemy from creating a table for this class
    __abstract__ = True

    id = Column(String, primary_key=True, default=generate_uid)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, default=func.now(), onupdate=func.now(), nullable=False
    )


class User(BaseModel):
    __tablename__ = "users"

    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)


class Test(BaseModel):
    __tablename__ = "test"

    name = Column(String, nullable=True)
