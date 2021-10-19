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
