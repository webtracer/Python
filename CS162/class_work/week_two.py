class OutOfRangeError(Exception):
    """

    """
    pass


def name_the_number():
    users_number = input("Please enter an integer: ")
    try:
        if users_number == 1:
            print(users_number)
        elif users_number == 2:
            print(users_number)
        elif users_number == 3:
            print(users_number)
        else:
            raise OutOfRangeError
    except OutOfRangeError:
        print("That number is out of range")


def multiply_3_numbers(num_1, num_2, num_3):
    result = num_1 * num_2 * num_3
    return result


# name_the_number()

"""
Quiz 2 code questions
"""

# li = ["hi", "hello", "hey"]
#
# for s in li:
#     try:
#         print(s[3])
#     except IndexError:
#         print("String is too short")
#     else:
#         print("This string has more than 3 characters")

# li = ["one"]
# try:
#     print(li[2])
# except IndexError:
#     print("List is too short")

class HPError(Exception):
    pass


def hpmadlibs(day, name, creature):
    if name != "Voldemort":
        print("It was a sunny ", day, "at Hogwarts when ", name, "suddenly stopped and pointed toward the lake shore.")
        print("'Look over there, I think a ", creature, "has escaped from Hagrid's collection!' ", name, "shouted.")
    else:
        raise HPError


hpmadlibs("Tuesday", "Voldemort", "hippogriff")