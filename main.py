
# Python Inheritance super() Method.

#  if we need to access the superclass method from the subclass, we use the super() method.


class Animal:
    name = ""

    def eat(self):
        print("I can eat")


# inherit from Animal
class Dog(Animal):

    # override eat() method
    def eat(self):   # Overriding the eat() of Animal class
        # call the eat() method of the superclass using * super() method *
        super().eat()

        print("I like to eat bones")


# create an object of the subclass
labrador = Dog()

labrador.eat()

# Output :
# I can eat
# I like to eat bones