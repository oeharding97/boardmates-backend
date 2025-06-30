from sqlmodel import SQLModel
from sqlmodel import Session

from app.database.session import engine
from app.models.users import User

def reset_db():
    # Drop all tables
    SQLModel.metadata.drop_all(bind=engine)
    print("✅ Dropped all tables.")

    # Recreate all tables
    SQLModel.metadata.create_all(bind=engine)
    print("✅ Recreated all tables.")

if __name__ == "__main__":
    reset_db()