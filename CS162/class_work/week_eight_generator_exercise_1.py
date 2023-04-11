# def even_numbers(limit):
#   """Generates all even numbers from zero up to, but not including, limit"""
#   num = 0
#   while num < limit:
#     yield num
#     num += 2
#
# gen_1 = even_numbers(101)
#
# for val in gen_1:
#   print(val)

def squares_generator (limit):
    """
    Prints out all the squares up to 10,000
    :return:
    """
    num = 1
    while num < limit:
        yield num * num
        num += 1


squares = squares_generator(101)

# for square in squares_generator:
#     print(square)
