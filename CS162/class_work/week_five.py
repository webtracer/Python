# # Week 5 - File handling, Pickling, JSON
#
# # r is for reading the file, w is for writing the file
# infile = open('dogs.txt', 'r')  # There's nothing special about the extension ".txt"
#
# # Once you've opened the file, you can read the first line like this:
#
# # This line pulls the entire line in, newline character and all
# line = infile.readline()
#
# # .strip() removes the extraneous stuff and returns the text
# line_stripped = line.strip()
#
# # When we're done reading from the file, we need to close it.
# infile.close()
#
# # can also do it this way
# infile = open('dogs.txt', 'r')
# try:
#     line = infile.readline()
# finally:
#     infile.close()
#
# # but this way is better
# with open('dogs.txt', 'r') as infile:
#     text = infile.readline()
#     print(text)
#
# # this will print out the file, stripping the extraneous stuff
# with open('dogs.txt', 'r') as infile:
#     for line in infile:
#         print(line.strip())
#
# # To catch errors with the file name or access
# try:
#     with open('dogs.txt', 'r') as infile:
#         for line in infile:
#             print(line.strip())
# except FileNotFoundError:
#     print("The file was not found")
#
# # to write to a file, we do this
# cat_list = ['Siamese', 'Manx', 'Abyssinian', 'Savannah', 'Ragdoll']
#
# with open('cats.txt', 'w') as outfile:
#     for cat in cat_list:
#         outfile.write(cat + '\n')
#
# # Concatenating with the newline character advances us to the next line of the file. We don't have to worry about
# # handling a FileNotFoundError. If the file doesn't exist, it will be created. If the file does exist,
# # it will be overwritten by the new contents.
#
# # The argument passed to the write method must be a string. This includes integers etc
# with open('nums.txt', 'w') as outfile:
#     for num in range(10):
#         outfile.write(str(num) + '\n')
#
# # If we want to append to the file instead of overwriting the contents, replace w with a
# with open('nums.txt', 'a') as outfile:
#     for num in range(5):
#         outfile.write(str(num) + '\n')
#
# with open('nums.txt', 'r') as infile:
#     for line in infile:
#         print(line.strip())
#

# def find_gold(maze, position):
#     """
#     maze is a list of lists that represents a square maze
#     ' ' is an empty square
#     '#' is a wall
#     'G' is where the gold is hidden
#     position is a tuple of the current row and column
#
#     returns a list of coordinates that leads to the gold
#     """
#     row, col = position  # tuple unpacking
#     if row < 0 or row >= len(maze):  # base case for row out of bounds
#         return None
#     if col < 0 or col >= len(maze[row]):  # base case for column out of bounds
#         return None
#     if maze[row][col] == '#':  # base case for hitting a wall
#         return None
#     if maze[row][col] == '.':  # base case for repeating a position
#         return None
#     if maze[row][col] == 'G':  # base case for finding the goal
#         return [(row, col)]
#
#     maze[row][col] = '.'  # mark current square to avoid revisiting
#     partial_route = find_gold(maze, (row-1, col))  # try "up"
#     if partial_route is not None:
#         maze[row][col] = ' '  # unmark current square
#         return [(row, col)] + partial_route
#     partial_route = find_gold(maze, (row+1, col))  # try "down"
#     if partial_route is not None:
#         maze[row][col] = ' '  # unmark current square
#         return [(row, col)] + partial_route
#     partial_route = find_gold(maze, (row, col-1))  # try "left"
#     if partial_route is not None:
#         maze[row][col] = ' '  # unmark current square
#         return [(row, col)] + partial_route
#     partial_route = find_gold(maze, (row, col+1))  # try "right"
#     if partial_route is not None:
#         maze[row][col] = ' '  # unmark current square
#         return [(row, col)] + partial_route
#     maze[row][col] = ' '  # unmark current square
#
#
# maiz = [[' ', '#', ' ', ' ', ' ', '#'],
#         [' ', ' ', ' ', '#', ' ', '#'],
#         ['#', '#', ' ', '#', ' ', '#'],
#         [' ', ' ', ' ', '#', ' ', '#'],
#         [' ', '#', ' ', '#', ' ', ' '],
#         ['G', '#', '#', '#', '#', ' ']]
#
# print(find_gold(maiz, (0,0)))

# def hailstone(num):
#     print(f"At the top num = {num}")
#     if num == 1:
#         print("num=1")
#         return 0
#
#     if num % 2 == 0:
#         print(f"Num = {num}, and num % 2 = 0")
#         return hailstone(num/2) + 1  # The +1 is the number of recursions that occur and is the return value
#     else:
#         print(f"Num = {num}, and num % 2 != 0")
#         return hailstone(num*3+1) + 1
#
#
# print(hailstone(256))


# def isPalindrome(str):
#     print(f"str at the top = {str}")
#     if str == "":
#         return True
#
#     first_last = str[0] == str[-1]
#     print(f"at the return str = {str[1:-1]} and first_last = {first_last}")
#     return isPalindrome(str[1:-1]) and first_last
#
#
# print(isPalindrome("racecar"))


