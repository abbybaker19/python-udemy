# objects - have attributes and capabilities
# we store attributes in variables called fields
# then we model capabilities using functions called methods
# class - a blueprint we use to define an object's attributes (or fields and methods)

# class Dog: # defining the object's name
#     # initialization method - sets all values required when a new object is created
#     def __init__(self, name="", height=0, weight=0):
#         self.name = name    # assignments
#         self.height = height
#         self.weight = weight
#
#     # defining what happens when the dog is asked to demonstrate multiple capabilities
#     def run(self):
#         print("{} the dog runs".format(self.name))
#
#     def eat(self):
#         print("{} the dog eats".format(self.name))
#
#     def bark(self):
#         print("{} the dog barks".format(self.name))

# simulating a square
class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    # property keyword is used to define any call to a field that will execute a function
    @property
    def height(self):
        print("retrieving the height")
        return self.__height

    # setter keyword initializes a variable value
    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("please only enter numbers for height")

    @property
    def width(self):
        print("retrieving the width")
        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("please only enter numbers for width")

    def get_area(self):
        return int(self.__height) * int(self.__width)


# defining main method where we will call Dog
def main():
    # ruby = Dog("Ruby", 24, 51)
    # ruby.run()
    # ruby.eat()
    # ruby.bark()
    square = Square()
    height = input("enter height: ")
    width = input("enter width: ")
    square.height = height
    square.width = width
    print("height:", square.height)
    print("width:", square.width)
    print("the area is:", square.get_area())


# calling main function to execute
main()
