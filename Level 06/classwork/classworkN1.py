num1 = int(input("enter number: "))

if num1 > 1:
    for i in range(2, num1):
        if num1 % i ==0:
            print("your number is not a prime")
            break
    else:
        print("your number is prime")
else:
    print("your number is not prime")
