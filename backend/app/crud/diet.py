import asyncpg
from app.core.database import get_db_connection
from app.schemas.diet import DietPlan
from typing import Optional, List
from uuid import UUID

async def create_diet_plan(plan: DietPlan) -> DietPlan:
    conn = await get_db_connection()
    row = await conn.fetchrow(
        """
        INSERT INTO diet_plans (user_id, coach_id, plan)
        VALUES ($1, $2, $3)
        RETURNING id, user_id, coach_id, plan, created_at
        """,
        str(plan.user_id), str(plan.coach_id), plan.plan
    )
    await conn.close()
    return DietPlan(**dict(row))

async def get_diet_plans_by_user(user_id: UUID) -> List[DietPlan]:
    conn = await get_db_connection()
    rows = await conn.fetch(
        "SELECT id, user_id, coach_id, plan, created_at FROM diet_plans WHERE user_id = $1",
        str(user_id)
    )
    await conn.close()
    return [DietPlan(**dict(row)) for row in rows]
