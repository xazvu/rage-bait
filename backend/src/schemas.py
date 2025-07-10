from datetime import datetime

from pydantic import BaseModel, EmailStr


class ActivityBase(BaseModel):
    name: str
    description: str
    category: str
    mod: str
    timestamp: str
    date_of_activity: datetime
