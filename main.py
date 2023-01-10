
# Python Class and Objects

# The class keyword to create a class in Python.
# Syntax : class ClassName:
#                attributes ....(variables )
#                behaviour .....(methods)

# define a class
class Bike:
    name = ""   # initialized  with empty string
    gear = 0    # initialized  with 0

# create object of Bike class
bike1 = Bike()

# access class attributes and assign new values using the object.
bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear} ")

# Output :
# Name: Mountain Bike, Gears: 11