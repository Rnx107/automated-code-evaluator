from typing import TYPE_CHECKING

from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.core.roles import UserRole
from backend.models.base import Base

if TYPE_CHECKING:
    from backend.models.assignment import Assignment
    from backend.models.submission import Submission


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(320), unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), nullable=False)

    assignments: Mapped[list["Assignment"]] = relationship(
        back_populates="creator",
        cascade="all, delete-orphan",
    )
    submissions: Mapped[list["Submission"]] = relationship(back_populates="student")
