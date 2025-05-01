age = int(input("enter age: "))

if age <= 10:
    print("Kid")
elif age > 10 and age < 18:
    print("Teenager")
elif age >= 18 and age < 30:
    print("Adult")
else:
    print("UNC")