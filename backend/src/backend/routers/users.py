from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.user import User
from backend.schemas.user import UserCreate, UserLogin, UserResponse
from backend.security import hash_password, verify_password

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/login")
def user_login(user: UserLogin, db: Session = Depends(get_db)):
    statement = select(User).where(User.email == user.email)
    result = db.execute(statement)
    db_user = result.scalar_one_or_none()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User Not Found")
    if not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    return {"message": "Login Successful"}


@router.post(
    "/create", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
def user_create(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.execute(
        select(User).where(User.email == user.email)
    ).scalar_one_or_none()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    db_user = User(
        name=user.name,
        email=user.email,
        password_hash=hash_password(user.password),
        role=user.role,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
