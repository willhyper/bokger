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

def log(clz, _do = logger.log):
    @wraps(clz, updated=()) #https://stackoverflow.com/questions/6394511/python-functools-wraps-equivalent-for-classes
    class wrapped_clz(clz):
        def __getattribute__(self, name):
            attr = object.__getattribute__(self, name)
            
            if not callable(attr): return attr
            fn = attr
            
            @wraps(name)
            def wrapped_fn(*args, **kwargs):
                _return = attr(*args, **kwargs)
                _do(f"{type(self).__name__}.{fn.__name__}({_repr(*args, **kwargs)})={_return}")
                return _return
            return wrapped_fn

    return wrapped_clz


