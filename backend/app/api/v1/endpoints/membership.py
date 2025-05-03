from fastapi import APIRouter, HTTPException
from app.schemas.membership import Membership
from app.crud.membership import create_membership, get_membership_by_user

router = APIRouter()

@router.post("/", response_model=Membership)
async def add_membership(membership: Membership):
    return await create_membership(membership)

@router.get("/user/{user_id}", response_model=Membership)
async def get_membership(user_id: str):
    membership = await get_membership_by_user(user_id)
    if not membership:
        raise HTTPException(status_code=404, detail="Membership not found")
    return membership
