from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import Base

if TYPE_CHECKING:
    from backend.models.assignment import Assignment
    from backend.models.execution_result import ExecutionResult
    from backend.models.plagiarism_report import PlagiarismReport
    from backend.models.scheduler_job import SchedulerJob
    from backend.models.user import User


class Submission(Base):
    __tablename__ = "submissions"

    id: Mapped[int] = mapped_column(primary_key=True)
    assignment_id: Mapped[int] = mapped_column(ForeignKey("assignments.id"), nullable=False)
    student_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    code: Mapped[str] = mapped_column(Text, nullable=False)
    submitted_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="pending")

    assignment: Mapped["Assignment"] = relationship(back_populates="submissions")
    student: Mapped["User"] = relationship(back_populates="submissions")
    execution_results: Mapped[list["ExecutionResult"]] = relationship(
        back_populates="submission",
        cascade="all, delete-orphan",
    )
    scheduler_job: Mapped["SchedulerJob | None"] = relationship(
        back_populates="submission",
        uselist=False,
        cascade="all, delete-orphan",
    )
    reports_as_a: Mapped[list["PlagiarismReport"]] = relationship(
        back_populates="submission_a",
        foreign_keys="PlagiarismReport.submission_a_id",
        cascade="all, delete-orphan",
    )
    reports_as_b: Mapped[list["PlagiarismReport"]] = relationship(
        back_populates="submission_b",
        foreign_keys="PlagiarismReport.submission_b_id",
        cascade="all, delete-orphan",
    )
