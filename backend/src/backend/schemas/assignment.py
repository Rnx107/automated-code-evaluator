from datetime import datetime

from backend.core.runtime import LanguageRuntime
from pydantic import BaseModel, Field


class AssignmentCreate(BaseModel):
    title: str = Field(min_length=10)
    language: LanguageRuntime
    due_date: datetime


class AssignmentResponse(BaseModel):
    id: int = Field(gt=0)
    created_by: int = Field(gt=0)
    title: str
    language: LanguageRuntime
    due_date: datetime


class AssignmentUpdate(BaseModel):
    title: str | None = None
    language: LanguageRuntime | None = None
    due_date: datetime | None = None
