# Slower Version

def unique_numbers(lst):
    result = []

    for i in lst:
        if lst.count(i) == 1:
            result.append(i)

    return result

print(unique_numbers([1, 2, 3, 2, 4, 5, 5]))

# Faster Version

def unique(lst):
    freq = {}

    for i in range(len(lst)):
        freq[lst[i]] = freq.get(lst[i], 0) + 1

    result = []

    for key, value in freq.items():
        if value == 1:
            result.append(key)
    return result

print(unique([1, 2, 3, 2, 4, 5, 5]))