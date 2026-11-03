from pydantic import BaseModel, ConfigDict, Field


class TestCaseCreate(BaseModel):
    assignment_id: int = Field(gt=0)
    input: str
    expected_output: str
    weight: float = Field(ge=0)


class TestCaseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(gt=0)
    assignment_id: int = Field(gt=0)
    input: str
    expected_output: str
    weight: float = Field(ge=0)


class TestCaseUpdate(BaseModel):
    input: str | None = None
    expected_output: str | None = None
    weight: float | None = Field(default=None, ge=0)