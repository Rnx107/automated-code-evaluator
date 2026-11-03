from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class SchedulerJobCreate(BaseModel):
    submission_id: int = Field(gt=0)
    priority: int = Field(ge=0)
    deadline: datetime


class SchedulerJobResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(gt=0)
    submission_id: int = Field(gt=0)
    priority: int = Field(ge=0)
    deadline: datetime
    status: str


class SchedulerJobUpdate(BaseModel):
    priority: int | None = Field(default=None, ge=0)
    deadline: datetime | None = None
    status: str | None = Field(default=None, min_length=1)