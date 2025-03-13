password = "goa123"
attempts = 0

while attempts < 3:
    user = input("enter password: ")
    if user == password:
        print("Correct Password!")
        break
    else:
        attempts = attempts + 1
        print(f"Wrong password attempts left: {3 - attempts}")

if attempts == 3:
    print("You ran out of the attempts")

else:
    num = int(input("please input a number: "))
    count = 0
    while num == 1:
        num = int(input("try another number: "))

    for i in range(2, num):
        if num % i == 0 and count == 0:
            print('Your number is not a prime')
            count += 1

    if count == 0:
        print('your number is a prime')
