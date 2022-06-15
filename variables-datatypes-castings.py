import sys

age = 21
name = "Abby"

print("Hello", name)

'''
Multiline
Comment
'''

str1 = "\"This is a quote\""
# \ = escape char

'''
new line: \n
backslash: \\
single quote: \'
backspace: \b
tab: \t
'''

# integer = values without decimal
# float = values with decimal
# complex =

print(sys.maxsize)
print(sys.float_info.max)
f1 = 1.111111111111111
f2 = 1.111111111111111
f3 = f1+f2
print(f3)

can_vote = True

print("cast", type(int(5.4)))
print("cast", type(str(5.4)))
print("cast", type(chr(97)))
print("cast", type(ord('a')))
print("cast", type(float(2)))

# note that var names are case sensitive

num_1 = "1"
num_2 = "2"
print("1 + 2 =", (int(num_1) + int(num_2)))
