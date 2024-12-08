import os
import pytest

from app.service.loader.environment_variable_loader import EnvironmentVariableLoader

# Test environment variable key and value
TEST_ENV_VAR_KEY = "TEST_ENV_VAR"
TEST_ENV_VAR_VALUE = "test_value"

@pytest.fixture
def setup_and_cleanup_environment_variable():
    """Set up an environment variable for testing and clean it up afterward"""
    # Set up the environment variable
    os.environ[TEST_ENV_VAR_KEY] = TEST_ENV_VAR_VALUE
    # Run the test
    yield
    # Clean up the environment variable
    del os.environ[TEST_ENV_VAR_KEY]

def test_load_environment_variable_success(setup_and_cleanup_environment_variable):
    """Positive test case: Verify the environment variable is correctly loaded"""
    value = EnvironmentVariableLoader.load(TEST_ENV_VAR_KEY)
    assert value == TEST_ENV_VAR_VALUE, "Failed to correctly retrieve the environment variable value"

def test_load_environment_variable_failure():
    """Negative test case: Verify that loading a non-existent environment variable raises a KeyError"""
    non_existent_key = "NON_EXISTENT_ENV_VAR"
    with pytest.raises(KeyError) as key_error_info:
        EnvironmentVariableLoader.load(non_existent_key)
