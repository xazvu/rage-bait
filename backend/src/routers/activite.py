from site import USER_BASE

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from pydant import CreateUser, ReadUser
from db.engine import get_db
from db.models import User

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/", response_model=list[ReadUser])
async def comments(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.post("/", response_model=ReadUser)
async def comments(us: CreateUser, db: Session = Depends(get_db)):
    users = User(name=us.name, email=us.email, password=us.password, role=us.role)
    db.add(users)
    db.commit()
    db.refresh(users)
    return users