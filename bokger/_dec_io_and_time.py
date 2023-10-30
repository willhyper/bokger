__author__ = 'chaoweichen26@gmail.com'

from pydecor import Decorated
from time import time

def _repr(*args, **kwargs) -> str:
    _args = ', '.join([repr(a) for a in args])
    _kwargs = ', '.join([f'{k}={v}' for k, v in kwargs.items()])
    if _args and _kwargs:
        return _args + ', ' + _kwargs
    elif _args and not _kwargs:
        return _args
    elif not _args and _kwargs:
        return _kwargs
    else:
        return ""

class OpInfo:
    def __init__(self, dec: Decorated, started, ended):
        self.args = dec.args
        self.kwargs = dec.kwargs
        self.wrapped = dec.wrapped
        self.result = dec.result
        self.started = started
        self.ended = ended

    def __repr__(self):
        _module_method_name = self.wrapped.__qualname__
        _args = _repr(*self.args, **self.kwargs)
        _msg = f"{_module_method_name}({_args}) -> {self.result}"
        _elapsed_sec = self.ended - self.started
        _elapsed_msg = "" if _elapsed_sec < 0.001 else f" # elapsed {_elapsed_sec:.3f} seconds"
        return _msg + _elapsed_msg
        
def log(d: Decorated, log):
    _start = time()
    _result = d(*d.args, **d.kwargs)
    _end = time()
    log(OpInfo(d, _start, _end))
    return _result # = d.result

