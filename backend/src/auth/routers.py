from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from auth.schemas import Token
from auth.services import get_user_token
from db.engine import get_db


auth_app = APIRouter(tags=["Auth"])


@auth_app.post('/token/')
def get_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        session: AsyncSession = Depends(get_db),
) -> Token:
    return get_user_token(form_data=form_data, session=session)


