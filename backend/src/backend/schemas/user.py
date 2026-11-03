from backend.core.roles import UserRole
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    name: str = Field(min_length=5, max_length=100)
    email: EmailStr
    role: UserRole
    password: str = Field(min_length=8)


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(gt=0)
    name: str
    email: str
    role: UserRole


class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    role: UserRole | None = None


class UserLogin(BaseModel):
    email: str
    password: str
