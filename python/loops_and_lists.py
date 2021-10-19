# Loops are a way to repeatedly execute some code
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# for loop specifies the variable name to use (planet) and the set of values to loop over (planets)
# the in keyword links them together
for planet in planets:
    print(planet, end=' ')  # print all on same line
# The object to the right of in has to support iteration
multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for multiplier in multiplicands:
    product = product * multiplier
print(product)
# You can also loop through strings
s = 'steganograpHy is thE practice of conceaLing a file or message within another fiLe Or message'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')

# range() is a function that returns a sequence of numbers
for i in range(5):
    print("Doing important work. i =", i)

# while() loop iterates while a condition is met
i = 0
while i < 10:
    print(i, end=' ')
    i += 1  # increase the value of i by 1
print()

# List comprehensions are a unique feature to python
squares = [n**2 for n in range(10)]
print(squares)

# without list comprehensions
squares = []
for n in range(10):
    squares.append(n**2)
print(squares)

# adding if statement to list comprehension
short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print(loud_short_planets)

# cleaner list comprehension structure
[
    planet.upper() + '!'
    for planet in planets
    if len(planet) < 6
]

print([32 for planet in planets])


# Example list comprehension for cleaner code
# no list comprehension
def count_negatives(nums):
    """Return the number of negative numbers in the given list.

    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative


# list comprehension usage
def count_negatives_v2(nums):
    return len([num for num in nums if num < 0])


def count_negatives_v3(nums):
    # Reminder: in the "booleans and conditionals" exercises, we learned about a quirk of
    # Python where it calculates something like True + True + False + True to be equal to 3.
    return sum([num < 0 for num in nums])
