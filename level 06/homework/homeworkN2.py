num = int(input("enter number: "))

print(f"{num}-The following numbers are evenly divisible by:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
