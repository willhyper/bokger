from functools import wraps
from .Logger import logger
import time

def log_io(fn, _log = logger.log):
    @wraps(fn)
    def _dec(*args, **kwargs):
        _return = fn(*args, **kwargs)
        _log(f"{fn.__name__}({args, kwargs})={_return}")
        return _return
    return _dec

def log_time(fn, _log = logger.log):
    @wraps(fn)
    def _dec(*args, **kwargs):
        _start = time.time()        
        _return = fn(*args, **kwargs)
        _end = time.time()
        _elapsed = _end - _start
        _log(f"{fn.__name__}({args, kwargs}) elapsed {_elapsed} seconds.")
        return _return
    return _dec