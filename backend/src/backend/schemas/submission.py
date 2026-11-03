from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class SubmissionCreate(BaseModel):
    assignment_id: int = Field(gt=0)
    student_id: int = Field(gt=0)
    code: str


class SubmissionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(gt=0)
    assignment_id: int = Field(gt=0)
    student_id: int = Field(gt=0)
    code: str
    submitted_at: datetime
    status: str


class SubmissionUpdate(BaseModel):
    status: str = Field(min_length=1)