from .router import router


@router.get("/")
async def get_users():
    return {
        "data": {
            "user1": "User One",
            "user2": "User Two",
        }
    }