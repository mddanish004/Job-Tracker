from datetime import datetime

from sqlmodel import Field, SQLModel


class Company(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    name: str
    website: str | None = None

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)