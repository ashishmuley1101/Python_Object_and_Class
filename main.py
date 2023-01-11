
# Python Multiple Inheritance.

# A class can be derived from more than one superclass in Python. This is called multiple inheritance.

# Syntax : class SuperClass1:
#                features of SuperClass1
#          class SuperClass2:
#                features of SuperClass2
#          class MultiDerived(SuperClass1, SuperClass2):
#                features of SuperClass1 + SuperClass2 + MultiDerived class

class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")

class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")

class Bat(Mammal, WingedAnimal):
    pass

# create an object of Bat class
b1 = Bat()

# Calling the methods from super classes
b1.mammal_info()
b1.winged_animal_info()

# Output :
# Mammals can give direct birth.
# Winged animals can flap.