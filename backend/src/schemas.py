from datetime import datetime

from pydantic import BaseModel, EmailStr


class ActivityBase(BaseModel):
    name: str
    description: str
    budget: float
    category: str
    mod: str
    timestamp: str
    date_of_activity: datetime


class ActivityPhotoBase(BaseModel):
    url: str
    is_main: bool
    activity_id: int


class ActivityPhotoCreate(BaseModel):
    url: str
    is_main: bool
