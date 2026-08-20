from sqlmodel import SQLModel, create_engine

from app.config.settings import DATABASE_URL
from app.models.company import Company


engine = create_engine(
    DATABASE_URL,
    echo=True,
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()