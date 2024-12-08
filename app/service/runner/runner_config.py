from pydantic import BaseModel


class RunnerConfig(BaseModel):
    start: int
    end: int