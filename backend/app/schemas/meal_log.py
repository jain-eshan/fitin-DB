from pydantic import BaseModel
from uuid import UUID
from typing import Optional, Any

class MealLog(BaseModel):
    id: UUID
    user_id: UUID
    date: str
    meal: Any
    macros: Any
    created_at: Optional[str]
