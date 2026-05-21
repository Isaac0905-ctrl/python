import os
import tempfile

if os.path.exists('solution'):
    from solution import settings
else:
    from src import settings  # type: ignore

db_path = tempfile.NamedTemporaryFile(delete=False, suffix='.db').name
setattr(settings, 'DB_PATH', db_path)  # set DB_PATH to the temporary file path

log_path = tempfile.NamedTemporaryFile(delete=False, suffix='.log').name
setattr(settings, 'LOG_PATH', log_path)  # set LOG_PATH to the temporary

if os.path.exists('solution'):
    from solution.buses import Bus
    from solution.db import DbHandler
    from solution.errors import TitsaError
    from solution.stops import Stop
    from solution.users import User
else:
    from src.buses import Bus  # type: ignore
    from src.db import DbHandler  # type: ignore
    from src.errors import TitsaError  # type: ignore
    from src.stops import Stop  # type: ignore
    from src.users import User  # type: ignore

__all__ = ['settings', 'DbHandler', 'TitsaError', 'User', 'Bus', 'Stop']
