def mult2(num):
    return num * 2


times_two = mult2
print("4 * 2 =", times_two(4))


def do_math(func, num):
    return func(num)


print("8 * 2 =", do_math(mult2, 8))


def get_func(num):
    def mult_by(value):
        return num * value

    return mult_by


gen_func = get_func(5)
print("5 * 9 =", gen_func(9))

list_func = [times_two, gen_func]
print("5 * 9 =", list_func[1](9))

# create a function that receives a list and a function
# the function passed will return true or false if a list value is odd
# the surrounding function will return a list of odd numbers


def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def change_list(list, func):
    odd_list = []
    for i in list:
        if func(i):
            odd_list.append(i)
    return odd_list


a_list = range(1, 20)
print(change_list(a_list, is_it_odd))


# function annotations
def random_func(name: str, age: int, height: float) -> str:
    print("name:", name)
    print("age:", age)
    print("height:", height)
    return "{} is {} years old and is {} inches tall".format(name, age, height)


print(random_func("abby", 21, 68.1))

print(random_func.__annotations__)
