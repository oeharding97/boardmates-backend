import os

from sqlalchemy import create_engine, Engine
from sqlmodel import Session

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://oeharding:password@localhost/boardmates_db")

engine: Engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session