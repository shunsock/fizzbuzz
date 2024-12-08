from app.service.runner.fizzbuzz_presenter.fizz import Fizz


def test_buzz_str():
    """
    Test the __str__ method of the Fizz class.
    Expected: 'Fizz'
    """
    buzz = Fizz()
    assert str(buzz) == "Fizz", "The __str__ method should return 'Fizz'"


def test_buzz_present(capsys):
    """
    Test the present method of the Fizz class.
    Expected: 'Fizz'
    """
    buzz = Fizz()
    buzz.present()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Fizz", "The present method should print 'Fizz'"
