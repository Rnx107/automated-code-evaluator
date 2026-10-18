from typing import TYPE_CHECKING

from sqlalchemy import Float, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import Base

if TYPE_CHECKING:
    from backend.models.assignment import Assignment
    from backend.models.execution_result import ExecutionResult


class TestCase(Base):
    __tablename__ = "test_cases"

    id: Mapped[int] = mapped_column(primary_key=True)
    assignment_id: Mapped[int] = mapped_column(ForeignKey("assignments.id"), nullable=False)
    input: Mapped[str] = mapped_column(Text, nullable=False)
    expected_output: Mapped[str] = mapped_column(Text, nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)

    assignment: Mapped["Assignment"] = relationship(back_populates="test_cases")
    execution_results: Mapped[list["ExecutionResult"]] = relationship(
        back_populates="test_case",
        cascade="all, delete-orphan",
    )
