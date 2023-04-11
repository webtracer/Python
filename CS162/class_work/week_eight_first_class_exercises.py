
def greeting(name):
    """
    takes a name and returns a personalized greeting
    :param name:
    :return:
    """

    return f"Hello {name}"

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
