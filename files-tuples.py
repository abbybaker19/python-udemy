import os
# module that allows you to work with files

# with open ensures the files will be closed if the program crashes
# mydata.txt is the file to open - if it does not already exist it will be created
# mode="w" allows you to open the file with writing permission - can also open with a for
# appending which takes you to the end of the file
# encoding means unicode will be used
# as my_file tells computer what name you're referencing the file as
# with open("mydata.txt", mode="w", encoding="utf-8") as my_file:
#     my_file.write("some random text\nmore random text\nand some more")

# reading the file
# not putting the mode here because it defaults to reading, so we do not need to specify
# with open("mydata.txt", encoding="utf-8") as my_file:
#     print(my_file.read())

# os.rename("mydata.txt", "mydata2.txt")
# os.remove("mydata2.txt")
# os.mkdir("directory")
# os.chdir("directory")
# print("current directory", os.getcwd())
# os.chdir("..")
# os.rmdir("mydir") to remove directory

# with open("mydata2.txt", encoding="utf-8") as my_file:
#     line_num = 1
#     while True:
#         line = my_file.readline()
#         if not line:
#             break
#         print("line", line_num, ":", line, end="")
#         line_num += 1

# problem
# sample output:
# line 1
# number of words: 3
# avg word length: 4.7
# line 2
# number of words: 3
# avg word length: 4.7

# with open("mydata2.txt", encoding="utf-8") as my_file:
#     line_num = 1
#     while True:
#         line = my_file.readline()
#         if not line:
#             break
#         print("line", line_num)
#         word_list = line.split()
#         print("number of words: ", len(word_list))
#         char_count = 0
#         for word in word_list:
#             for char in word:
#                 char_count += 1
#         avg_char = char_count / len(word_list)
#         print("avg word length: {:.2f}".format(avg_char))
#         line_num += 1
#         print()


# tuples - basically a list, but once it's created the values cannot be changed. also use ()
my_tuple = (1, 2, 3, 4, 5)
print("1st value:", my_tuple[0])
print(my_tuple[0:3])
print("length:", len(my_tuple))
more_fibs = my_tuple + (13, 21, 34)
print("34 in tuple:", 34 in more_fibs)
for i in more_fibs:
    print(i)
a_list = [55, 89, 144]
a_tuple = tuple(a_list)
a_list = list(a_tuple)
print("max:", max(a_tuple))
print("min:", min(a_tuple))
