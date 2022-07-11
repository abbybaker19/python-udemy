# matching data

import re

# . matches any character or space
# use backslash to match .
rand_str = "F.B.I. I.R.S. CIA"
print("matches:", len(re.findall(".\..\..", rand_str)))

# matching white space
rand_str = """This is a long
string that goes
on for many lines"""
print(rand_str)
regex = re.compile("\n")
rand_str = regex.sub(" ", rand_str)
print(rand_str)

# can also match for backspaces, form feeds, carriage returns, tabs, and vertical tabs by using
# \b, \f, \r, \t

# matching a single number
rand_str = "12345"
# \d [0-9]
# \D [^0-9]
print("matches:", len(re.findall("\d", rand_str)))

# multiple different numbers
if re.search("\d{5}", rand_str):
    print("it is a zip code")

# match within a range
rand_str = "123 12345 123456 1234567"
print("matches:", len(re.findall("\d{5,7}", rand_str)))

# matching for any single letter or number
# \w matches for [a-zA-Z0-9]
# \W matches for [^a-zA-Z0-9]
phone = "412-555-1212"
# creating a regex to check if this is a phone number or not
if re.search("\w{3}-\w{3}-\w{4}", phone):
    print("it is a phone number")

if re.search("\w{2,20}", "rocketman"):
    print("it is a valid name")

# matching for whitespace
# \s [\f\n\r\t\v]
# \S [^\f\n\r\t\v]
if re.search("\w{2,20}\s\w{2,20}", "abby baker"):
    print("it is a valid name")

# matching for one or more
# + to match for one or more
print("matches:", len(re.findall("a+", "a as ape bug")))

# checking email addresses:
# 1-20 lowercase and uppercase letters, numbers, plus ._%=-
# an @ symbol
# 2-20 lowercase and uppercase letters, numbers, plus .-
# a period
# 2-3 lowercase and uppercase letters
email_list = "db@aol.com m@.com @apple.com db@.com"
print("email matches:", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", email_list)))

