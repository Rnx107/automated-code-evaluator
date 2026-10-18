from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.core.runtime import LanguageRuntime
from backend.models.base import Base

if TYPE_CHECKING:
    from backend.models.submission import Submission
    from backend.models.test_case import TestCase
    from backend.models.user import User


class Assignment(Base):
    __tablename__ = "assignments"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_by: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    due_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    language: Mapped[LanguageRuntime] = mapped_column(Enum(LanguageRuntime), nullable=False)

    creator: Mapped["User"] = relationship(back_populates="assignments")
    test_cases: Mapped[list["TestCase"]] = relationship(
        back_populates="assignment",
        cascade="all, delete-orphan",
    )
    submissions: Mapped[list["Submission"]] = relationship(
        back_populates="assignment",
        cascade="all, delete-orphan",
    )
