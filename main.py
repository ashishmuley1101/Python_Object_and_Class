
# Python Operator Overloading.

# ** In Python that allows the same operator to have different meaning according to the context is called operator overloading.
# + Operator Overloading
# the + operator will perform arithmetic addition on two numbers, merge two lists, or concatenate two strings.

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # The __add__() method overloads the + operator to add the real and imaginary parts of the
    # two complex numbers together and returns a new Complex object with the resulting values
    def __add__(self, other):
        return self.real + other.real, self.imag + other.imag  # obj1.real + obj2.real, obj1.imag + obj2.imag

obj1 = Complex(1, 2)
obj2 = Complex(3, 4)
obj3 = obj1 + obj2  # calling the __add__() method from class using " + " operator

print(obj3)   # O/p : (4, 6)

#----------------------------------------------------------------

#  The < operator to compare two object's ages
# __lt__() overloads the < operator to compare the twp object.
# The __lt__() method returns,
# True - if the first object's age is less than the second object's age
# False - if the first object's age is greater than the second object's age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # overload < operator
    def __lt__(self, other):
        return self.age < other.age

p1 = Person("Alice", 20)
p2 = Person("Bob", 30)

print(p1 < p2)  # O/p: True
print(p2 < p1)  # O/p: False
