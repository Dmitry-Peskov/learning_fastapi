import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import DateTime, String
from .base_model import BaseModel


class User(BaseModel):
    fullname: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    happy_birthday: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    telegram_url: Mapped[str] = mapped_column(
        String,
        nullable=True
    )
