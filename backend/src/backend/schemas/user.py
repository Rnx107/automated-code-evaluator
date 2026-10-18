from pydantic import BaseModel, EmailStr, Field, field_validator

from backend.core.roles import UserRole


class UserCreate(BaseModel):
    name: str = Field(min_length=5, max_length=100)
    email: EmailStr
    role: UserRole
    password: str = Field(min_length=8)

    @field_validator("password")
    @classmethod
    def validate_password(cls, password: str) -> str:
        requirements = (
            any(character.islower() for character in password),
            any(character.isupper() for character in password),
            any(character.isdigit() for character in password),
            any(not character.isalnum() and not character.isspace() for character in password),
            not any(character.isspace() for character in password),
        )
        if not all(requirements):
            raise ValueError(
                "Password must contain lowercase, uppercase, digit, and special characters "
                "and must not contain whitespace"
            )
        return password


class UserResponse(BaseModel):
    id: int = Field(gt=0)
    name: str
    email: str
    role: UserRole


class AdminUserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    role: UserRole | None = None


class UserLogin(BaseModel):
    email: str
    password: str
