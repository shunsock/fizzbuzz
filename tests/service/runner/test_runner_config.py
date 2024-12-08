import pytest
from pydantic import ValidationError
from app.service.runner.runner_config import RunnerConfig

def test_runner_config_valid():
    """Test valid configurations for RunnerConfig."""
    config = RunnerConfig(start=5, end=10)
    assert config.start == 5
    assert config.end == 10

def test_runner_config_start_greater_than_end():
    """Test that start > end raises a validation error."""
    with pytest.raises(ValidationError) as validation_error_info:
        RunnerConfig(start=10, end=5)
    assert "start must not be greater than end" in str(validation_error_info.value)

def test_runner_config_negative_values():
    """Test that negative values raise a validation error due to PositiveInt."""
    with pytest.raises(ValidationError):
        RunnerConfig(start=-1, end=10)

    with pytest.raises(ValidationError):
        RunnerConfig(start=5, end=-10)

def test_runner_config_zero_values():
    """Test that zero values raise a validation error due to PositiveInt."""
    with pytest.raises(ValidationError):
        RunnerConfig(start=0, end=10)

    with pytest.raises(ValidationError):
        RunnerConfig(start=5, end=0)

def test_runner_config_equal_values():
    """Test that start equal to end is valid."""
    config = RunnerConfig(start=10, end=10)
    assert config.start == 10
    assert config.end == 10
