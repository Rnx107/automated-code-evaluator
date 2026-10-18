from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import Base

if TYPE_CHECKING:
    from backend.models.submission import Submission
    from backend.models.test_case import TestCase


class ExecutionResult(Base):
    __tablename__ = "execution_results"

    id: Mapped[int] = mapped_column(primary_key=True)
    submission_id: Mapped[int] = mapped_column(ForeignKey("submissions.id"), nullable=False)
    test_case_id: Mapped[int] = mapped_column(ForeignKey("test_cases.id"), nullable=False)
    actual_output: Mapped[str] = mapped_column(Text, nullable=False)
    passed: Mapped[bool] = mapped_column(Boolean, nullable=False)
    runtime_ms: Mapped[int] = mapped_column(Integer, nullable=False)
    memory_kb: Mapped[int] = mapped_column(Integer, nullable=False)

    submission: Mapped["Submission"] = relationship(back_populates="execution_results")
    test_case: Mapped["TestCase"] = relationship(back_populates="execution_results")
