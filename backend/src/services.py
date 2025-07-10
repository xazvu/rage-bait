from unicodedata import category

from fastapi import Depends
from sqlalchemy.orm import Session

from db.models import User, Activity, ActivityPhoto
from db.engine import get_db
from schemas import ActivityBase, ActivityPhotoBase


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
        activate_create: ActivityBase,
        session: Session = Depends(get_db),
):
    activity = Activity(
        name=activate_create.name,
        description=activate_create.description,
        category=activate_create.category,
        mod=activate_create.mod,
        timestamp=activate_create.timestamp,
        date_of_activity=activate_create.date_of_activity
    )
    session.add(activity)
    session.commit()
    session.refresh(activity)
    return activity


def create_activity_photos(
        activate_photo_create: ActivityPhotoBase,
        session: Session = Depends(get_db),
):
    photos = [ActivityPhoto(
        url=activate_photo_create.url,
        activity_id=activate_photo_create.activity_id
    )
        for url in activate_photo_create]

    session.add_all(photos)

