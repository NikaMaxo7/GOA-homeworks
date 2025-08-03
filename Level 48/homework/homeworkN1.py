numbers = [1, 2, 3, 2, 4, 5, 3, 6, 7, 2]
seen = []
duplicates = []

for num in numbers:
    if num in seen:
        if num not in duplicates:
            duplicates.append(num)
    else:
        seen.append(num)

print("Duplicates:", duplicates)