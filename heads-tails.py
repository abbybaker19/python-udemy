import random

flip_list = []
for i in range(1, 101):
    flip_list += random.choice(['H', 'T'])

print("heads:", flip_list.count('H'))
print("tails:", flip_list.count('T'))
