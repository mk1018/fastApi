import os
from functools import wraps

def set_run_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        os.environ['RUN_TEST'] = "True"
        return func(*args, **kwargs)
    return wrapper