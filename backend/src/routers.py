from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

import services
from db.engine import get_db
from db.models import User
from schemas import ActivityBase

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
):
    return services.create_activity(activate_create=activate_create, session=session)


# user

# @router.get('/users/{user_id}')
# def get_user(
#         user_id: int,
#         session: Session = Depends(get_db),
# ):
#     return services.get_user(user_id=user_id, session=session)
#
