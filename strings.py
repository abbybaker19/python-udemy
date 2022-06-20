# string = series of characters between quotes
print(type("34hsy6"))
print(type(3))
print(type(4.603920))

samp_string = "this is a very important string"
print(len(samp_string))
print(samp_string[17])
print(samp_string[-1])
print(samp_string[0:10])
print("every other: ", samp_string[0:-1:2])

print("green " + "eggs")
print("hello " * 5)

num_string = str(4)
for char in samp_string:
    print(char)

for i in range(0, len(samp_string)-1, 2):
    print(samp_string[i] + samp_string[i+1])

# unicodes
# A - Z have unicode values of 65-90
# a - z have unicode values of 97-122
# ord function gives the unicode value
print("A =", ord("A"))
# can also convert from unicode using chr function
print("65 =", chr(65))

# problem
# receive an upper case string
# convert to unicode
# translate back into original message

message = input("input a message: ").upper().replace(" ", "")
unicode = ""
for char in message:
    unicode += str(ord(char))
print("encoded message: ", unicode)
new_message = ""
for i in range(0, len(unicode)-1, 2):
    char_code = unicode[i] + unicode[i+1]
    new_message += chr(int(char_code))
print("original message: ", new_message)
