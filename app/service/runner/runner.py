from app.service.runner.runner_config import RunnerConfig
from app.service.runner.selector import Selector


class Runner:
    def __init__(self, config: RunnerConfig):
        self.config = config

    def run(self) -> None:
        for i in range(self.config.start, self.config.end + 1):
            presenter = Selector.select(i)
            presenter.present()
