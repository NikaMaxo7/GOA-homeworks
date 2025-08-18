def even_or_odd():
    n = int(input("Enter a number: "))
    if n % 2 == 0:
        return "The number is Even"
    else:
        return "The number is Odd"

print(even_or_odd())