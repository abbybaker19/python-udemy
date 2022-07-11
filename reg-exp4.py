import re

# ^: matches the beginning of a string
# $: matches the end of a string

# everything before @
rand_str = "match everything up to @"
regex = re.compile(r"^.*[^@]")
matches = re.findall(regex, rand_str)
print("matches:", len(matches))
for i in matches:
    print(i)

# everything after @
rand_str = "@ get this string"
regex = re.compile(r"[^@\s].*$")
matches = re.findall(regex, rand_str)
print("matches:", len(matches))
for i in matches:
    print(i)

# grabbing the first word from each line
rand_str = '''ape is big
turtle is slow
cheetah is fast
'''
regex = re.compile(r"(?m)^.*?\s")
matches = re.findall(regex, rand_str)
print("matches:", len(matches))
for i in matches:
    print(i)

# subexpressions - parts of a larger expression

# grabbing only 555-1212
# surround want you want with ()
rand_str = "my number is 412-555-1212"
regex = re.compile(r"412-(.*)")
matches = re.findall(regex, rand_str)
print("matches:", len(matches))
for i in matches:
    print(i)

# getting only the numbers without the area codes from a string
rand_str = "412-555-1212 412-555-1213 412-555-1214"
# bracket index allows you to get the 8 characters without the area code
regex = re.compile(r"412-(.{8})")
matches = re.findall(regex, rand_str)
print("matches:", len(matches))
for i in matches:
    print(i)

# multiple subexpressions
# getting only 555 and then only 1212
rand_str = "my number is 412-555-1212"
regex = re.compile(r"412-(.*)-(.*)")
matches = re.findall(regex, rand_str)
print("matches:", len(matches))
print(matches[0][0], matches[0][1])
