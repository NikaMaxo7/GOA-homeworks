numbers = [3, 7, 12, 5, 18, 1]

greater_than_5 = []

for num in numbers:
    if num > 5:
        greater_than_5.append(num)

print("Numbers greater than 5:", greater_than_5)
print("Count of numbers > 5:", len(greater_than_5))