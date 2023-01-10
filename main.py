
# Python class Methods.

# The define a function inside a Python class called behaviour(methods) of that class.
# Syntax : class ClassName:
#                attributes ....(variables )
#                behaviour .....(methods)

class Room:
    length = 0.0
    breadth = 0.0

    # method to calculate area
    # The self parameter is a reference to the current instance of the class, and is used to access
    # variables that belongs to the class.
    # it has to be the first parameter of any function in the class
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)


# create object of Room class
study_room = Room()

# assign values to all the attributes
study_room.length = 42.5
study_room.breadth = 30.8

# access method inside class
study_room.calculate_area()

# Output :
# Area of Room = 1309.0