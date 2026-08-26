from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

engine = create_engine("sqlite:///database.db")


def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
