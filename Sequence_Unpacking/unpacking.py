"""
Iterable unpacking is a method usedd in python for assigning the values of an iterable to a variable in python
It works for any iterable in python including Strings, Files, Iterators and generators
"""

# tuples
from audioop import avg


p = (2, 3)
x, y = p
print(x, y)

# Lists
data = ["1", "John Doe", "36", "SomeFortune10000", "Johndoe@emaill.com"]
id, name, age, company, email = data
print(id, name, age, company, email)

#Strings
greet = "Hello"
a, b, c, d, e = greet
print(a, b, c, d, e)

"""PS. There is no special method for discarding certain values
If you want to discard certain values you can assign a dummy variable to it
"""
discard = [1.3, 5.0, 4.5, 7.6]
_, _, point1, point2 = discard
print(point1, point2)


"""Unpacking elements from iterables of arbitrary length.  The python * expression is used to unpack multiple elements from a list"""

def unpack_multiple_elements(iterable):
    *everything_else_here, the_last_element = iterable
    return everything_else_here
print(unpack_multiple_elements(data))
