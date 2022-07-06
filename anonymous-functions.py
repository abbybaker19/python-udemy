import random
from functools import reduce
# lambda - used when you need a small function but don't want to junk up your code with temporary function names that
# could cause conflicts

sum_1 = lambda x, y: x + y

print("sum:", sum_1(4, 5))

can_vote = lambda age: True if age >= 18 else False
print("can vote:", can_vote(16))

power_list = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]

for func in power_list:
    print(func(4))

attack = {'quick': (lambda: print("quick attack")),
          'power': (lambda: print("power attack")),
          'miss': (lambda: print("attack missed"))}

attack['quick']()


attack_key = random.choice(list(attack.keys()))
attack[attack_key]()


# map - allows you to execute a function on each item in a list
one_to_10 = range(1, 11)


def dbl_num(num):
    return num * 2


print(list(map(dbl_num, one_to_10)))
print(list(map((lambda x: x * 3), one_to_10)))

a_list = list(map((lambda x, y: x + y), [1, 2, 3], [1, 2, 3]))
print(a_list)

# filter - selects items based on a function
print(list(filter((lambda x: x % 2 == 0), range(1, 11))))

# finding the multiples of 9 from a random 100 value list w values between 1 and 1000
values = []
for i in range(1, 101):
    i = random.randint(1, 1001)
    values.append(i)

print(list(filter((lambda x: x % 9 == 0), values)))

# reduce - receives a list and returns a single result
print(reduce((lambda x, y: x + y), range(1, 6)))

