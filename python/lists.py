# Lists represent an ordered sequence of values
primes = [2, 3, 5, 7]
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'],
]
hands_v2 = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]
my_favourite_things = [32, 'raindrops on roses', help]

# Indexing can access individual list elements with []
# Which planet is closest to the sun?
print(planets[0])
# Next closest
print(planets[1])
# Which planet is furthest from the sun?
print(planets[-1])
print(planets[-2])

# Slicing allows us to split up lists [:]
# First three planets
print(planets[0:3])
# Start and end indices are not required
print(planets[:3])
print(planets[3:])
# last three planets
print(planets[-3:])

# Lists are "mutable" which means they can be modified "in place"
# You can modify lists by assigning to an index or slice expression
planets[3] = 'Kepler'
print(planets)
planets[:3] = ['Mur', 'Vee', 'Ur']

planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars']
print(planets)

# List functions are useful for working with lists
# len gives the length of a list
print(len(planets))
# sorted returns a sorted version of a list (Alphabetical or Numerical)
print(sorted(planets))
# sum adds all the elements in a list
print(sum(primes))  # 17
# min and max get the minimum or maximum of several arguments
print(min(primes))  # 2
print(max(primes))  # 7

# Everything in python is an object
# Objects carries things associated with them
# You can access those things but using python's dot syntax
# Numbers in python carry around an associated variable called imag
# which represents their imaginary part
x = 12  # x is a real number so it's imaginary part is 0
print(x.imag)
c = 12 + 3j  # c is a complex number so it's imaginary part is 3
print(c.imag)
# The things an object carries around can also include functions
# A function attached to an object is called a method
#     Non-function things attached to an object are called attributes
# numbers have a method called bit_length
print(x.bit_length)
# to call a method you need ()
print(x.bit_length())  # 4
# you can also call help on a method
help(x.bit_length)

# List methods
# append adds an element to a list with no return
planets.append('Pluto')  # pluto is a fucking planet you assholes
help(planets.append)
print(planets)
planets.pop()  # removes and returns the last element of a list

# Searching a list
# Where does earth fall in the order of planets?
print(planets.index('Earth'))
# To avoid ValueErrors where a value
# Use the in conditional operator to check if a value is in a list
print('Pluto' in planets)
if 'Mercury' in planets:
    print(planets.index('Mercury'))

# You can call help on a object to find all the method and attributes attached
help(planets)

# Tuples are almost exactly the same as lists
t = (1, 2, 3)  # tuples use () instead of square brackets
print(t)
# Tuples can't be modified they're immutable
# Tuples are often used for functions that have multiple return values
x = 0.125
# as_integer_ratio is the method of float objects
#     returns a numerator and denominator in the form of a tuple
print(x.as_integer_ratio())
numerator, denominator = x.as_integer_ratio()
print(numerator, '/', denominator, sep='')
print(numerator / denominator)

# Multivariable assignment
a = 1
b = 0
a, b = b, a
print(a, b)
