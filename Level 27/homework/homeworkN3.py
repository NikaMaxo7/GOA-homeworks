num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))
if num1 > num2 and num1 > num3:
    print(f"Biggest Number Is {num1}")
if num2 > num1 and num2 >num3:
    print(f"Biggest Number Is {num2}")
else:
    print(f"Biggest Number Is {num3}")