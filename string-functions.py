rand_string = "       this is an important string    "
rand_string = rand_string.strip()
# .strip() removes white space on right and left side
print(rand_string)
print(rand_string.capitalize())
print(rand_string.upper())
print(rand_string.lower())

a_list = ["bunch", "of", "strings"]
print(" ".join(a_list))

# delimeter = something used to separate data

a_list2 = rand_string.split()
for i in a_list2:
    print(i)

print("how many is: ", rand_string.count("is"))
print("where is: ", rand_string.replace(" an", " a kind of"))

# create an acronym generator
org_message = input("enter a message to be created into an acronym: ").upper()
# print(org_message)
word_list = list(org_message.split())
# print(word_list)
acro = ""
for word in word_list:
    # print(word)
    first = word[0]
    # print(first)
    acro += first
print(acro)

letter_z = "z"
print("is z a letter or number?", letter_z.isalnum())
print("is z a letter?", letter_z.isalpha())
print("is z a digit?", letter_z.isdigit())
print("is z a space?", letter_z.isspace())

# making a cesar cypher
message = input("enter your message: ")
key = int(input("how many characters should we shift? (1-26): "))
secret = ""
for char in message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key
        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            elif char_code < ord('A'):
                char_code += 26
            else:
                if char_code > ord('z'):
                    char_code -= 26
                elif char_code < ord('a'):
                    char_code += 26
        secret += chr(char_code)
    else:
        secret += char
print("encrypted: ", secret)

key = -key
message = ''
for char in secret:
    if char.isalpha():
        char_code = ord(char)
        char_code += key
        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            elif char_code < ord('A'):
                char_code += 26
            else:
                if char_code > ord('z'):
                    char_code -= 26
                elif char_code < ord('a'):
                    char_code += 26
        message += chr(char_code)
    else:
        message += char
print("decrypted: ", message)

