# try:
#     a_list = [1, 2, 3]
#     print(a_list[3])
# except IndexError:
#     print("index does not exist")
#
#
# # custom exceptions
# class DogNameError(Exception):
#     def __init__(self, *args, **kwargs):
#         Exception.__init__(self, *args, **kwargs)


# try:
#     dog_name = input("what is your dog's name? ")
#
#     if any(char.isdigit() for char in dog_name):
#         # Raise your own exception
#         # You can raise the built-in exceptions as well
#         raise DogNameError
#
# except DogNameError:
#     print("your dog's name cannot contain a number")

# finally and else
# finally - when you always want certain code to execute
# else - only executed if no exception is raised
# num1, num2 = input("enter two values to divide: ").split()
#
# try:
#     quotient = int(num1) / int(num2)
#     print("{} / {} = {}".format(num1, num2, quotient))
#
# except ZeroDivisionError:
#     print("cannot divide by 0")
#
# else:
#     print("you did not raise an exception")
#
# finally:
#     print("executes no matter what")

# 1. Create a file named mydata2.txt and put data in it
# 2. Using what you learned in part 8 and Google to find out how to open a file without with try to
# open the file in a try block
# 3. Catch the FileNotFoundError exception
# 4. In else print the file contents
# 5. In finally close the file
# 6. Try to open the nonexistent file mydata3.txt and test to see if you caught the exception

with open("mydata2.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("welcome to my random txt file\nmy dogs' names are ruby and ellie\nmy favorite color is blue")

try:
    my_file = open("mydata2.txt", encoding="utf-8")

except FileNotFoundError as ex:
    print("file not found")
    print(ex.args)

else:
    print(my_file.read())
    my_file.close()

finally:
    print("finished working with file")

