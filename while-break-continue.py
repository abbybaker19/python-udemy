import random

rand_num = random.randrange(1, 51)
i = 1

while i != rand_num:
    i += 1
print("the random value is: ", rand_num)

i = 1
while i <= 20:
    if (i % 2) == 0:
        i += 1
        continue
    if i == 15:
        break
    print("odd: ", i)
    i += 1

# draw a pine tree after asking the user for a number of rows
# sample:
# how tall is the tree? 5
    #
   ###
  #####
 #######
#########
    #

layers = int(input("how many layers does the tree have? "))
spaces = layers - 1
hashes = 1
stump_spaces = layers - 1
while layers != 0:
    for i in range(spaces):
        print(' ', end="")
    for i in range(hashes):
        print('#', end="")
    print()
    spaces -= 1
    hashes += 2
    layers -= 1
for i in range(stump_spaces):
    print(' ', end="")
print("#")
