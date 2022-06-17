drink = input("diet coke or pepsi: ")
if drink == "diet coke":
    print("here is your diet coke")
elif drink == "pepsi":
    print("here is your pepsi")
else:
    print("here is your water")

num_1, operator, num_2 = input("Enter a simple math problem with one operator: ").split()
num_1 = int(num_1)
num_2 = int(num_2)

if operator == "+":
    answer = num_1 + num_2
    print(num_1, operator, num_2, "=", answer)
elif operator == "-":
    answer = num_1 - num_2
    print(num_1, operator, num_2, "=", answer)
elif operator == "*":
    answer = num_1 * num_2
    print(num_1, operator, num_2, "=", answer)
elif operator == "/":
    answer = num_1 / num_2
    print(num_1, operator, num_2, "=", answer)
else:
    print("invalid input. please try again")

age = int(input("enter your age: "))
if (age >= 1) and (age <= 18):
    print("you are a minor")
elif (age == 21) or (age == 50):
    print("u are old")
elif not age < 65:
    print("these responses are very random")

age = int(input("enter your age: "))
if age < 5:
    print("too young for school")
elif age == 5:
    print("go to kindergarten")
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("go to grade {} school".format(grade))
else:
    print("go to college")

# ternary operator:
# condition_true if condition else condition_false
age = int(input("enter your age: "))
can_vote = True if age >= 18 else False
print("you can vote: ", can_vote)