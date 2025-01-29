def args_logger(*args, **kwargs):
    
    for i in range(0, len(args)):
        current_arg = args[i]
        
        print(f"{i + 1}. {current_arg}")
    
    for i in range(0, len(kwargs)):
        current_key = sorted(kwargs.keys())[i]
        current_value = kwargs[current_key]
        
        print(f"* {current_key}: {current_value}")

args_logger("what's", "up", "doc", date="July 4 1776", age=17)