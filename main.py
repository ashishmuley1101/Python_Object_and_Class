
# Python OOP Encapsulation.

# Encapsulation prevents outer classes from accessing and changing attributes and methods of a class.
# This also helps to achieve data hiding.
# In Python, we denote private attributes using underscore as the prefix i.e single _ or double __.


class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()


# Output :
# Selling Price: 900
# Selling Price: 900
# Selling Price: 1000

#----------------------------------------------------------------

#  Creating a base class
class Base:
     def __init__(self):
     # Protected member
        self._a = 2

# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling protected member of base class: ",
              self._a)

        # Modify the protected variable:
        self._a = 3
        print("Calling modified protected member outside class: ",
              self._a)


obj1 = Derived()

obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)

# Output :
# Calling protected member of base class:  2
# Calling modified protected member outside class:  3
# Accessing protected member of obj1:  3
# Accessing protected member of obj2:  2