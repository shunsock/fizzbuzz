from pydantic import BaseModel, PositiveInt, ValidationInfo, field_validator


class RunnerConfig(BaseModel):
    start: PositiveInt
    end: PositiveInt

    @field_validator("end")
    @classmethod
    def check_start_less_than_end(
        cls, end: PositiveInt, info: ValidationInfo
    ) -> PositiveInt:
        start = info.data.get("start")
        if start is not None and start > end:
            raise ValueError("start must not be greater than end")
        return end
