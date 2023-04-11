import random


def bubble_sort(a_list):
    """
    Sorts a_list in ascending order
    """

    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp
            print(a_list)

    return a_list


def insertion_sort(a_list):
  """
  Sorts a_list in ascending order
  """
  for index in range(1, len(a_list)):
    value = a_list[index]
    pos = index - 1
    while pos >= 0 and a_list[pos] > value:
      a_list[pos + 1] = a_list[pos]
      pos -= 1
    a_list[pos + 1] = value

    return a_list


def random_list():
    new_list = []
    builder_list = []
    i = 0

    for x in range(1,25):
        j = random.randint(1, 1000)
        new_list.append(j)

    # while i < len(builder_list):
    #     j = random.randint(1,1000)
    #     list.append(j)
    #     i += 1

    return new_list


list_to_sort = random_list()
print(list_to_sort)
bubble_sort(list_to_sort)
# print(bubble_sort(list_to_sort))
# print(insertion_sort(list_to_sort))
# print(bubble_sort(random_list()))
# print(insertion_sort(random_list()))
