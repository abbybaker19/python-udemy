import math

def mult_divide(num_1, num_2):
    return (num_1 * num_2), (num_1 / num_2)


mult, divide = mult_divide(5, 4)
print(mult)
print(divide)


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def get_primes(max_number):
    list_primes = []
    for num_1 in range(2, max_number):
        if is_prime(num_1):
            list_primes.append(num_1)
    return list_primes


# max_num = int(input("Search for primes up to: "))
# primes = get_primes(max_num)
# for prime in primes:
#     print(prime)


# *args allows you to create a function with an undefined amount of arguments
def sum_all(*args):
    sum_1 = 0
    for i in args:
        sum_1 += i
    return sum_1


print("sum:", sum_all(1, 2, 3, 4, 5))


def get_area(shape):
    # routes to different functions depending on what the shape is
    shape = shape.lower()
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("please enter rectangle or circle")


def rectangle_area():
    length = float(input("enter the length of the rectangle: "))
    width = float(input("enter the width of the rectangle: "))
    area = length * width
    print("the area of the rectangle is {:.2f}".format(area))


def circle_area():
    radius = float(input("enter the radius of the circle: "))
    area = math.pi*(math.pow(radius, 2))
    print("the area of the circle is {:.2f}".format(area))


def main():
    shape_type = input("get area for what shape: ")
    get_area(shape_type)


main()
