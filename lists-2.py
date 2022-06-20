import math
even_list = [i*2 for i in range(10)]
for k in even_list:
    print(k, end=" ")
print()

print()

num_list = [1, 2, 3, 4, 5]
list_of_values = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)] for m in num_list]

for k in list_of_values:
    print(k)
print()

mult_d_list = [[0] * 10 for i in range(10)]
# mult_d_list[0][1] = 10
# print(mult_d_list[0][1])

for i in range(10):
    for j in range(10):
        mult_d_list[i][j] = "{} : {}".format(i, j)

for i in range(10):
    for j in range(10):
        print(mult_d_list[i][j], end=" || ")
    print()

print()
# use two for loops to fill in the cells and make a multiplication table
mult_table = [[0] * 10 for i in range(10)]
for i in range(1, 10):
    for j in range(1, 10):
        mult_table[i][j] = i * j

for i in range(1, 10):
    for j in range(1, 10):
        print(mult_table[i][j], end="   ")
    print()
