# week 5 exploration notes

import pickle
import json

# # r opens a file for writing
# infile = open('dogs.txt', 'r')  # There's nothing special about the extension ".txt"
#
# # Once you've opened the file, you can read the first line like this:
# line = infile.readline()
# # strip() removes EOL characters
# line_stripped = line.strip()
# # When we're done reading from the file, we need to close it.
# infile.close()
#
# # can also do this to make sure the file gets closed
# infile = open('dogs.txt', 'r')
# try:
#     line = infile.readline()
# finally:
#     infile.close()
#
# # but this works better - automatically closes the file when it's done reading
# with open('dogs.txt', 'r') as infile:
#     text = infile.readline()
#
# # iteration (for printing for example) like this
# with open('dogs.txt', 'r') as infile:
#     for line in infile:
#         print(line.strip())
#
# # Can do file exception this way
# try:
#     with open('dogs.txt', 'r') as infile:
#         for line in infile:
#             print(line.strip())
# except FileNotFoundError:
#     print("The file was not found.")
#
# # writing to a file is done this way - w instead of a - CAUTION this overwrites the file if it exists
# cat_list = ['Siamese', 'Manx', 'Abyssinian', 'Savannah', 'Ragdoll']
#
# with open('cats.txt', 'w') as outfile:
#     for cat in cat_list:
#         outfile.write(cat + '\n')
#
# # non-text must be converted to a string before writing - ex: numbers
# with open('nums.txt', 'w') as outfile:
#     for num in range(10):
#         outfile.write(str(num) + '\n')
#
# # This will append to the previous created file
# with open('nums.txt', 'a') as outfile:
#     for num in range(15):
#         outfile.write(str(num) + '\n')
#
# with open('nums.txt') as infile:
#     for line in infile:
#         print(line.strip())
#
# # Since not everything written to disk will be text
# #       lists, dictionaries, objects etc
# # we "pickle" the data to the disk
# # This requires 'import pickle' to work
# # The wb is for write binary
# # Use pickle.dump(filename, var)
# cat_list = ['Siamese', 'Manx', 'Abyssinian', 'Savannah', 'Ragdoll']
# with open('cats.pkl', 'wb') as outfile:
#     pickle.dump(cat_list, outfile)
#
# # to read the pickled file, use rb (read binary) and pickle.load(var)
# with open('cats.pkl', 'rb') as infile:
#     restored_list = pickle.load(infile)
#
# print(cat_list)
# print(restored_list)
# print(f"Cat_list == restored_list: {cat_list == restored_list}")
# print(f"Cal_list is restored_list: {cat_list is restored_list}")
#
# # working with JSON (JavaScript Object Notation)
# # pickle is used for working entirely in python
# # JSON is used to share data/information between multiple platforms/languages
# # requires import json at the top of the file
# cat_list = ['Siamese', 'Manx', 'Abyssinian', 'Savannah', 'Ragdoll']
# with open('cats.json', 'w') as outfile:  # just 'w' since it's a text file
#     json.dump(cat_list, outfile)
#
# with open('cats.json', 'r') as infile:  # just 'r' since it's a text file
#     restored_list = json.load(infile)
#
# with open('SuperSquad.json', 'r') as infile:
#     squad = json.load(infile)
#
# print(f"The imported json file has a type of: {type(squad)}")
# print(squad["members"][1]["powers"][2])

infile = open('Mary.txt', 'w')
line_1 = "Mary had a little lamb"
line_2 = "Its fleece was white as snow."
line_3 = "And everywhere that Mary went,"
line_4 = "The lamb was sure to go."
with open('Mary.txt', 'a') as outfile:
    outfile.write(line_1 + '\n')
    outfile.write(line_2 + '\n')
    outfile.write(line_3 + '\n')
    outfile.write(line_4 + '\n')

infile = open('Mary.txt', 'r')
for x in infile:
    print(x.strip())

new_dict = {
1:"William",
2:"Patrick",
3:"Jon",
4:"Tom",
5:"Peter",
6:"Colin",
7:"Sylvester",
8:"Paul",
9:"Chris",
10:"David",
11:"Matt",
12:"Peter",
13:"Jodie"
}

with open("names.pkl",'wb') as outfile:
    pickle.dump(new_dict, outfile)   # Make sure this is the variable name and not the file name, then outfile

# names = {}
with open('names.pkl', 'rb') as infile:
    names = pickle.load(infile)

print(f"The type of new_dict is {type(new_dict)}")
print(f"The type of names is {type(names)}")
print(names)

with open("names.json", 'w') as outfile:
    json.dump(new_dict, outfile)

with open("names.json", 'r') as infile:
    restored_dict = json.load(infile)

print(restored_dict)
