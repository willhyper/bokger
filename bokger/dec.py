__author__ = 'chaoweichen26@gmail.com'

from pydecor import instead, after
from bokger import _dec_io_and_time, logger, database

_dec_html = instead(_dec_io_and_time.log, log= logger.log)
_dec_db = after(database.push)

log = _dec_db(_dec_html)
