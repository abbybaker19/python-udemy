# iterables - a stored sequence of values (or a list); has an __iter__ method
# iterator - object with a __next__ method

# convert to iterator:
samp_str = iter("sample")

print("char:", next(samp_str))
print("char:", next(samp_str))


# custom iterable
class Alphabet:
    def __init__(self):
        self.letters = "abcdefghijklmnopqrstuvwxyz"
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.letters) - 1:
            raise StopIteration
        self.index += 1
        return self.letters[self.index]


alpha = Alphabet()
for letter in alpha:
    print(letter)

abby = {"f_name": "abby", "l_name": "baker"}
for key in abby:
    print(key, abby[key])


# create a class that returns values from a fibonacci sequence each time next is called
class FibGenerator:
    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        fib_num = self.first + self.second
        self.first = self.second
        self.second = fib_num
        return fib_num


fib_seq = FibGenerator()

for i in range(10):
    print("fib:", next(fib_seq))
