import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1

        if guess < number_to_guess:
            print("Higher!")
        elif guess > number_to_guess:
            print("Lower!")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break

guess_the_number()