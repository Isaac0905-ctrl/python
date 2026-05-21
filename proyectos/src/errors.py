from .settings import LOG_PATH


class TitsaError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        with open(LOG_PATH, 'a') as f:
            f.write(message + '\n')
