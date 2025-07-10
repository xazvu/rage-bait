from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from auth.oauth2 import create_access_token
from auth.schemas import Token
from auth.security import verify_password
from db.engine import get_db
from services import get_user


def get_user_token(
        form_data: OAuth2PasswordRequestForm,
        session: AsyncSession = Depends(get_db),
):
    """Return admin access token"""
    user = get_user(form_data.username)
    if not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Wrong password")
    access_token = create_access_token(
        data={
            "sub": str(user.id),
            "email": user.email,
            "username": user.username,
        })
    return Token(access_token=access_token, token_type="bearer")