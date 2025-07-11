from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

import services
from auth.oauth2 import get_current_user
from db.engine import get_db
from db.models import User, ActivityPhoto
from schemas import ActivityBase, ActivityPhotoCreate, ActivityPhotoBase, UserBase, UserCreate

router = APIRouter()

@router.get('/activities/')
def get_activities(
        session: Session = Depends(get_db),
):
    return services.get_activities(session=session)


@router.get('/activities/{activity_id}')
def get_activity(
        activity_id: int,
        session: Session = Depends(get_db),
):
    return services.get_activity(activity_id=activity_id, session=session)


@router.post('/activities/')
def create_activity(
        activate_create: ActivityBase,
        session: Session = Depends(get_db),
        current_user: UserBase = Depends(get_current_user),
):
    return services.create_activity(created_by=current_user.id,
                                    activate_create=activate_create,
                                    session=session)


@router.post('/activity_photos/', response_model=list[ActivityPhotoCreate])
def create_activity_photo(
        activity_id: int,
        activate_photo_create: list[ActivityPhotoCreate],
        current_user: User = Depends(get_current_user),
        session: Session = Depends(get_db)
):
    return services.create_activity_photos(activity_id=activity_id,
                                           session=session,
                                           activate_photo_create=activate_photo_create)

@router.get('/activity_photos/', response_model=list[ActivityPhotoBase])
def get_list_photos(
        session: Session = Depends(get_db)
):
    return session.query(ActivityPhoto).all()



@router.get('/users/{user_id}', response_model=UserBase)
def get_user(
        user_id: int,
        session: Session = Depends(get_db),
):
    user = services.get_user_by_id(user_id=user_id, session=session)
    return user
#
#
@router.get('/users/me', response_model=UserBase)
def get_user_profile(
    current_user: User = Depends(get_current_user),
):
    """Получить профиль текущего пользователя"""
    return current_user

#
@router.post('/users/', response_model=UserCreate)
def create_user(
        user_create: UserCreate,
        session: Session = Depends(get_db),
):
    return services.create_user(user_create=user_create, session=session)
