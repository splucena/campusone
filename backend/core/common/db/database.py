import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


load_dotenv()

P_DB = os.getenv("POSTGRES_DB")
P_USER = os.getenv("POSTGRES_USER")
P_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DATABASE_URL = (
    f"postgresql://{P_USER}:{P_PASSWORD}@web-core-db:5432/{P_DB}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
