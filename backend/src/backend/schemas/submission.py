from datetime import datetime

from pydantic import BaseModel, Field


class CreateSubmission(BaseModel):
    assignment_id: int = Field(gt=0)
    student_id: int = Field(gt=0)
    code: str


class ShowSubmission(BaseModel):
    id: int = Field(gt=0)
    assignment_id: int = Field(gt=0)
    student_id: int = Field(gt=0)
    code: str
    submitted_at: datetime
    status: str


class UpdateSubmissionStatus(BaseModel):
    status: str = Field(min_length=1)