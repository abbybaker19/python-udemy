def add(x, y):
    return x + y


print(add(3, 9))


def change_name():
    global gbl_name
    gbl_name = "Matthew"


gbl_name = "Natalie"
change_name()
print(gbl_name)


def is_float(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False


pi = 3.141595326
print(is_float(pi))

# solve for x in an algebraic equation
# sample
# print(solver("x + 4 = 9")
# x = 5


def solver(eqn):
    x, ad, y, eq, z = eqn.split()
    # print(x, ad, y, eq, z)
    y = int(y)
    z = int(z)
    ans = z - y
    return "{} {} {}, {} {} {} {} {}".format(x, eq, ans, ans, ad, y, eq, z)
    # OR x, add, num_1, equal, num_2 = equation.split()
    # num_1, num_2 = int(num_1), int(num_2)
    # return "x = " + str(num_1 - num_2)


print(solver("x + 5 = 11"))
