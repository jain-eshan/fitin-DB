from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    role_id: int

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: UUID
    created_at: Optional[str]

class UserInDB(UserOut):
    password_hash: str
