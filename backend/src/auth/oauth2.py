from typing import Annotated

import jwt

from fastapi import HTTPException

from datetime import datetime, timezone
from datetime import timedelta

from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from db.engine import get_db
from services import get_user_by_id

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = 'ef26207164680423fb7505fe096e0e44ad534ce10a43d1c0885a1e499eeba82a'


def create_access_token(data: dict, expires_delta: timedelta | None = None):
        """Create access token with lifetime 15 minute"""
        encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        encode.update({"exp": expire})
        encode_jwt = jwt.encode(encode, SECRET_KEY, algorithm="HS256")
        return  encode_jwt


def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)],
        session: Session = Depends(get_db),
):
    """Return current user"""
    payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(status_code=401, detail="Not Authenticated")
    user = get_user_by_id(user_id=user_id, session=session)
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user
