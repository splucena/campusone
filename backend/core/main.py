from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.users.router import router as user_router

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
    return {"message": "Hello world!!!x"}


@app.get("/v1/api/dream-big")
async def dream_big():
    return {"message": "From core-web-app Dream BIG!!!"}


@app.get("/v1/api/data")
async def test_data():
    return {"data": {
        "backend": "fastapi",
        "frontend": "angular",
        "container": "docker",
        "orchestrator": "kubernetes",
        "version_control": "git",
    }}
