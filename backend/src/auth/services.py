from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from auth.oauth2 import create_access_token
from auth.schemas import Token
from auth.security import verify_password
from db.engine import get_db
from db.models import User
from services import get_user_by_email


def get_user_token(
        form_data: OAuth2PasswordRequestForm,
        session: Session = Depends(get_db),
):
    """Return admin access token"""
    user = get_user_by_email(email=form_data.username, session=session)
    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Wrong password")
    access_token = create_access_token(
        data={
            "sub": str(user.id),
            "email": user.email,
            "username": user.username,
        })
    return Token(access_token=access_token, token_type="bearer")