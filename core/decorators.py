
import time

from functools import wraps
from core.exceptions import APIConnectionError


def retry(max_attempts=3, delay=1):

    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1.")

    if delay < 0:
        raise ValueError("delay cannot be negative.")

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            for attempt in range(max_attempts):

                try:
                    return func(*args, **kwargs)

                except APIConnectionError:

                    if attempt == max_attempts - 1:
                        raise

                    time.sleep(delay)

        return wrapper

    return decorator
