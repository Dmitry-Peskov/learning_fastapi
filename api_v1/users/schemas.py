import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, PastDate, ConfigDict


class UserCreate(BaseModel):
    fullname: str
    happy_birthday: PastDate
    email: EmailStr
    telegram_url: str


class UserGet(UserCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime


class UserUpdate(BaseModel):
    fullname: Optional[str] = None
    happy_birthday: Optional[PastDate] = None
    email: Optional[EmailStr] = None
    telegram_url: Optional[str] = None
