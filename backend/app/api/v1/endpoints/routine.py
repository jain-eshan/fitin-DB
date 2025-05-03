from fastapi import APIRouter
from app.schemas.routine import ExerciseRoutine
from app.crud.routine import create_routine, get_routines_by_user
from typing import List

router = APIRouter()

@router.post("/", response_model=ExerciseRoutine)
async def add_routine(routine: ExerciseRoutine):
    return await create_routine(routine)

@router.get("/user/{user_id}", response_model=List[ExerciseRoutine])
async def get_routines(user_id: str):
    return await get_routines_by_user(user_id)
