from fastapi import APIRouter
from app.schemas.diet import DietPlan
from app.crud.diet import create_diet_plan, get_diet_plans_by_user
from typing import List

router = APIRouter()

@router.post("/", response_model=DietPlan)
async def add_diet_plan(plan: DietPlan):
    return await create_diet_plan(plan)

@router.get("/user/{user_id}", response_model=List[DietPlan])
async def get_diet_plans(user_id: str):
    return await get_diet_plans_by_user(user_id)
