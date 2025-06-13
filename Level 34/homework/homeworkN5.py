def remove_smallest(numbers):
    if numbers == []:
        return []

    smallest = min(numbers)

    index_of_smallest = numbers.index(smallest)

    new_list = []

    for i in range(len(numbers)):
        if i != index_of_smallest:
            new_list.append(numbers[i])

    return new_list