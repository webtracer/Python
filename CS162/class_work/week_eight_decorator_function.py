# Write a decorator named debug that prints "Entering "
# followed by the name of the decorated function (func.__name__)
# before calling it and prints "Exiting "
# followed by the name of the decorated function after calling it.

import functools


# def greeting(name):
#     """
#     takes a name and returns a personalized greeting
#     :param name:
#     :return:
#     """
#
#     return f"Hello {name}"


# def shout(func, name):
#     """
#
#     :param func:
#     :param name:
#     :return:
#     """
#     hi_there = func(name)
#     return hi_there.upper()


def debug(func):
    """

    :param func:
    :return:
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Entering {func}")
        result = func(*args, **kwargs)
        print(f"Exiting {func}")
        return result
    return wrapper


@debug
def greeting(name):
    """
    takes a name and returns a personalized greeting
    :param name:
    :return:
    """

    return f"Hello {name}"

@debug
def shout(func, name):
    """

    :param func:
    :param name:
    :return:
    """
    hi_there = func(name)
    return hi_there.upper()


if __name__ == "__main__":
    print(greeting("Laura"))
    print(shout(greeting, "Laura"))
