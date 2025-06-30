from datetime import datetime, timezone

from sqlmodel import SQLModel, Field

class UserBase(SQLModel):
    username: str
    first_name: str
    last_name: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    last_login: datetime | None


class User(UserBase, table=True):
    __tablename__ = "users"
    user_id: int | None = Field(default=None, primary_key=True)
