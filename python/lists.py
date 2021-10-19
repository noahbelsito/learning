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
