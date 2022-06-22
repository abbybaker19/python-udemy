# static methods - allow access without the need to initialize a class

# class Sum:
#     @staticmethod
#     # decorator that defines the method as static
#     def get_sum(*args):
#         sum_1 = 0
#         for i in args:
#             sum_1 += i
#
#         return sum_1

# static variables - fields that are declared in a class but outside any method
# their value will be shared by every object of that class

# class Dog:
#     num_dogs = 0
#
#     def __init__(self, name="unknown"):
#         self.name = name
#         Dog.num_dogs += 1
#
#     @staticmethod
#     def get_num_dogs():
#         print("there are currently {} dogs".format(Dog.num_dogs))
#
#
# def main():
#     # print("sum:", Sum.get_sum(1, 2, 3, 4, 5))
#     ruby = Dog("ruby")
#     ellie = Dog("ellie")
#     ruby.get_num_dogs()
#     ellie.get_num_dogs()
#
#
# main()


# modules
# import sum
#
# print("sum:", sum.get_sum(1, 2, 3, 4, 5))

from sum import get_sum

print("sum:", get_sum(1, 2, 3, 4, 5))
