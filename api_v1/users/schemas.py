import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, HttpUrl, PastDate, ConfigDict, validator


class UserGet(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime


class UserCreate(UserGet):
    fullname: str
    happy_birthday: PastDate
    email: EmailStr
    telegram_url: str


class UserUpdate(BaseModel):
    fullname: Optional[str] = None
    happy_birthday: Optional[PastDate] = None
    email: Optional[EmailStr] = None
    telegram_url: Optional[str] = None
