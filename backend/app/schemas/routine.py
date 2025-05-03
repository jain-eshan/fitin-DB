from pydantic import BaseModel
from uuid import UUID
from typing import Optional, Any

class ExerciseRoutine(BaseModel):
    id: UUID
    user_id: UUID
    coach_id: UUID
    date: str
    routine: Any
    created_at: Optional[str]
