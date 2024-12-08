from app.service.runner.fizzbuzz_presenter.buzz import Buzz
from app.service.runner.fizzbuzz_presenter.fizz import Fizz
from app.service.runner.fizzbuzz_presenter.fizz_buzz import FizzBuzz
from app.service.runner.fizzbuzz_presenter.otherwise import Otherwise
from app.service.runner.selector import Selector

def test_divisible_by_3_and_5():
    """
    Test numbers divisible by 3 and 5
    Expected: FizzBuzz
    """
    result = Selector.select(15)
    assert isinstance(result, FizzBuzz), f"Expected FizzBuzz, got {type(result)}"

def test_divisible_by_3():
    """
    Test numbers divisible by 3 only
    Expected: Fizz
    """
    result = Selector.select(9)
    assert isinstance(result, Fizz), f"Expected Fizz, got {type(result)}"

def test_divisible_by_5():
    """
    Test numbers divisible by 5 only
    Expected: Buzz
    """
    result = Selector.select(10)
    assert isinstance(result, Buzz), f"Expected Buzz, got {type(result)}"

def test_not_divisible_by_3_or_5():
    """
    Test numbers not divisible by 3 or 5
    Expected: Otherwise
    """
    result = Selector.select(7)
    assert isinstance(result, Otherwise), f"Expected Otherwise, got {type(result)}"
