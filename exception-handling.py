import random

while True:
    try:
        number = int(input("please enter a number: "))
        break
    except ValueError:
        print("you did not enter a number")
print("thank you for entering a number")

# do {...} while {...} problem example
# guessing game
# sample output:
# guess a number between 1 and 10: 1
# guess a number between 1 and 10: 3
# you guessed it

answer = random.randrange(1, 11)
while True:
    try:
        guess = int(input("guess a number between 1 and 10: "))
        if guess == answer:
            print("you guessed it")
            break
    except ValueError:
        print("you did not enter a number")


# float accuracy
# decimal module

from decimal import Decimal as D
sum = D(0)
sum += D("0.01")
sum += D("0.01")
sum += D("0.01")
sum -= D("0.03")
print("sum = ", sum)
