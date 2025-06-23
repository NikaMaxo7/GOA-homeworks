def find_average(numbers):
    if not numbers:
        return 0
    else:
        total = 0
        for num in numbers:
            total += num
        return total / len(numbers)