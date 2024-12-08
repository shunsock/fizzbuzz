from app.service.runner.fizzbuzz_presenter.buzz import Buzz


def test_buzz_str():
    """
    Test the __str__ method of the Buzz class.
    Expected: 'Buzz'
    """
    buzz = Buzz()
    assert str(buzz) == "Buzz", "The __str__ method should return 'Buzz'"


def test_buzz_present(capsys):
    """
    Test the present method of the Buzz class.
    Expected: 'Buzz'
    """
    buzz = Buzz()
    buzz.present()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Buzz", "The present method should print 'Buzz'"
