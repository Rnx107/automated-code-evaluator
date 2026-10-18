from pydantic import BaseModel, Field


class PlagiarismReportCreate(BaseModel):
    submission_a_id: int = Field(gt=0)
    submission_b_id: int = Field(gt=0)
    similarity_score: float = Field(ge=0, le=1)
    flagged: bool


class PlagiarismReportResponse(BaseModel):
    id: int = Field(gt=0)
    submission_a_id: int = Field(gt=0)
    submission_b_id: int = Field(gt=0)
    similarity_score: float = Field(ge=0, le=1)
    flagged: bool


class PlagiarismReportUpdate(BaseModel):
    similarity_score: float | None = Field(default=None, ge=0, le=1)
    flagged: bool | None = None
