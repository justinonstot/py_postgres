# python decorators from FreeCodeCamp

# a function can be passed to another function as an argument

### To create a decorator in Python.
## Create an outer function that takes a function as an argument
## then have an inner function that wraps around the decorated function

# This decorator logs the date and time a function is executed
from datetime import datetime

def log_datetime(func):
    '''Log the date and time of a function'''
    
    def wrapper():
        print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-"*30}')
        func()
    return wrapper

@log_datetime
def daily_backup():
    print('Daily backup job has finished.')
    
daily_backup()