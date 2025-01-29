import functools

def printer_decorator(name):
    def decorator(func):
        @functools.wraps(func)
        def printer(*args):
            x = args[0]
            print(f"Applying {name} to {x}")  # Prints the name of the decorator
            return func(x)
        return printer
    return decorator

@printer_decorator("my_decorator")
def my_decorator(func):
    def wrapper(*args):
        x = args[0]
        x += 1
        result = func(x)
        return result
    return wrapper

@printer_decorator("my_decorator_2")
def my_decorator_2(func):
    def wrapper(*args):
        x = args[0]
        x += 2
        result = func(x)
        return result
    return wrapper

@printer_decorator
@my_decorator
@my_decorator_2
def do_this(x: int):
    return x

print(do_this(1))