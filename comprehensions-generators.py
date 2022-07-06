import random
# list comprehensions - execute an expression against an iterable
# can act as a map as well as a filter all in one line of code

print(list(map((lambda x: x * 2), range(1, 11))))

# same thing using list comprehension:
print([2 * x for x in range(1, 11)])

# list of odds using filter:
print(list(filter((lambda x: x % 2 != 0), range(1, 11))))
# using list comprehension:
print([x for x in range(1, 11) if x % 2 != 0])

# value to the second power in range of 50, printing only multiples of 8
print([i ** 2 for i in range(50) if i % 8 == 0])

# using multiple for loops
print([x * y for x in range(1, 3) for y in range(11, 16)])

# putting list comprehensions in list comprehensions:
print([x for x in [i * 2 for i in range(10)] if x % 8 == 0])

# generate a list of 50 random values between 1 and 1000 and return those that are multiples of 9
print([x for x in [random.randint(1, 1001) for i in range(50)] if x % 9 == 0])

# working with multidimensional lists:
multi_list = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
print([col[1] for col in multi_list])
print([multi_list[i][i] for i in range(len(multi_list))])


# generator functions: returns a result generator when it is called, can be suspended and renewed throughout the program
# do not have to use all at one time
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        return True


def gen_prime(max_number):
    for num1 in range (2, max_number):
        if is_prime(num1):
            yield num1
            # yield indicates generator


prime = gen_prime(50)
print("prime:", next(prime))
print("prime:", next(prime))
print("prime:", next(prime))
print("prime:", next(prime))
print("prime:", next(prime))
print("prime:", next(prime))

# generator expressions: look just like list comprehension, but they return results once at a time and use ()
# can also iterate through all the results
double = (x * 2 for x in range(10))
print("double:", next(double))
print("double:", next(double))

for num in double:
    print(num)

