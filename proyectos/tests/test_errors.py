from .loader import TitsaError, settings


def test_titsa_error_initialization():
    error_message = 'This is a test error.'
    error = TitsaError(error_message)
    assert str(error) == error_message


def test_titsa_error_logging():
    ERROR_MESSAGES = [
        'First test error for logging.',
        'Second test error for logging.',
        'Third test error for logging.',
    ]
    for error_message in ERROR_MESSAGES:
        TitsaError(error_message)
    with open(settings.LOG_PATH, 'r') as log_file:
        logs = log_file.read()
    for error_message in ERROR_MESSAGES:
        assert error_message in logs
