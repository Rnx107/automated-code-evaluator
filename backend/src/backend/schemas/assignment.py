from datetime import datetime

from backend.core.runtime import LanguageRuntime
from pydantic import BaseModel, Field


class CreateAssignment(BaseModel):
    title: str = Field(min_length=10)
    language: LanguageRuntime
    due_date: datetime


class ShowAssignment(BaseModel):
    id: int = Field(gt=0)
    created_by: int = Field(gt=0)
    title: str
    language: LanguageRuntime
    due_date: datetime


class UpdateAssignment(BaseModel):
    title: str | None = None
    language: LanguageRuntime | None = None
    due_date: datetime | None = None
