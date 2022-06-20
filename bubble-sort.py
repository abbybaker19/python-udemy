# bubble sort:
# consists of an outer loop that decreases in size with each iteration
# goal is to have the largest number at the end of the list when the outer loop completes one cycle
# inner loop starts comparing indexes at the beginning of the loop
# check if list[i] > list[i + 1]
# if so, swap the index values
# when the inner loop completes, the largest number should be at the end of the list
# decrement the outer loop by 1

import random

rand_list = []
for i in range(5):
    rand_list.append(random.randrange(1, 9))
for i in rand_list:
    print(i, end="")

i = len(rand_list) - 1
while i > 1:
    j = 0
    while j < i:
        print("\nis {} > {}".format(rand_list[j], rand_list[j + 1]))
        print()
        if rand_list[j] > rand_list[j+1]:
            print("switch")
            temp = rand_list[j]
            rand_list[j] = rand_list[j+1]
            rand_list[j+1] = temp
        else:
            print("don't switch")
        j += 1
        for k in rand_list:
            print(k, end="")
        print()
    print("end of round")
    i -= 1
    for k in rand_list:
        print(k, end="")
    print()
