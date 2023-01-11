
# Python OOP Polymorphism.

# Polymorphism means more than one form.
# The same entity (method or operator or object) can perform different operations in different scenarios.

class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")

class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

class Ostrich(Bird):

    def flight(self):
        print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = Sparrow()
obj_ost = Ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

# Output :
# There are many types of birds.
# Most of the birds can fly but some cannot.
# There are many types of birds.
# Sparrows can fly.
# There are many types of birds.
# Ostriches cannot fly.