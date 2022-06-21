def factorial(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial(num - 1)
        return result


print(factorial(4))


# fibonacci example
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = fibonacci(num - 1) + fibonacci(num - 2)
        return result


print(fibonacci(2))

# fibonacci asking user how many numbers they want and displaying them
amount = int(input("how many fibonacci values should be found? "))
i = 1
while i < amount:
    fib = fibonacci(i)
    print(fib)
    i += 1

