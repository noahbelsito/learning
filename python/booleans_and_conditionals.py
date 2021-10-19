# a bool has two possible values: True and False
# we can assign them manually
x = True
print(x)
print(type(x))

# usually we get bool values from bool operators (answer yes/no questions)
"""
    a == b   |   a equal to b
    a != b   |   a not equal to b
    a < b    |   a less than b
    a > b    |   a greater than b
    a <= b   |   a less than or equal to b
    a >= b   |   a greater than equal to b
"""

# Conditional Boolean Expressions
"""
    a == c and a == b       |   a is equal to b and c
    a == c or a == b        |   a is equal to c or b
    a == c and not a == b   |   a is equal to c and not equal to b
"""


# Boolean Operator Usage
def can_run_for_president(age):
    """Can someone of the given age run for president in the US?"""
    # The US Constitution says you must be at least 35 years old
    return age >= 35


print("Can a 19-year-old run for president?", can_run_for_president(19))
print("Can a 45-year-old run for president?", can_run_for_president(45))


# Boolean and Math Operators
def is_odd(n):
    return (n % 2) == 1


print("Is 100 odd?", is_odd(100))
print("Is -1 odd?", is_odd(-1))


# Conditional Boolean expression usage
def can_run_for_president(age, is_natural_born_citizen):
    """Can someone of the given age and citizenship status run for president in the US?"""
    # The US Constitution says you must be a natural born citizen *and* at least 35 years old
    return is_natural_born_citizen and (age >= 35)


print(can_run_for_president(19, True))
print(can_run_for_president(55, False))
print(can_run_for_president(55, True))

True or True and False  # True
