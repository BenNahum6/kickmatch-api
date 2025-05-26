from fastapi import APIRouter
from pydantic import BaseModel
from app.db.DatabaseSupabase import DatabaseSupabase

router = APIRouter()

# Data model for user creation/update
class User(BaseModel):
    name: str
    email: str

@router.get("/users")
async def get_users():
    return [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"}
    ]

@router.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"id": user_id, "name": "Alice", "email": "alice@example.com"}

@router.post("/users")
async def create_user(user: User):
    return {"message": "User created", "user": user}

@router.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    return {"message": f"User {user_id} updated", "user": user}

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    return {"message": f"User {user_id} deleted"}
