from app.service.runner.runner import Runner
from app.service.runner.runner_config import RunnerConfig


class FizzbuzzController:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def run(self) -> bool:
        runner = Runner(RunnerConfig(start=self.start, end=self.end))
        runner.run()
        return True