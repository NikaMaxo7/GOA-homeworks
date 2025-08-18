def sum_and_average():
    numbers = []

    for i in range(5):
        num = int(input("Enter a number: "))
        numbers.append(num)

    total = sum(numbers)
    average = total / len(numbers)

    return "Sum:", total, "Average:", average

print(sum_and_average())