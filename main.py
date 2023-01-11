
# Python OOP Multilevel Inheritance.

# In Python, not only can we derive a class from the superclass but you can also derive a class from the derived class.
# This form of inheritance is known as multilevel inheritance.

# Syntax : class SuperClass:
#                Super class code here
#
#          class DerivedClass1(BaseClass):
#                 Derived class 1 code here
#
#          class DerivedClass2(DerivedClass1):
#                  Derived class 2 code here

class Gandfather:  # base class
    def talk_loud(self):
        print("Talking loudly.")
class Father(Gandfather):  # child1 derived class
    def waking(self):
        print("Waking early in the morning. ")

class Son(Father): # child2 derived class

    def eyes(self):
        print("Cute button eyes.")


# Create object
s1 = Son()
# Calling members of the base class
s1.talk_loud()
# Calling members of the child1 class
s1.waking()
# calling member of own class
s1.eyes()

# Output :
# Talking loudly.
# Waking early in the morning.
# Cute button eyes.