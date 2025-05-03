from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserOut
from app.crud.user import create_user, get_user_by_email, get_user_by_id
from typing import List

router = APIRouter()

@router.post("/", response_model=UserOut)
async def register_user(user: UserCreate):
    db_user = await get_user_by_email(user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await create_user(user)

@router.get("/{user_id}", response_model=UserOut)
async def get_user(user_id: str):
    user = await get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
