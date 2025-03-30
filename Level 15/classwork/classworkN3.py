def even_last(numbers):
    if not numbers:
        return 0
    even_sum = 0
    for i in range(0, len(numbers), 2):
        even_sum += numbers[i]

    return even_sum * numbers[-1]