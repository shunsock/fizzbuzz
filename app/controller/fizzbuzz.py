import json

from pydantic import ValidationError

from app.service.runner.runner import Runner
from app.service.runner.runner_config import RunnerConfig


class FizzbuzzController:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def run(self) -> None:
        """
        Run the fizzbuzz algorithm

        Note:
            we catch errors at controller level and print them to the user
        """
        try:
            runner = Runner(RunnerConfig(start=self.start, end=self.end))
            runner.run()
        except ValidationError as e:
            print("UserError: Input Values are invalid")
            print(json.dumps(e.errors(), indent=4))
            exit(1)
