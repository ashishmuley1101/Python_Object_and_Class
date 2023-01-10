
# Python class Constructors using __init__() function.

# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are
# necessary to do when the object is being created.

# Syntax : class ClassName:
#                attributes ....(variables )
#                behaviour .....(methods)
#                def __init__(self,attributes...)  -----> class Constructor
#                        self.attributes = attributes


class Person:
    name = ""
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(f"My name is {p1.name} and my age is  {p1.age}")

p2 = Person("Jesrry", 32)

print(f"My name is {p2.name} and my age is {p2.age}")


# Output :
# My name is John and my age is  36
# My name is Jesrry and my age is 3