__author__ = 'chaoweichen26@gmail.com'

from pydecor import instead
from bokger import _dec_io_and_time, logger

log = instead(_dec_io_and_time.log, log=logger.log)