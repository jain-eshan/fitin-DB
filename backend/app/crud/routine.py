import asyncpg
from app.core.database import get_db_connection
from app.schemas.routine import ExerciseRoutine
from typing import Optional, List
from uuid import UUID

async def create_routine(routine: ExerciseRoutine) -> ExerciseRoutine:
    conn = await get_db_connection()
    row = await conn.fetchrow(
        """
        INSERT INTO exercise_routines (user_id, coach_id, date, routine)
        VALUES ($1, $2, $3, $4)
        RETURNING id, user_id, coach_id, date, routine, created_at
        """,
        str(routine.user_id), str(routine.coach_id), routine.date, routine.routine
    )
    await conn.close()
    return ExerciseRoutine(**dict(row))

async def get_routines_by_user(user_id: UUID) -> List[ExerciseRoutine]:
    conn = await get_db_connection()
    rows = await conn.fetch(
        "SELECT id, user_id, coach_id, date, routine, created_at FROM exercise_routines WHERE user_id = $1",
        str(user_id)
    )
    await conn.close()
    return [ExerciseRoutine(**dict(row)) for row in rows]
