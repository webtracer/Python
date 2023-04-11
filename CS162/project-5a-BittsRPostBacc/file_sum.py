# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 02/02/2023
# Description: Program contains a function that takes as input a file that contains lines of numbers,
#                   reads them in, sums them and then writes the total to a separate file

def file_sum(file_name):
    """
    Takes the name of a file that contains numbers
    :param file_name: name of the file that contains numbers
    :return: Nothing, but output a file that contains the sum of the input numbers
    """
    number_sum = 0.0
    output_file = "sum.txt"

    with open(file_name, 'r') as infile:
        for x in infile:
            number_sum += float(x.strip())

    with open(output_file, 'w') as outfile:
        outfile.write(str(number_sum))


# file_sum("/Users/randybitts/Documents/OSU Classes/Winter_2023/CS_162/numbers_for_162_5a.txt")