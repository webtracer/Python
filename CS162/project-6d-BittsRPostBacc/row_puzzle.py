def row_puzzle(row_to_inspect, current_index=0, next_index=0, visited=None, last_index=0):
    """

    :param row_to_inspect:
    :param current_index:
    :param next_index:
    :param visited:
    :param last_index:
    :return:
    """

    if len(row_to_inspect) == 0:
        return True

    if last_index == 0:
        last_index = current_index

    if visited is None:
        visited = {}

    if current_index not in visited:
        if current_index == 0:
            current_value = row_to_inspect[current_index]
            visited[current_index] = current_index
            last_index = current_index
            row_puzzle(row_to_inspect,current_index+current_value,0,visited,last_index)
        else:
            if current_index > len(row_to_inspect) - 1:
                row_puzzle(row_to_inspect, current_index - last_index, 0, visited, last_index)
            elif current_index == len(row_to_inspect) - 1 and row_to_inspect[current_index] == 0:
                return True
            elif current_index == len(row_to_inspect) - 1 and row_to_inspect[current_index] != 0:
                return False
            else:
                current_value = row_to_inspect[current_index]
                next_index = current_index+current_value

            if next_index > len(row_to_inspect) -1:
                next_index = current_index - current_value
                visited[current_index] = current_index
                last_index = current_index
                row_puzzle(row_to_inspect, next_index,0,visited,last_index)
            elif next_index == len(row_to_inspect) - 1 and row_to_inspect[next_index] == 0:
                return True
            elif next_index == len(row_to_inspect) - 1 and row_to_inspect[next_index] != 0:
                return False
            else:
                visited[current_index] = current_index
                last_index = current_index
                row_puzzle(row_to_inspect,next_index,0,visited,last_index)
    else:
        if last_index > current_index:
            if last_index - current_index > 0:
                row_puzzle(row_to_inspect, last_index - current_index, 0, visited, last_index)
            else:
                row_puzzle(row_to_inspect, current_index-last_index, 0, visited, last_index)
        elif last_index == current_index:
            # row_puzzle(row_to_inspect, last_index + current_index, 0, visited, last_index)
            # row_puzzle(row_to_inspect, next_index + current_index, 0, visited, last_index)
            row_puzzle(row_to_inspect, last_index, 0, visited, last_index)
        else:
            row_puzzle(row_to_inspect,current_index-last_index,0,visited,last_index)

     
solvable_row = [2, 4, 5, 3, 1, 3, 1, 4, 0]
unsolvable_row = [1, 3, 2, 1, 3, 4, 0]
# blank_row = []

indexed = 0
for item in solvable_row:
    print(f"Index: {indexed}, value: {item}")
    indexed += 1

# print(row_puzzle(solvable_row))
print(row_puzzle(unsolvable_row))
# print(row_puzzle(blank_row))
