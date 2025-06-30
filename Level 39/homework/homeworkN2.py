def Sum(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    return f"Sum: {total}"

print(Sum([5,5,5,5]))