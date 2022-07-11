import re

# groups and built in functions
# | to define matches you will accept

rand_str = "1. dog 2. cat 3. turtle"
regex = re.compile(r"\d\.\s(dog|cat)")
matches = re.findall(regex, rand_str)
print("matches:", len(matches))
for i in matches:
    print(i)

# create a regex that will match for 5 digit zip codes and disregard everything else
# sample output: "12345 12345-1234"
rand_str = "12345 12345-1234 1234 12345-333"
regex = re.compile(r"(\d{5}-\d{4}|\d{5}\s)")
matches = re.findall(regex, rand_str)
print("matches:", len(matches))
for i in matches:
    print(i)

# group - used to retrieve parts of regex matches
# bd = input("enter your birthday (mm-dd-yyyy): ")
# bd_regex = re.search(r"(\d{1,2})-(\d{1,2})-(\d{4})", bd)
# print("you were born on", bd_regex.group())
# print("birth month", bd_regex.group(1))
# print("birth day", bd_regex.group(2))
# print("birth year", bd_regex.group(3))

# match object functions
match = re.search(r"\d{2}", "the chicken weighed 13 lbs")
print("match:", match.group())
print("span:", match.span())
print("start:", match.start())
print("end:", match.end())

# named groups
rand_str = "april 19 2001"
regex = re.compile(r"^(?P<month>\w+)\s(?P<day>\d+)\s(?P<year>\d+)")
matches = re.search(regex, rand_str)
print("month:", matches.group('month'))
print("day:", matches.group('day'))
print("year:", matches.group('year'))

rand_str = "d+b@aol.com a_1@yahoo.co.uk A-100@m-b.INTERNATIONAL"
regex = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
matches = re.findall(regex, rand_str)
for i in matches:
    print(i)

rand_str = "14125551212 4125551212 (412)5551212 412 555 1212 412-555-1212 1-412-555-1212"
regex = re.compile(r"((1?)(-| ?)(\()?(\d{3})(\)|-| |\))?(\d{3})(-| )?(\d{4}|\d{4}))")
matches = re.findall(regex, rand_str)
for i in matches:
    print(i)
