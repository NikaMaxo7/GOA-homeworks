def Sum(lst):
    i = 0
    total = 0
    while i < len(lst):
        total += lst[i]
        i += 1
    return f"Sum: {total}"

print(Sum([5,5,5,5]))