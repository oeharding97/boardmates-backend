from datetime import datetime
from enum import EnumType

from pydantic import BaseModel

class EventType(EnumType):
    BIRTHDAY = "birthday"
    WORK = "work"

class EventCreate(BaseModel):
    event_name: str
    start_date: datetime
    end_date: datetime
    event_type: str
    created_at: datetime
    created_by: int


class Event(EventCreate):
    event_id: int
    updated_at: datetime
    updated_by: int


