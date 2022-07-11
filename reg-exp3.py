# greedy and lazy matching

import re

# matching 0 or 1 of something
rand_str = "cat cats"
# + and ? say maybe this will be here, and maybe it won't
regex = re.compile("[cat]+s?")
matches = re.findall(regex, rand_str)
for i in matches:
    print(i)

# matching for 0 or more
rand_str = "doctor doctors doctor's"
regex = re.compile("[doctor]+['s]*")
matches = re.findall(regex, rand_str)
for i in matches:
    print(i)
# can do the same thing by setting an interval match
regex = re.compile("[doctor]+['s]{0,2}")
matches = re.findall(regex, rand_str)
for i in matches:
    print(i)

# create a regular expression that will grab each of the lines in this string and then print out the number of matches
# and each line
long_str = '''just some words
and some more\r
and more
'''
print("matches:", len(re.findall(r"[\w\s]+[\r]?\n", long_str)))
matches = re.findall("[\w\s]+[\r]?\n", long_str)
for i in matches:
    print(i)

# greedy vs lazy matching
# we want tp split the strings at the tags into 2 separate lines, but this does not give it to us
# how do we fix it?
rand_str = "<name>life on mars</name><name>freaks and geeks</name>"
# the * is greedy, which means it grabs the biggest match possible
regex = re.compile(r"<name>.*</name>")
matches = re.findall(regex, rand_str)
print("matches:", len(matches))
for i in matches:
    print(i)

# instead of the * we will use a ? to indicate we want to grab the smallest match possible
regex = re.compile(r"<name>.*?</name>")
matches = re.findall(regex, rand_str)
print("matches:", len(matches))
for i in matches:
    print(i)

# word boundaries
# use \b to define where the word starts or ends
rand_str = "ape at the apex"
regex = re.compile(r"ape")
regex2 = re.compile(r"\bape\b")
matches = re.findall(regex, rand_str)
matches2 = re.findall(regex2, rand_str)
print("matches 1:", len(matches))
print("matches 2:", len(matches2))
