from pydantic import BaseModel, Field


class ExecutionResultCreate(BaseModel):
    submission_id: int = Field(gt=0)
    test_case_id: int = Field(gt=0)
    actual_output: str
    passed: bool
    runtime_ms: int = Field(ge=0)
    memory_kb: int = Field(ge=0)


class ExecutionResultResponse(BaseModel):
    id: int = Field(gt=0)
    submission_id: int = Field(gt=0)
    test_case_id: int = Field(gt=0)
    actual_output: str
    passed: bool
    runtime_ms: int = Field(ge=0)
    memory_kb: int = Field(ge=0)


class ExecutionResultUpdate(BaseModel):
    actual_output: str | None = None
    passed: bool | None = None
    runtime_ms: int | None = Field(default=None, ge=0)
    memory_kb: int | None = Field(default=None, ge=0)
