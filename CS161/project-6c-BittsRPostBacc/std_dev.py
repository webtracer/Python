# Author: Randy Bitts
# GitHub username: BittsRPostBacc
# Date: 10/23/2022
# Description: Takes a list of Person objects (name and age) and returns the population standard deviation age

class Person:
    """    Represents an individual by name and age only    """
    def __init__(self, name, age):
        """
        Constructor for the Person Class
        :param name: name of the person
        :param age: age of the person
        """
        self._name = name
        self._age = age

    def get_age(self):
        """
        Getter for the age of the person
        :return:
        """
        return self._age


def std_dev(list_of_people):
    """ Takes a list of person objects, gets their ages
            and returns the population standard deviation of all their ages
    :param list_of_people: a list of Person objects
    :return: the population standard deviation of all their ages
    """
    ages = []
    simple_age_mean = 0  # Stores the simple average of the ages
    subtract_and_square = []  # Stores the value of each (age - minus simple_age_mean)^2
    age_variance = 0  # this is the simple average of the "subtract and squared" values

    #  get all the ages, add them to the ages list and add them to the simple_age_mean variable
    for person in list_of_people:
        ages = ages + [(person.get_age())]
        simple_age_mean += person.get_age()

    simple_age_mean = simple_age_mean / len(ages)  # calculates the simple average

    # for each age, we need to subtract the mean, and square the result
    for age in ages:
        subtract_and_square += [((age - simple_age_mean)**2)]

    # add all the "subtract and square" ages together
    for age in subtract_and_square:
        age_variance += age
    age_variance = age_variance / len(ages)  # and find the simple average

    # this is the square root of the age variance and final step
    pop_standard_deviation = age_variance ** 0.5

    return pop_standard_deviation


# p1 = Person("Kyoungmin", 73)
# p2 = Person("Mercedes", 24)
# p3 = Person("Beatrice", 48)
# person_list = [p1, p2, p3]
# answer = std_dev(person_list)

# Test Case from the example of calculating the population standard deviation page in the Readme.md file
#     the calculated answer on the webpage is 2.983, and my function returns 2.9832867780352594
# p1 = Person("Cooper", 9)
# p2 = Person("Gracie", 2)
# p3 = Person("Blake", 5)
# p4 = Person("Randy", 4)
# p5 = Person("laura", 12)
# p6 = Person("Mike", 7)
# p7 = Person("Mae", 8)
# p8 = Person("Jeff", 11)
# p9 = Person("Olivia", 9)
# p10 = Person("Luke", 3)
# p11 = Person("Noah", 7)
# p12 = Person("Hannah", 4)
# p13 = Person("Jessica", 12)
# p14 = Person("Art", 5)
# p15 = Person("Joanne", 4)
# p16 = Person("Terri", 10)
# p17 = Person("Neal", 9)
# p18 = Person("Loretta", 6)
# p19 = Person("Joe", 9)
# p20 = Person("Alma", 4)
#
# person_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20]
# answer = std_dev(person_list)
# print(answer)
