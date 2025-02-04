from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from services.users.router import router as user_router

from common.db.database import get_db
from common.db.models import User
from sqlalchemy.orm import Session

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router, prefix="/v1/api")


@app.get("/")
async def root():
    return {"message": "Hello world!!!xxx"}


@app.get("/v1/api/dream-big")
async def dream_big():
    return {"message": "From core-web-app Dream BIG!!!"}


@app.get("/v1/api/data")
async def test_data(db: Session = Depends(get_db)):
    users = db.query(User).all()
    # print(users)
    campusone_users = {}
    for user in users:
        campusone_users.update({
            f"{user.name}": user.email
        })
        print(user.name)
    return {"data": campusone_users}
