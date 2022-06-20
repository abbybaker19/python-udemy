import random

# lists - allow you to refer to groups of data with only one name

rand_list = ["string", 1.234, 28]
one_to_ten = list(range(11))
rand_list = rand_list + one_to_ten
print(rand_list[0])
print("list length = ", len(rand_list))
first_3 = rand_list[0:3]
for i in first_3:
    print("{}:{}".format(first_3.index(i), i))

print(first_3[0]*3)
print("string" in first_3)
print("index of string: ", first_3.index("string"))

first_3[0] = "new string"
first_3.append("another string")
print()

# example problem
# generate a random list of 5 values between 1 and 9
rand_list = []
for i in range(5):
    rand_list.append(random.randrange(1, 9))

for i in rand_list:
    print(i)
print()

num_list = []
for i in range(5):
    num_list.append(random.randrange(1,9))

num_list.sort()
num_list.reverse()
num_list.insert(5, 3)
num_list.remove(3)
num_list.pop(2)

for j in num_list:
    print(j, end="")
print()
