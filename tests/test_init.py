'''
can monkey patch
'''

from bokger import logger
print = logger.log

print(f"hello world")