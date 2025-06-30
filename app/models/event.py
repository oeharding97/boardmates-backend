from datetime import datetime, timezone
from enum import Enum

from sqlmodel import SQLModel, Field, Relationship

from app.models.users import User


class EventRecurrence(Enum):
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"

class EventBase(SQLModel):
    title: str
    description: str | None
    location: str
    start_time: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    end_time: datetime
    all_day: bool = False
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime | None = None
    recurrence_rule: EventRecurrence | None = None
    created_by: str
    updated_by: str | None = None

class Event(EventBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class EventPublic(EventBase):
    id: int

class EventCreate(SQLModel):
    title: str
    description: str | None
    location: str
    start_time: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    end_time: datetime
    all_day: bool = False
    recurrence_rule: EventRecurrence | None = None