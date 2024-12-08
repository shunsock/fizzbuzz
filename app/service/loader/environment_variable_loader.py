import os
from typing import Optional


class EnvironmentVariableLoader:
    @staticmethod
    def load(key: str) -> str:
        value: Optional[str] = os.getenv(key)

        if value is None:
            raise KeyError(f"Could not find environment variable with key: {key}")

        return value