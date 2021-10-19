# Python really excels at string manipulation
# String Syntax
x = '"Pluto" is a planet'
y = "Pluto's a planet"

# Escape Character Usage in strings (\)
"""
    \'    |    ' 	       |    'What\'s up?'              |    What's up?
    \" 	  |    " 	       |    "That's \"cool\"" 	       |     That's "cool"
    \\ 	  |    \ 	       |    "Look, a mountain: /\\"    |    Look, a mountain: /\
    \n    |                |    "1\n2 3"                   |    1 
                                                                2 3
"""

triple_quote_string = """This
is
an example of a triple
quote string."""

# Strings are sequences of characters
planet = 'Pluto'
# Indexing strings
print(planet[0])
# Slicing strings
print(planet[2:])
# String length
print(len(planet))
# Looping over a string
print([char+'! ' for char in planet])
# Can't modify strings like lists
# planet[0] = 'B' << error
# planet.append   << error

# String Methods
true_statement = 'Pluto is a planet!'
print(true_statement.upper())
print(true_statement.lower())
# Searching for the first index of a substring
print(true_statement.index('plan'))
print(true_statement.startswith(planet))
print(true_statement.endswith('dwarf planet'))
# Split divides a string into a list by a separator
words = true_statement.split()
print(words)
# Changing split separator
date_str = '1956-01-31'
year, month, day = date_str.split('-')
print(year, month, day)
# Join brings strings together
print('/'.join([month, day, year]))
print(' 👏 '.join([word.upper() for word in words]))
# building strings without .format()
print(planet + ', we miss you.')
position = 9
planet + ", you'll always be the " + str(position) + "th planet to me."
# building strings with .format()
print("{}, you'll always be the {}th planet to me.".format(planet, position))

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points formatted as percent       separate with commas
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(planet,
                                                                                                        pluto_mass,
                                                                                                        pluto_mass /
                                                                                                        earth_mass,
                                                                                                        population))
# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)
