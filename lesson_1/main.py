from functools import wraps
from time import time

def run_time(func):
    @wraps(func)
    def wrapper():
        start = time()
        func()
        end = time()
        print(f"the function happened {end - start} seconds")
    return wrapper


@run_time
def my_func():
    for i in range(1000000000):
        continue


my_func()
