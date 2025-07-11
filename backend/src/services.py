
from fastapi import Depends, HTTPException
from pydantic import EmailStr
from sqlalchemy.orm import Session
from starlette import status

from auth.oauth2 import get_current_user
from auth.security import bcrypt_password
from db.models import User, Activity, ActivityPhoto, UserPreferences
from db.engine import get_db
from schemas import ActivityBase, ActivityPhotoCreate, UserCreate


def get_activities(
        session: Session = Depends(get_db),
):
    return session.query(Activity).all()


def get_activity(
        activity_id: int,
        session: Session = Depends(get_db),
):
    return session.query(Activity).filter(Activity.id == activity_id).first()

def create_activity(
        created_by: int,
        activate_create: ActivityBase,
        session: Session = Depends(get_db),
):
    activity = Activity(
        name=activate_create.name,
        description=activate_create.description,
        category=activate_create.category,
        mod=activate_create.mod,
        budget=activate_create.budget,
        timestamp=activate_create.timestamp,
        date_of_activity=activate_create.date_of_activity,
        created_by=created_by,
    )
    session.add(activity)
    session.commit()
    session.refresh(activity)
    return activity


def create_activity_photos(
        activity_id: int,
        activate_photo_create: list[ActivityPhotoCreate],
        current_user: User = Depends(get_current_user),
        session: Session = Depends(get_db),
):
    photos = [
        ActivityPhoto(
            url=photo.url,
            is_main=photo.is_main,
            activity_id=activity_id
        ) for photo in activate_photo_create
    ]
    session.add_all(photos)
    session.commit()
    return photos


def get_user_preferences(
        session: Session = Depends(get_db),
):
    return session.query(UserPreferences).all()



def get_user_by_id(user_id: int, session: Session):
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

def get_user_by_email(
        email: EmailStr,
        session: Session = Depends(get_db),
):
    return session.query(User).where(User.email == email).first()


def create_user(
        user_create: UserCreate,
        session: Session = Depends(get_db),
):
    user = User(
        name=user_create.name,
        email=user_create.email,
        password=bcrypt_password(user_create.password),
        role='role'
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user



