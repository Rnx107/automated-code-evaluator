from pydantic import BaseModel, Field


class CreateTestCase(BaseModel):
    assignment_id: int = Field(gt=0)
    input: str
    expected_output: str
    weight: float = Field(ge=0)


class ShowTestCase(BaseModel):
    id: int = Field(gt=0)
    assignment_id: int = Field(gt=0)
    input: str
    expected_output: str
    weight: float = Field(ge=0)


class UpdateTestCase(BaseModel):
    input: str | None = None
    expected_output: str | None = None
    weight: float | None = Field(default=None, ge=0)