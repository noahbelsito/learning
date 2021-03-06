# abs() returns the absolute value of a number
print(abs(-8.2))

# help() returns a brief description of what a function does
help(abs)


# def defines a new function
# you can add comments after the function definition to add docstring (help fn)
def least_difference(a, b, c):
    """Returns the smallest difference between any two numbers
    among a, b and c.

    : Parameters
    a: number
    b: number
    c: number

    : Return
    the smallest difference between any two numbers among a, b, and c

    >>> least_difference(1, 5, -5)
    4
    """

    diff_1 = abs(a - b)
    diff_2 = abs(b - c)
    diff_3 = abs(c - a)
    return min(diff_1, diff_2, diff_3)  # without a return function they will return None


print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 100),
    least_difference(5, 6, 7),  # Python allows trailing commas in argument lists
)

help(least_difference)


# optional argument example
def greet(who="cutie"):
    print("Hello, ", who)


# Higher Order Functions
def multiply_by_five(x):
    return 5 * x


# takes a function as an argument and the arguments for that function
def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)


# takes a function as an argument and the arguments for that function
def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))


print(
    call(multiply_by_five, 1),
    squared_call(multiply_by_five, 1),
    sep='\n',  # '\n' is the newline character
)


# Higher Order Functions Example
def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5


print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)
