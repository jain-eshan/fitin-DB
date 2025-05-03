from fastapi import APIRouter
from app.schemas.meal_log import MealLog
from app.crud.meal_log import create_meal_log, get_meal_logs_by_user
from typing import List

router = APIRouter()

@router.post("/", response_model=MealLog)
async def add_meal_log(log: MealLog):
    return await create_meal_log(log)

@router.get("/user/{user_id}", response_model=List[MealLog])
async def get_meal_logs(user_id: str):
    return await get_meal_logs_by_user(user_id)
