# regular expressions - allow you to locate and change strings
# work almost the same way in every programming language
# allows you to find any string in a large amount of data, verify format, find and replace data, and format

import re

# searching for an exact string match:
if re.search("ape", "the ape was at the apex"):
    print("there is an ape")

all_apes = re.findall("ape", "the ape was at the apex")
for i in all_apes:
    print(i)

the_str = "the ape was at the apex"
for i in re.finditer("ape.", the_str):
    loc_tuple = i.span()
    print(loc_tuple)
    print(the_str[loc_tuple[0]:loc_tuple[1]])

animal_str = "cat rat mat fat pat"
all_animals = re.findall("[Crmfp]at", animal_str)
# can also use "[^Cr]at" to search for everything except C and r
# can also use "[c-mC-M]at" to search for lowercase c through m and uppercase C through M
for i in all_animals:
    print(i)

# replacing matches:
owl_food = "rat cat mat pat"

# compiling an re into a pattern object:
regex = re.compile("[cr]at")
owl_food = regex.sub("owl", owl_food)
print(owl_food)

# \ and solving \ problems
# use r to indicate a raw string
rand_str = "here is \\stuff"
print("find \\stuff:", re.search(r"\\stuff", rand_str))


