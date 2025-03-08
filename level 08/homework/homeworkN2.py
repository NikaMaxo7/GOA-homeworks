secret_number1 = 3
secret_number2 = 7
secret_number3 = 2
secret_number4 = 9

while True:
    guess1 = int(input("enter first number: "))
    guess2 = int(input("enter second number: "))
    guess3 = int(input("enter third number: "))
    guess4 = int(input("enter fourth number: "))

    if guess1 == secret_number1 and guess2 == secret_number2 and guess3 == secret_number3 and guess4 == secret_number4:
        print("Congrats! You Guessed It Right")
        break
    else:
        print("Wrong! Try again")
