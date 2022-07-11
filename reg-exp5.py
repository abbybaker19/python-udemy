# back references, look ahead/behind

import re
from functools import reduce

# back reference - allows you to reuse the expression that precedes it

rand_str = "the cat cat fell out the window"
regex = re.compile(r"(\b\w+)\s+\1")
matches = re.findall(regex, rand_str)
print("matches:", len(matches))
for i in matches:
    print(i)

# back reference substitutions:
rand_str = "<a href='#><b>the link</b></a>"
# grabbing only the text within the bold tags
regex = re.compile(r"<b>(.*?)</b>")
rand_str = re.sub(regex, r"\1", rand_str)
print(rand_str)

# matching the phone number using multiple subexpressions
rand_str = "412-555-1212"
regex = re.compile(r"([\d]{3})-([\d]{3}-[\d]{4})")
# change output as (412)555-1212
rand_str = re.sub(regex, r"(\1)\2", rand_str)
print(rand_str)

rand_str = "https://www.youtube.com http://www.google.com"
# <a href='https://www.youtube.com'>www.youtube.com</a>
# <a href='http://www.google.com'>www.google.com</a>
# grab the url and provide the above output using back referencing and substitution
regex = re.compile(r"(https?://([\w.]+))")
rand_str = re.sub(regex, r"<a href='\1'>\2</a>\n", rand_str)
print(rand_str)

# lookaheads - defining a pattern to match but not return
# (?=expressions)
rand_str = "one two three four"
# grab all letters and numbers of one or more that are separated by a word boundary but don't include it
regex = re.compile(r"\w+(?=\b)")
matches = re.findall(regex, rand_str)
print("matches:", len(matches))
for i in matches:
    print(i)

# look behind - looks for what is before the text to return, but does not return it
# (?<=expression)
# getting the words after the numbers but no numbers
rand_str = "1. bread 2. apple 3. lettuce"
regex = re.compile(r"(?<=\d.\s)\w+")
matches = re.findall(regex, rand_str)
print("matches:", len(matches))
for i in matches:
    print(i)

# look ahead and behind
rand_str = "<h1>i am important</h1> <h1>i am too</h1>"
regex = re.compile(r"(?<=<h1>).+?(?=</h1>)")
matches = re.findall(regex, rand_str)
print("matches:", len(matches))
for i in matches:
    print(i)

# negative look ahead and behind
# (?!expression) ahead
# (?<!expression) behind
rand_str = "8 apples $3, 1 bread $1, 1 cereal $4"
# total grocery items by ignoring the $
regex = re.compile(r"(?<!\$)\d+")
matches = re.findall(regex, rand_str)
print("matches:", len(matches))
for i in matches:
    print(i)

matches = [int(i) for i in matches]
print("total items: {}".format(reduce((lambda x, y: x + y), matches)))
