from fastapi import APIRouter
from .endpoints import user, routine, diet, membership, meal_log

api_router = APIRouter()
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(routine.router, prefix="/routines", tags=["routines"])
api_router.include_router(diet.router, prefix="/diets", tags=["diets"])
api_router.include_router(membership.router, prefix="/memberships", tags=["memberships"])
api_router.include_router(meal_log.router, prefix="/meals", tags=["meals"])
