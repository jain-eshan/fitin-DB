import asyncpg
from app.core.database import get_db_connection
from app.schemas.user import UserCreate, UserOut
from typing import Optional
from uuid import UUID
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Helper to hash password
async def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

async def create_user(user: UserCreate) -> UserOut:
    conn = await get_db_connection()
    hashed_password = await get_password_hash(user.password)
    row = await conn.fetchrow(
        """
        INSERT INTO users (email, password_hash, full_name, role_id)
        VALUES ($1, $2, $3, $4)
        RETURNING id, email, full_name, role_id, created_at
        """,
        user.email, hashed_password, user.full_name, user.role_id
    )
    await conn.close()
    return UserOut(**dict(row))


async def get_user_by_email(email: str) -> Optional[UserOut]:
    conn = await get_db_connection()
    row = await conn.fetchrow(
        "SELECT id, email, full_name, role_id, created_at FROM users WHERE email = $1",
        email
    )
    await conn.close()
    return UserOut(**dict(row)) if row else None


async def get_user_by_id(user_id: UUID) -> Optional[UserOut]:
    conn = await get_db_connection()
    row = await conn.fetchrow(
        "SELECT id, email, full_name, role_id, created_at FROM users WHERE id = $1",
        str(user_id)
    )
    await conn.close()
    return UserOut(**dict(row)) if row else None
