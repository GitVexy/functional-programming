def add_format(default_formats, new_format):
    return {
        **default_formats, new_format : True # Unpack existing formats and add new format
        }


def remove_format(default_formats, old_format):
    return {
            **default_formats, old_format : False # Unpack existing formats and add new format
        }

# Explaining unpacking:

def example(a, b, *args, **kwargs):
    
    print(f"a: {a}",
          "\nb: {b}",
          "\nargs: {args}",
          "\nkwargs: {kwargs}"
          )
    
    if kwargs["help"]:
        print("\nHelp:\n\nexample(a: str, b: str, *args: set/list/tuple, **kwargs: dict)\n")



a = "Hi"                        # normal variable
b = "Hello"                     # normal variable
args = ("Hello", "there")       # tuple of arguments
kwargs = {                      # dictionary of keyword arguments
    "one"   : "Test",
    "two"   : "Test 2",
    "help"  : True
    }
example(a, b, *args, **kwargs)  # calling a function with unpacked args and kwargs

