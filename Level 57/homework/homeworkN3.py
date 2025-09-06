def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

for i in range(3):
    num = int(input("Enter number " + str(i+1) + ": "))
    
    if is_even(num):
        print("Number", num, "is even")
    else:
        print("Number", num, "is odd")