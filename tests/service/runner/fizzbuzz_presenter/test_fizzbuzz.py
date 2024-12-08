from app.service.runner.fizzbuzz_presenter.fizz_buzz import FizzBuzz


def test_buzz_str():
    """
    Test the __str__ method of the FizzBuzz class.
    Expected: 'FizzBuzz'
    """
    buzz = FizzBuzz()
    assert str(buzz) == "FizzBuzz", "The __str__ method should return 'FizzBuzz'"

def test_buzz_present(capsys):
    """
    Test the present method of the FizzBuzz class.
    Expected: 'FizzBuzz'
    """
    buzz = FizzBuzz()
    buzz.present()
    captured = capsys.readouterr()
    assert captured.out.strip() == "FizzBuzz", "The present method should print 'FizzBuzz'"
