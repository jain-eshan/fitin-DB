from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class Membership(BaseModel):
    id: UUID
    user_id: UUID
    status: str
    start_date: Optional[str]
    end_date: Optional[str]
    created_at: Optional[str]
