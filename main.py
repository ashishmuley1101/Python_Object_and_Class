
# Python OOP Single Inheritance.

# Inheritance is a way of creating a new class for using details of an existing class without modifying it.
# The newly formed class is a derived class (or child class). Similarly,
# the existing class is a base class (or parent class).

# Syntax : class ParentClass:
#                attributes ....(variables )
#                behaviour .....(methods)

#          class ChildClass(ParentClass)
#                attributes ....(variables )
#                behaviour .....(methods)



class Animal:  # base class
    def eat(self):
        print("I can eat!")

    def sleep(self):
        print("I can sleep!")

class Dog(Animal):  # derived class

    def bark(self):
        print("I can bark! Woof woof!!")


# Create object of the Dog class
dog1 = Dog()

# Calling members of the base class
dog1.eat()
dog1.sleep()

# Calling member of the derived class
dog1.bark()

# Output :
# I can eat!
# I can sleep!
# I can bark! Woof woof!!