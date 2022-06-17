for i in [2, 4, 6, 8, 10]:
    print(i)

print()
for i in range(2, 6):
    print(i)

print()
i = 6
print("is 6 even?", (i % 2 == 0))

print()
for i in range (1, 21):
    if i % 2 != 0:
        print(i)

print()
your_float = float(input("enter a float: "))
print("rounded to 2 decimals: {:.2f}".format(your_float))

print()
# compounding interest example
investment = float(input("enter your initial investment amount: "))
interest = float(input("enter your expected interest rate: ")) * 0.01
years = int(input("enter a number of years: "))

for i in range(years):
    money = investment + (investment * interest)

print("investment after {} years: ${:.2f}".format(years, money))
