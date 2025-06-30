from datetime import datetime, timezone

from sqlmodel import Session

from app.models.event import EventCreate, Event
from app.models.users import User


class EventService:
    def __init__(self, session: Session):
        self.session = session

    def create_event(self, event: EventCreate, user: User):
        event_data = event.dict()
        # TODO - Remove test and use user from dependency
        event = Event(**event_data, created_by='test')

        self.session.add(event)
        self.session.commit()
        self.session.refresh(event)
        return event