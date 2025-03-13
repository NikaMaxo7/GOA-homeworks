number = int(input("enter number: "))

sum_odd = 0

for i in range(1, number + 1):
    if i % 2 != 0:
        sum_odd += i

print("The sum of odd numbers is:", sum_odd)
