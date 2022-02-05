
def outer_function():
    message = 'Hi'

    def inner_function():
        print(message)
    #return inner_function()
    return inner_function  # waiting to be executed

#outer_function()

my_func = outer_function()
my_func()  # closure remembers the message variable even after the outer function is executed
my_func()


def outer_function(msg):
    def inner_function():
        print(msg)
    
    return inner_function 

hi_func = outer_function('Hi')
bye_func = outer_function('bye')

hi_func() 
bye_func()

# decorator is function that takes another function as an argument and adds some functionality and returns another function
# without altering the source code of the original function

def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

def display():
    print('display function run')

decorated_display = decorator_function(display)
decorated_display()


@decorator_function
def display():
    print('display function run')

display()
#display = decorator_function(display)


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print('display function run')

@decorator_function
def display_info(name,age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)



# class decorator

class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_class
def display():
    print('display function run')

@decorator_class
def display_info(name,age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)



from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Tom', 22)