"""

Outer function decorates a func that takes kwargs
the wrapper function it returns takes args (multiple tuples)

"""

def configure_plugin_decorator(func):
    def wrapper(*args):
        new_kwargs = dict(args)
        result = func(**new_kwargs)
        return result
        
    return wrapper
