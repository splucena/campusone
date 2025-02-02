from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
