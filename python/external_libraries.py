# Python has a vast amount of libraries for different uses
# Standard library is the library that comes with python
# Imports are how we import external libraries
import math as mt
from math import *
import numpy
import tensorflow as tf

math = mt
print("It's math! It has type {}".format(type(mt)))
# math is a module
# a module is just a collection of variables defined by someone else
# we can see all the names in math using the built-in function dir()
print(dir(math))
print("pi to 4 significant digits = {:.4}".format(mt.pi))
print(math.log(32, 2))
help(math.log)
help(math)

print(pi, log(32, 2))

# submodules are modules within other modules
print("numpy.random is a", type(numpy.random))  # random is a submodule
print("it contains names such as...", dir(numpy.random)[-15:])

# Roll 10 dice
rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls)

# Using help, dir and type
print(type(rolls))
print(dir(rolls))
print(rolls.mean())
print(rolls.tolist())
help(rolls.ravel)

# Operator overloading
# [1, 2, 3, 4, 5] + 10   <<   error
# operators on numpy arrays
print(rolls + 10)
print(rolls >= 3)

# 2D Array
x_list = [[1, 2, 3], [2, 4, 6]]
x = numpy.asarray(x_list)
print("x_list = {}\nx =\n{}".format(x_list, x))
print(x[1, -1])

# Tensorflow usage
# Creating constants each with the value 1
a = tf.constant(1)
b = tf.constant(1)
# You can add them together
print(a + b)
# a symbolic handle to one of the outputs of an operation
# it does not hold the values of that operation's output,
# but instead provides a means of computing those values in a TensorFlow TF Session
