def factorial():
    n = int(input("Enter a number: "))

    result = 1

    for i in range(1, n + 1):
        result *= i

    return "Factorial:", result

print(factorial())