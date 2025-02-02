from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world!!!x"}


@app.get("/dream-big")
async def dream_big():
    return {"message": "From core-web-app Dream BIG!!!"}
