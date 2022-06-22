# magic methods - allow you to define how objects of the same type can be compared
# will also allow you to define what happens when mathematical operations are performed on your objects

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return"{}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)

    def __add__(self, other_time):
        new_time = Time()
        if (self.second + other_time.second) >= 60:
            self.minute += 1
            new_time.second = (self.second + other_time.second) - 60
        else:
            new_time.second = self.second + other_time.second

        if (self.minute + other_time.minute) >= 60:
            self.hour += 1
            new_time.minute = (self.minute + other_time.minute) - 60
        else:
            new_time.minute = self.minute + other_time.minute

        if (self.hour + other_time.hour) >= 24:
            new_time.hour = (self.hour + other_time.hour) - 24
        else:
            new_time.hour = self.hour + other_time.hour

        return new_time

# magic method examples:
# __eq__ : equal
# __ne__ : not equal
# __lt__ : less than
# __gt__ : greater than
# __le__ : less than or equal to
# __ge__ : greater than or equal to
# __add__ : addition
# __sub__ : subtraction
# __mul__ : multiplication
# __div__ : division
# __mod__ : modulus


def main():
    time1 = Time(1, 20, 30)
    print(time1)
    time2 = Time(24, 41, 30)
    print(time1 + time2)


main()
