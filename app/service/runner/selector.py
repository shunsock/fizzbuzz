from app.service.runner.fizzbuzz_presenter.buzz import Buzz
from app.service.runner.fizzbuzz_presenter.fizz import Fizz
from app.service.runner.fizzbuzz_presenter.fizz_buzz import FizzBuzz
from app.service.runner.fizzbuzz_presenter.otherwise import Otherwise
from app.service.runner.fizzbuzz_presenter.protocol import FizzBuzzPresenter


class Selector:
    @staticmethod
    def select(count: int) -> FizzBuzzPresenter:
        divisible_by_3 = count % 3 == 0
        divisible_by_5 = count % 5 == 0

        if divisible_by_3 and divisible_by_5:
            return FizzBuzz()
        elif divisible_by_3:
            return Fizz()
        elif divisible_by_5:
            return Buzz()
        else:
            return Otherwise(count)
