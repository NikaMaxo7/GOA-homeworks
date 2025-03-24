num = int(input("enter number: "))

def calculating():
    if num % 2 == 0:
        x = num + 5
    else:
        x = num * 3
    sum = num + x
    remains = sum % 5

print(calculating())