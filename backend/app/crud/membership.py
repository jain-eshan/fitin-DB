import asyncpg
from app.core.database import get_db_connection
from app.schemas.membership import Membership
from typing import Optional
from uuid import UUID

async def create_membership(membership: Membership) -> Membership:
    conn = await get_db_connection()
    row = await conn.fetchrow(
        """
        INSERT INTO memberships (user_id, status, start_date, end_date)
        VALUES ($1, $2, $3, $4)
        RETURNING id, user_id, status, start_date, end_date, created_at
        """,
        str(membership.user_id), membership.status, membership.start_date, membership.end_date
    )
    await conn.close()
    return Membership(**dict(row))

async def get_membership_by_user(user_id: UUID) -> Optional[Membership]:
    conn = await get_db_connection()
    row = await conn.fetchrow(
        "SELECT id, user_id, status, start_date, end_date, created_at FROM memberships WHERE user_id = $1",
        str(user_id)
    )
    await conn.close()
    return Membership(**dict(row)) if row else None
