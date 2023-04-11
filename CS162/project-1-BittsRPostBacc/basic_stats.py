# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 01/08/2023
# Description: basic_stats - determines the mode, mean and median of a list of student grades
#           pulling the grades from the student objects that are created from the list provided at runtime

# import the statistics module
import statistics


class Student:
    """
    A class representing a students name and grade
    """
    def __init__(self, name, grade):
        """
        Default constructor for the Student Class
        :param name: Students Name
        :param grade: Students Grade
        """
        self._name = name
        self._grade = grade

    def get_grade(self):
        """
        Getter for the Student class
        :return: Students grade
        """
        return self._grade


def basic_stats(students):
    """
    The basic_stats function takes a list of student objects and returns the made, median and mean of their grades
    :param students: A list of Student class objects
    :return: stats_tuple containing the mode median and mean of all student grades
    """
    grades = []
    for item in students: # Run through each item in the list, and store the grades in a different list
        grades.append(item.get_grade())

    # Create the stats tuple, and pull the grades while getting the mean, median and mode
    stats = (statistics.mean(grades), statistics.median(grades), statistics.mode(grades))
    # return f"Median Grade: {median}, Mode Grade: {mode}, Mean Grade: {mean}"
    return stats


# s1 = Student("Kyoungmin", 73)
# s2 = Student("Mercedes", 74)
# s3 = Student("Avanika", 78)
# s4 = Student("Marta", 74)
#
# student_list = [s1, s2, s3, s4]
# print(basic_stats(student_list))  # should print a tuple of three values
