name = input("What is your name? ")
num_1, num_2 = input("Enter two numbers: ").split()
# split takes the first number and stores it in num_1, second to num_2
num_1 = int(num_1)
num_2 = int(num_2)
sum_1 = num_1 + num_2
difference = num_1 - num_2
product = num_1 * num_2
quotient = num_1 / num_2
remainder = num_1 % num_2

print("{} + {} = {}".format(num_1, num_2, sum_1))
print("{} - {} = {}".format(num_1, num_2, difference))
print("{} * {} = {}".format(num_1, num_2, product))
print("{} / {} = {}".format(num_1, num_2, quotient))
print("{} % {} = {}".format(num_1, num_2, remainder))

# problem: ask user to input number of miles
# convert to km
# print answer

miles = input("Enter the number of miles you are traveling with no commas: ")
miles = int(miles)
km = round(miles * 1.60934, 2)
print("You will travel {} kilometers".format(km))
