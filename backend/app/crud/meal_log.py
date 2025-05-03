import asyncpg
from app.core.database import get_db_connection
from app.schemas.meal_log import MealLog
from typing import Optional, List
from uuid import UUID

async def create_meal_log(log: MealLog) -> MealLog:
    conn = await get_db_connection()
    row = await conn.fetchrow(
        """
        INSERT INTO meal_logs (user_id, date, meal, macros)
        VALUES ($1, $2, $3, $4)
        RETURNING id, user_id, date, meal, macros, created_at
        """,
        str(log.user_id), log.date, log.meal, log.macros
    )
    await conn.close()
    return MealLog(**dict(row))

async def get_meal_logs_by_user(user_id: UUID) -> List[MealLog]:
    conn = await get_db_connection()
    rows = await conn.fetch(
        "SELECT id, user_id, date, meal, macros, created_at FROM meal_logs WHERE user_id = $1",
        str(user_id)
    )
    await conn.close()
    return [MealLog(**dict(row)) for row in rows]
