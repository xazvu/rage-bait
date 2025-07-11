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


class UserBase(BaseModel):
    id: int
    name: str
    email: str


class UserInfo(UserBase):
    role: str = None


class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_active: bool


class UserCreate(UserBase):
    password: str
    role: str = 'user'

    class Config:
        from_attributes = True


class ActivityHistoryBase(BaseModel):
    id: int
    user_id: int
    activity_id: int
    timestamp: datetime
    rating: int
    review: str
    is_completed: bool


class  UserPreferencesBase(BaseModel):
    mood: str
    available_time: int
    budget: float
    location: str