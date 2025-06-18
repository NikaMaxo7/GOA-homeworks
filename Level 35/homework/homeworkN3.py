def check_age():
    age = int(input("Enter your age: "))

    if age > 18:
        return("You are an adult.")
    elif age < 18:
        return("You are not an adult.")
    else:
        return("You are exactly 18 years old.")

check_age()