def sum_two_smallest_numbers(numbers):
    if numbers[0] < numbers[1]:
        smallest = numbers[0]
        second_smallest = numbers[1]
    else:
        smallest = numbers[1]
        second_smallest = numbers[0]

    for i in range(2, len(numbers)):
        num = numbers[i]
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num

    return smallest + second_smallest