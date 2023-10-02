import sys
import pathlib
from .Logger import logger
from .utilities.Caller import _get_caller_info
from ._version import __version__

logger.log(f"Bokger version {__version__}")

_script_name = pathlib.Path(sys.argv[0]).stem # no extension    

_caller_info = _get_caller_info(_script_name)
if _caller_info['__doc__']: logger.log_code(_caller_info['__doc__'])
if _caller_info['__author__']: logger.log_code(f"authored by {_caller_info['__author__']}")

