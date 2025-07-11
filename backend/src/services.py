<<<<<<< HEAD
from fastapi import Depends
=======

from fastapi import Depends, HTTPException
from pydantic import EmailStr
>>>>>>> develop
from sqlalchemy.orm import Session
from starlette import status

from auth.oauth2 import get_current_user
from auth.security import bcrypt_password
from db.models import User, Activity, ActivityPhoto, UserPreferences, ActivityHistory
from db.engine import get_db
<<<<<<< HEAD
from schemas import ActivityBase, ActivityPhotoCreate, UserCreate, ActivityHistoryBase, UserPreferencesBase
=======
from schemas import ActivityBase, ActivityPhotoCreate, UserCreate
>>>>>>> develop


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

<<<<<<< HEAD
# ActivityHistory
def get_activity_histories(
        session: Session = Depends(get_db),
):
    return session.query(ActivityHistory).all()


def create_activity_history(
        activity_history_create: ActivityHistoryBase,
        session: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    activity_history = ActivityHistory(
        user_id=current_user,
        activity_id=activity_history_create.activity_id,
        rating=activity_history_create.rating,
        review=activity_history_create.review,
        timestamp=activity_history_create.timestamp,
        is_completed=activity_history_create.is_completed
    )
    session.add(activity_history)
    session.commit()
    session.refresh(activity_history)
    return activity_history


def get_user_preferences(
        session: Session = Depends(get_db),
):
    return session.query(UserPreferences).all()


def create_user_preferences(
        user_preferences_create: UserPreferencesBase,
        session: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    user_preferences = UserPreferences(
        user_id=current_user,
        mood=user_preferences_create.mood,
        available_time=user_preferences_create.available_time,
        budget=user_preferences_create.budget,
        lcation=user_preferences_create.location
    )

    session.add(user_preferences)
    session.commit()
    session.refresh(user_preferences)
    return user_preferences
=======

>>>>>>> develop

