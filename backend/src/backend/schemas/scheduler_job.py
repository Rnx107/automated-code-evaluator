from datetime import datetime

from pydantic import BaseModel, Field


class CreateSchedulerJob(BaseModel):
    submission_id: int = Field(gt=0)
    priority: int = Field(ge=0)
    deadline: datetime


class ShowSchedulerJob(BaseModel):
    id: int = Field(gt=0)
    submission_id: int = Field(gt=0)
    priority: int = Field(ge=0)
    deadline: datetime
    status: str


class UpdateSchedulerJob(BaseModel):
    priority: int | None = Field(default=None, ge=0)
    deadline: datetime | None = None
    status: str | None = Field(default=None, min_length=1)