# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 03/01/2023
# Description: Program that generates multiple random lists of differing sizes and compares the time it takes for
# both the bubble and insertion sorts to sort the lists, then generates a graph for visual comparison

import time, random, functools      # Import the time, random and functools modules
from matplotlib import pyplot       # Explicitly import the pyplot functions from matplotlib module


def sort_timer(func):
    """
    Decorator Function to time the two sort functions
    :param func: name of the function to decorate
    :return: total elapsed time (End Time - Start Time)
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        return end_time-start_time
    return wrapper


@sort_timer     # decorate the insertion_sort function with sort timer
def bubble_sort(*args):
    """
    Function to perform a bubble_sort, courtesy of Module 4
    :param args: the List to sort through
    :return: Nothing
    """
    for pass_num in range(len(args) - 1):
        for index in range(len(args) - 1 - pass_num):
            if args[index] > args[index + 1]:
                temp = args[index]
                args[index] = args[index + 1]
                args[index + 1] = temp


@sort_timer     # decorate the insertion_sort function with sort timer
def insertion_sort(*args):
    """
    Function to perform an insertion sort, courtesy of Module 4
    :param args: The list to sort through
    :return: Nothing
    """
    for index in range(1, len(args)):
        value = args[index]
        pos = index - 1
        while pos >= 0 and args[pos] > value:
            args[pos + 1] = args[pos]
            pos -= 1
            args[pos + 1] = value


def compare_sorts(func1, func2, limit=1000, bubble_time=[], insertion_time=[], range_to_sort=[]):
    """
    Recursive function to perform both Bubble and Insertion sorts on the same lists, which vary in size from call
        to call.  When the recursion is done and the data is gathered, function exits to the Graphing function
    :param func1: Bubble Sort function declaration
    :param func2: Insertion Sort function declaration
    :param limit: Initial size 1000, increases with each recursion call
    :param bubble_time: Initial list to hold the bubble sort times of each list
    :param insertion_time: Initial list to hold the insertion sort times of each list
    :param range_to_sort: Holds the size values of each list to use as the y-axis
    :return: Recursion returns each set of variables, with the values they contain to stay current
    """

    first_list = []                 # List to store the random numbers
    range_to_sort.append(limit)     # update the y-axis values for the graph

    # generate a list of random numbers between 1 and 10000, with the limit variable determining list size
    for x in range(1, 10000):
        j = random.randint(1, limit)
        first_list.append(j)

    second_list = list(first_list)  # Copy the first list into the second list

    bubble_time.append(func1(first_list))       # Call the bubble_sort function and time it takes, and add to list
    insertion_time.append(func2(second_list))   # Call the insertion_sort function and time it takes, and add to list

    limit += 1000                   # Increase limit by 1000 for the next function call
    if limit < 10001:               # Last recursive call will be at 10,000
        compare_sorts(bubble_sort, insertion_sort, limit, bubble_time, insertion_time, range_to_sort)

    # Now that we are done gathering data, lets plot it
    plot_data(bubble_time, insertion_time, range_to_sort)


def plot_data(bubble_data, insertion_data, x_axis_data):
    """
    Function to generate a graph to display the difference in sorting times between the algorithms
    :param bubble_data: List of the times the Bubble Sort took with each list
    :param insertion_data: List of the times the Insertion took with each list
    :param x_axis_data: The quantity of values that were in each list
    :return: Nothing other than the generated graph
    """

    # The two "pyplot.plot" calls plot the individual data for each sort with differing graph visuals
    pyplot.plot(x_axis_data,  bubble_data, marker='*', markersize=9, color='blue', linewidth=1,
                label='Bubble Sort Times')
    pyplot.plot(x_axis_data,  insertion_data, marker='^', markersize=9, color='green', linewidth=1,
                linestyle="dashed", label='Insertion Sort Times')
    pyplot.xlabel("Records to Sort")        # Label for the X Axis
    pyplot.ylabel("Time To Sort")           # Label for the Y Axis
    pyplot.legend(loc='best')               # Let the pyplot function determine where to put the graph legend
    pyplot.title("Time Comparison Between Bubble and Insertion Sorts")  # Graph title
    pyplot.grid(True)                       # Add gridlines to the background, after all it just looks better
    pyplot.show()                           # show the graph


compare_sorts(bubble_sort, insertion_sort)
