from pydantic import BaseModel
from uuid import UUID
from typing import Optional, Any

class DietPlan(BaseModel):
    id: UUID
    user_id: UUID
    coach_id: UUID
    plan: Any
    created_at: Optional[str]
