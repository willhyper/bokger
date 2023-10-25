'''
can use decorator to log i/o 
'''
__author__ = "chaoweichen26@gmail.com"

from bokger import dec

@dec.log_io
def my_fn(num1 : int, num2 : int, num3 : int , num4 : int):
    return num1+num2+num3+num4

my_fn(1,2,num3=3, num4=4)