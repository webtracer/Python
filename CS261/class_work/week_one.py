# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date:
# Description:

# example

def fooMain():
    '''
    Get input from a user to create a matrix of inputted size
    '''

    # (matrixX, matrixY, squared(T/F))
    userInput = get_input()

    matrix = create_matrix(userInput[0], userInput[1], userInput[2])
    print_matrix(matrix)


def get_input():
    '''
    Prompt user for matrix size input
    '''

    # Prompts
    matrixX = input("How many rows do you want your matrix to have    :")
    matrixY = input("How many columns do you want your matrix to have :")
    squared = input("Do you want your Matrix Squared (T or F)         :")

    # Squared needs to be True or False
    while squared not in ("T", "F"):
        squared = input("Do you want your Matrix Squared (T or F)    :")

    # Set sqaured to boolean value
    if squared == "T":
        squared = True
    else:
        squared = False

    return (int(matrixX), int(matrixY), squared)


def create_matrix(matrixX, matrixY, squared=False):
    '''
    Create a list of list representing a matrix based on user input
    '''
    arrs = []

    # Fills matrix
    for x in range(matrixX):
        arrs.append(create_list(matrixY, x, squared))

    return arrs


def create_list(total, skip, squared=False):
    '''
    Creates a single list of size total
    '''
    if squared is False:
        return [x * skip for x in range(total)]

    return [(x * skip) * (x * skip) for x in range(total)]


def print_matrix(matrix):
    '''
    Prints the matrix in a readable way
    '''
    for row in matrix:
        print(row)


fooMain()

print("Spam"*3)  # String repetition

