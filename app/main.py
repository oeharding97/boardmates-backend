from typing import Annotated

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from sqlmodel import SQLModel
from sqlmodel import Session, select

from app.models.event import EventPublic, Event, EventCreate
from app.models.users import User
from app.services.event_service import EventService
from database.session import engine
from database.session import get_session


app = FastAPI()

SessionDep = Annotated[Session, Depends(get_session)]

def get_event_service(db: SessionDep) -> EventService:
    return EventService(session=db)

def get_user() -> User:
    # todo : add proper auth here
    return User(created_at="2025-06-23T20:54:23.580948",
    username="Olivia",
    user_id=1,
    first_name="Olivia",
    last_name="Harding")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/events", response_model=list[EventPublic])
def read_events(session: SessionDep, offset: int = 0, limit: int = 100):
    statement = select(Event).offset(offset).limit(limit)
    return session.exec(statement).all()

@app.get("/events/{event_id}", response_model=EventPublic)
def read_event(event_id: int, session: SessionDep):
    event = session.get(Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")


@app.post("/events/", response_model=EventPublic)
def create_event(event: EventCreate,
                 user: User = Depends(get_user),
                 service: EventService = Depends(get_event_service)):
    return service.create_event(event=event, user=user)


@app.get("/users", response_model=list[User])
def read_users(session: SessionDep, offset: int = 0, limit: int = 100):
    statement = select(User).offset(offset).limit(limit)
    return session.exec(statement).all()

@app.get("/users/{user_id}", response_model=User)
def read_user(session: SessionDep, user_id: int):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

@app.post("/users/", response_model=User)
def create_user(user: User, session: SessionDep):
    user = User.model_validate(user)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
