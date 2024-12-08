from app.service.runner.fizzbuzz_presenter.otherwise import Otherwise


def test_otherwise_initialization():
    """Test the initialization of the Otherwise class."""
    instance = Otherwise(count=42)
    assert instance.count == 42, "The count attribute should be set to the provided value."

def test_otherwise_present(capsys):
    """Test the present method of the Otherwise class."""
    instance = Otherwise(count=100)
    instance.present()
    captured = capsys.readouterr()
    assert captured.out.strip() == "100", "The present method should print the count value."