from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import Base

if TYPE_CHECKING:
    from backend.models.submission import Submission


class PlagiarismReport(Base):
    __tablename__ = "plagiarism_reports"

    id: Mapped[int] = mapped_column(primary_key=True)
    submission_a_id: Mapped[int] = mapped_column(ForeignKey("submissions.id"), nullable=False)
    submission_b_id: Mapped[int] = mapped_column(ForeignKey("submissions.id"), nullable=False)
    similarity_score: Mapped[float] = mapped_column(Float, nullable=False)
    flagged: Mapped[bool] = mapped_column(Boolean, nullable=False)

    submission_a: Mapped["Submission"] = relationship(
        back_populates="reports_as_a",
        foreign_keys=[submission_a_id],
    )
    submission_b: Mapped["Submission"] = relationship(
        back_populates="reports_as_b",
        foreign_keys=[submission_b_id],
    )
