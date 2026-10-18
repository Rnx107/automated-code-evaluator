from pydantic import BaseModel, Field


class CreatePlagiarismReport(BaseModel):
    submission_a_id: int = Field(gt=0)
    submission_b_id: int = Field(gt=0)
    similarity_score: float = Field(ge=0, le=1)
    flagged: bool


class ShowPlagiarismReport(BaseModel):
    id: int = Field(gt=0)
    submission_a_id: int = Field(gt=0)
    submission_b_id: int = Field(gt=0)
    similarity_score: float = Field(ge=0, le=1)
    flagged: bool


class UpdatePlagiarismReport(BaseModel):
    similarity_score: float | None = Field(default=None, ge=0, le=1)
    flagged: bool | None = None
