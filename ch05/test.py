# self_math is a higher order function
# input: a function that takes two arguments and returns a value
# output: a new function that takes one argument and returns a value
def self_math(operation):
    def inner_function(x):
        return operation(x, x)
        
    return inner_function

def multiply(x, y):
    return x * y

def add(x, y):
    return x + y

square_func = self_math(multiply)
double_func = self_math(add)

print(square_func(5))
# prints 25

print(double_func(5, 6))
# prints 10