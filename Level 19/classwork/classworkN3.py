def remove_odds(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result
print(remove_odds([1, 2, 3, 4, 5, 6, 7]))