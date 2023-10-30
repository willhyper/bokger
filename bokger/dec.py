__author__ = 'chaoweichen26@gmail.com'

from pydecor import Decorated, instead
from time import time
from bokger import logger

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

def _record_io_and_time(dec: Decorated):
    _start = time()
    _result = dec.wrapped(*dec.args, **dec.kwargs)
    _end = time()
    _elapsed_sec = _end - _start
    _args = _repr(*dec.args, **dec.kwargs)
    _module_method_name = dec.wrapped.__qualname__
    _msg = f"{_module_method_name}({_args}) -> {dec.result}"
    _elapsed_msg = "" if _elapsed_sec < 0.001 else f" # elapsed {_elapsed_sec:.3f} seconds"
    logger.log(_msg + _elapsed_msg)

log = instead(_record_io_and_time)