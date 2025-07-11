from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

import services
from auth.oauth2 import get_current_user
from db.engine import get_db
from db.models import User, ActivityPhoto
from schemas import ActivityBase, ActivityPhotoCreate, ActivityPhotoBase, UserBase, UserCreate, ActivityHistoryBase, \
    UserPreferencesBase

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
        session: Session = Depends(get_db)
):
    return services.create_activity_photos(activity_id=activity_id,
                                           session=session,
                                           activate_photo_create=activate_photo_create)


@router.get('/users/', response_model=UserBase)
def get_users(name, email):
    return {'name': name, 'email': email}


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
    user = services.get_user_by_id(user_id, session)
    return user


@router.get('/users/me', response_model=UserBase)
def get_user_profile(
    current_user: User = Depends(get_current_user),
):
    """Получить профиль текущего пользователя"""
    return current_user


@router.post('/users/', response_model=UserBase)
def create_user(
        user_create: UserCreate,
        session: Session = Depends(get_db),
):
    return services.create_user(user_create=user_create, session=session)


@router.get('/activity_histories/')
def get_activity_histories(
        session: Session = Depends(get_db)
):
    return services.get_activity_histories(session=session)


@router.post('/activity_histories/')
def create_activity_histories(
        activity_history_create: ActivityHistoryBase,
        session: Session = Depends(get_db),
        current_user: User = Depends(get_current_user),

):
    return services.create_activity_history(
        activity_history_create=activity_history_create,
        session=session,
        current_user=current_user,
    )


@router.get('/user_preferences/')
def get_user_preferences(
        session: Session = Depends(get_db)
):
    return services.get_user_preferences(session=session)


@router.post('/user_preferences/')
def create_user_preferences(
        user_preferences_create: UserPreferencesBase,
        session: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    return services.create_user_preferences(user_preferences_create, session, current_user)