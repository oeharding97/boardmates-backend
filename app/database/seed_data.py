from sqlmodel import Session

from app.database.session import engine
from app.models.users import User


def seed_users():
    user_1 = User(
        username='Olivia',
        first_name='Olivia',
        last_name='Harding')

    user_2 = User(
        username='Sri',
        first_name='Srihitha',
        last_name='Konreddy')

    with Session(engine) as session:
        session.add_all([user_1, user_2])
        session.commit()


if __name__ == '__main__':
    seed_users()