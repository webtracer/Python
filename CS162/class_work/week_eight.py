# Generators and Decorators
import functools    # needed by Decorator at the end
import json         # used by the lecture decorator example
# Generators

def even_numbers(limit):
  """Generates all even numbers from zero up to, but not including, limit"""
  num = 0
  while num < limit:
    yield num
    num += 2

gen_1 = even_numbers(101)

for val in gen_1:
  print(val)

# Decorators and first class functions

def sum(num_1, num_2):
    """Adds two numbers"""
    return num_1 + num_2


add = sum
print(add(7, 3))


def sum(num_1, num_2):
    """Adds two numbers"""
    return num_1 + num_2


def mult(num_1, num_2):
    """Multiplies two numbers"""
    return num_1 * num_2


def perform_binary_op(func, num_1, num_2):
    """
    Calls func(num_1, num_2) and returns the value returned by that function call
    """
    return func(num_1, num_2)


print(perform_binary_op(sum, 9, 8))
print(perform_binary_op(mult, 9, 8))


def double_plus_one(num):
    """returns 1 plus double the value of the argument"""

    def double(n):
        """returns double the value of the argument"""
        return n * 2

    return double(num) + 1


print(double_plus_one(5))


def get_double_func():
    """Returns a function that doubles a number"""

    def double(n):
        """Returns double the value of the argument"""
        return n * 2

    return double


twice = get_double_func()
print(twice(9))


def get_multiplier_by(factor):
    """Returns a function that multiplies its argument by the given factor"""

    def multiplier(n):
        """Multiplies the argument by a factor"""
        return n * factor

    return multiplier


mult7 = get_multiplier_by(7)
print(mult7(9))


def generic_decorator(func):
    """Adds printing of generic messages to func"""

    def wrapper():
        print("additional behavior before the function call")
        func()
        print("additional behavior after the function call")

    return wrapper


@generic_decorator
def greeting():
    """Prints a greeting"""
    print("hello world")


greeting = generic_decorator(greeting)

greeting()


def generic_decorator(func):
    """Adds printing of generic messages to func"""

    def wrapper():
        print("additional behavior before the function call")
        result = func()
        print("additional behavior after the function call")
        return result

    return wrapper


@generic_decorator
def greeting():
    """Returns a greeting"""
    return "hello world"


print(greeting())


def generic_decorator(func):
    """Adds printing of generic messages to func"""

    def wrapper(*args, **kwargs):
        print("additional behavior before the function call")
        result = func(*args, **kwargs)
        print("additional behavior after the function call")
        return result

    return wrapper


@generic_decorator
def increment(num):
    """Increments num by 1"""
    return num + 1


@generic_decorator
def add_three(num_1, num_2, num_3):
    """Returns the sum of the three arguments"""
    return num_1 + num_2 + num_3


print(increment(3))
print(add_three(2,3,4))


def generic_decorator(func):
  """Adds printing of generic messages to func"""
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    print("additional behavior before the function call")
    result = func(*args, **kwargs)
    print("additional behavior after the function call")
    return result
  return wrapper

@generic_decorator
def add_three(num_1, num_2, num_3):
  """Returns the sum of the three arguments"""
  return num_1 + num_2 + num_3


add_three(2, 14, 1)

# It's best practice to use functools.wraps() to decorate the wrapper in all your decorator functions.


def func_args_print(func):
    """Prints out the values of the parameters"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            print(arg)
        result = func(*args, **kwargs)
        return result

    return wrapper


@func_args_print
def add(num_1, num_2):
    return num_1 + num_2


print(add(7, 3))


# Lecture video

# Hailstone Recursive Generator

def hailstone(n):
    """
    Generator for the hailstone sequence
    :param n:
    :return:
    """

    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        yield int(n)


sequence = hailstone(3)

print()
print(f"Hailstone recursion sequence values:")
for value in sequence:
    print(value)
# print(next(sequence)) # Can print single sequence values instead of looping
print()


def generic_decorator(func):
    """
    Adds printing of generic messages to func
    :param func:
    :return:
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # print("Something before the function call")
        result = func(*args, **kwargs)
        # print("And this happens after the function call")
        print(json.dumps(result, indent=4))
        return result
    return wrapper()


@generic_decorator
def generate_json():
    example = {"squadName": "super hero squad", "homeTown": "Gotham City", "formed": "1937"}
    with open("example.json", 'w') as outfile:
        json.dump(example, outfile)
    return example


# generate_json()

stuff = (c for c in "AlphAbEt" if c.isupper())

print(type(stuff))

junk = [x for x in range(100) if x%2]
print(type(junk))

paraphernalia = {'a': "aacorn", 'b': "broccolini"}
print(type(paraphernalia))

panoply = {1, 2, 3, 4, 5}
print(type(panoply))

def concat_strings():
    def cat(s1, s2):
        return s1+s2
    return cat


print(cat("pers", "picacious"))