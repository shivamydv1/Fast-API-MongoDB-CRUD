from fastapi import APIRouter, Request
from services.user_service import *

router = APIRouter()

@router.post("/users")
async def create(request: Request):
    data = await request.json()
    user_id = create_user(data)
    return {"message": "User created", "id": user_id}

@router.get("/users")
def get_all():
    return get_all_users()

@router.get("/users/{id}")
def get_one(id: str):
    return get_user(id)

@router.put("/users/{id}")
async def update(id: str, request: Request):
    data = await request.json()
    update_user(id, data)
    return {"message": "User updated"}

@router.delete("/users/{id}")
def delete(id: str):
    delete_user(id)
    return {"message": "User deleted"}
