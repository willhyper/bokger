from functools import wraps
from .Logger import logger

def log_io(fn, _log = logger.log):
    @wraps(fn)
    def _dec(*args, **kwargs):
        _return = fn(*args, **kwargs)
        _log(f"{fn.__name__}({args, kwargs})={_return}")
        return _return
    return _dec